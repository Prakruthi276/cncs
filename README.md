 Flask-Based SMTP Email Server with MySQL Integration  

 Overview  
This project is a Flask-based SMTP email server designed for sending and managing emails locally. The server integrates HTML and CSS for the front-end, Flask for the back-end, and MySQL as the database. It runs on localhost and provides functionality to send, receive, and store email data efficiently.  

 Features  
- SMTP Protocol Support: Enables email handling for sending and receiving.  
- Flask Framework: Serves as the back-end for managing server operations.  
- MySQL Integration: Stores email information in a robust database.  
- User-Friendly Interface: Built with HTML and CSS for an intuitive front-end experience.  
- Localhost Deployment: Designed to operate locally for development and testing purposes.  

 Installation  

 Prerequisites  
- Python 3.7 or above  
- Flask  
- MySQL  
- SMTP Server (`aiosmtpd` recommended for local testing)  

 Setup Steps  
1. Clone the Repository:  
   ```bash  
   git clone https://github.com/your-username/email_server_smtp_flask.git  
   cd email_server_smtp_flask  
2.Install Dependencies:
   ```bash
   pip install -r requirements.txt
3.Set Up MySQL Database:
  Create a MySQL database and configure the connection details in the Flask app (update app.py with your MySQL credentials).
  Example:app.config['MYSQL_HOST'] = 'localhost'
          app.config['MYSQL_USER'] = 'root'
          app.config['MYSQL_PASSWORD'] = 'your-password'
          app.config['MYSQL_DB'] = 'email_server'
4.Run the Application:
  Start the Flask server:
           python app.py  
  Access the application in your browser: http://127.0.0.1:5000
5.Set Up SMTP Server:
   Run an SMTP server locally (e.g., using aiosmtpd):
   python -m aiosmtpd -n -c DebuggingServer localhost:1025

Project Structure:
email_server_smtp_flask/  
├── static/                # CSS and assets  
├── templates/             # HTML templates  
├── app.py                 # Flask application  
├── config.py              # Configuration settings  
├── requirements.txt       # Python dependencies  
└── README.md              # Project documentation  

Usage
Navigate to the home page to compose and send emails.
Sent emails are stored in the MySQL database and can be managed through the application.
Contact:
For questions or contributions, please reach out via prakruthimv276@gmail.com.
   
