# Secure Resort Chatbot

This project is a secure chatbot for a resort website that uses end-to-end encryption to ensure the privacy and security of messages exchanged between users and the resort bot. The application features user authentication through social media and email verification, and a web-based user interface for ease of use.

## Project Structure

```
secure_chat_bot/
│
├── server/
│   ├── app.py
│   ├── models.py
│   ├── routes.py
│   ├── config.py
│   └── requirements.txt
│
├── client/
│   ├── main.py
│   ├── encryption.py
│   ├── templates/
│   │   ├── index.html
│   │   ├── chat.html
│   └── static/
│       ├── css/
│       │   └── style.css
│       └── js/
│           └── script.js
│
└── README.md
```

## Getting Started

### Server Setup

1. Navigate to the `server` directory:

   ```sh
   cd server
   ```

2. Install the required packages:

   ```sh
   pip install -r requirements.txt
   ```

3. Run the Flask server:

   ```sh
   flask run
   ```

### Client Setup

1. Navigate to the `client` directory:

   ```sh
   cd client
   ```

2. Install the required packages:

   ```sh
   pip install -r requirements.txt
   ```

3. Run the client application:

   ```sh
   python main.py
   ```

### Web UI Setup

1. Navigate to the `client` directory:

   ```sh
   cd client
   ```

2. Open `index.html` in a web browser:

   ```sh
   open templates/index.html
   ```

## Features

- **User Authentication**: Users can authenticate via social media (Google) or email.
- **End-to-End Encryption**: Messages are encrypted using Diffie-Hellman key exchange and AES encryption.
- **Email Verification**: New users must verify their email address during registration.
- **Web-Based UI**: The application provides a web-based interface for chatting with the resort bot.

## Security Considerations

- **End-to-End Encryption**: Ensures that messages can only be read by the intended recipient.
- **OAuth Authentication**: Uses secure OAuth protocol for social media authentication.
- **Email Verification**: Adds an extra layer of security by verifying users' email addresses.
- **Session Keys**: Derived using PBKDF2 with a high iteration count to ensure security.

## Future Improvements

- **Two-Factor Authentication**: Adding an extra layer of security.
- **Improved Error Handling**: More robust error handling and user feedback.
- **Group Chats**: Extending functionality to support group communications.

## License

This project is licensed under the MIT License.

---

### Notes
1. Replace `YOUR_GOOGLE_CLIENT_ID` and `YOUR_GOOGLE_CLIENT_SECRET` with your actual credentials from the Google Developer Console.
2. Implement the `send_verification_email` function to send actual emails using an email service provider.

If you already have a virtual environment, remove it and create a new one to ensure a clean installation of dependencies.

 ```sh
    cd secure_chat_bot/server
    rm -rf venv
    python -m venv venv
    source venv/bin/activate  # On Windows use venv\Scripts\activate
    pip install --upgrade pip
    pip install -r requirements.txt
   ```

This setup provides a secure, end-to-end encrypted chatbot for a resort website with user-friendly authentication and a web-based interface.
