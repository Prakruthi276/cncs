import smtplib
from email.mime.text import MIMEText
from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure your SQL database here
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Prajwal%40123@localhost/new'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Email model
class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(120), nullable=False)
    recipients = db.Column(db.String(120), nullable=False)
    body = db.Column(db.Text, nullable=False)

# Route to display the HTML form
@app.route('/')
def index():
    return render_template('index.html')  # Make sure this HTML file exists in the templates folder

# Route to send the email and store its details
@app.route('/send_email', methods=['POST'])
def send_email():
    try:
        sender = request.form['sender']
        recipient = request.form['recipient']
        subject = request.form['subject']
        body = request.form['body']

        # Create email message
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = recipient

        # Send the email via SMTP
        with smtplib.SMTP('localhost', 2526) as server:  # Ensure this matches your SMTP config
            server.sendmail(sender, recipient, msg.as_string())

        # Store email details in the database
        new_email = Email(sender=sender, recipients=recipient, body=body)
        db.session.add(new_email)
        db.session.commit()

        return "Email sent and stored successfully!"

    except Exception as e:
        return f"Failed to send and store email: {e}"

# Route to store email directly via JSON
@app.route('/store_email', methods=['POST'])
def store_email():
    try:
        data = request.get_json()
        sender = data.get('sender')
        recipients = data.get('recipients')
        body = data.get('body')

        if not sender or not recipients or not body:
            raise ValueError("Sender, recipients, and body are required.")

        # Store email in the database
        new_email = Email(sender=sender, recipients=recipients, body=body)
        db.session.add(new_email)
        db.session.commit()

        return jsonify({"status": "success", "message": "Email data stored successfully!"}), 200

    except ValueError as ve:
        return jsonify({"status": "error", "message": str(ve)}), 400

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"status": "error", "message": "An unexpected error occurred"}), 500

# Initialize the database
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create the database tables
    app.run(debug=True)