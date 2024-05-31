from flask import request, jsonify, redirect, url_for, session, render_template
from app import app, db, oauth
from models import User, Message
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    redirect_uri = url_for('auth_callback', _external=True)
    return oauth.google.authorize_redirect(redirect_uri)

@app.route('/auth/callback')
def auth_callback():
    token = oauth.google.authorize_access_token()
    user_info = oauth.google.parse_id_token(token)
    session['user'] = user_info
    return redirect('/chat')

@app.route('/chat')
def chat():
    if 'user' not in session:
        return redirect('/')
    return render_template('chat.html', user=session['user'])

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    email = data['email']
    username = data['username']
    password = data['password']
    verification_code = os.urandom(6).hex()
    new_user = User(username=username, email=email, password=password, verification_code=verification_code)
    db.session.add(new_user)
    db.session.commit()
    send_verification_email(email, verification_code)
    return jsonify({'message': 'Registration successful, please verify your email'}), 201

@app.route('/verify_email', methods=['POST'])
def verify_email():
    data = request.json
    email = data['email']
    code = data['code']
    user = User.query.filter_by(email=email, verification_code=code).first()
    if user:
        user.verified = True
        db.session.commit()
        return jsonify({'message': 'Email verified successfully'}), 200
    return jsonify({'message': 'Invalid verification code'}), 400

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    new_message = Message(sender=data['sender'], recipient=data['recipient'], encrypted_message=data['message'])
    db.session.add(new_message)
    db.session.commit()
    return jsonify({'message': 'Message sent'}), 201

@app.route('/receive_messages/<recipient>', methods=['GET'])
def receive_messages(recipient):
    messages = Message.query.filter_by(recipient=recipient).all()
    return jsonify([{'sender': msg.sender, 'message': msg.encrypted_message} for msg in messages]), 200

def send_verification_email(email, code):
    # Email configuration
    sender_email = 'mruduladidde@gmail.com'  # Replace with your email
    sender_password = 'DBS@20006086'  # Replace with your password
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  # For SSL use 465

    # Create message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = email
    message['Subject'] = 'Verification Code for Resort Chatbot'

    body = f'Your verification code is: {code}. Enter this code to complete registration.'
    message.attach(MIMEText(body, 'plain'))

    # Connect to SMTP server and send email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, email, message.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        server.quit()
