from aiosmtpd.controller import Controller 
import requests

class CustomSMTPHandler:
    async def handle_DATA(self, server, session, envelope):
        mailfrom = envelope.mail_from
        rcpttos = envelope.rcpt_tos
        data = envelope.content.decode('utf8', errors='replace')

        # Log received email details
        print(f"Received message from: {mailfrom}")
        print(f"Message addressed to: {rcpttos}")
        print(f"Message body:\n{data}")

        # Prepare the email data for Flask backend
        email_data = {
            "sender": mailfrom,
            "recipients": ','.join(rcpttos),
            "body": data
        }

        try:
            print("Sending email data to Flask backend...")
            response = requests.post('http://127.0.0.1:5000/store_email', json=email_data, timeout=10)

            # Check the Flask backend response
            if response.status_code == 200:
                print("Email data successfully stored in the backend.")
                return '250 OK'  # SMTP success code
            else:
                print(f"Failed to store email data: {response.text}")
                return f'554 Error: {response.text}'  # Return the actual error from Flask backend

        except Exception as e:
            print(f"Error while storing email data: {e}")
            return '554 Error: Unable to process email'  # SMTP error response

if __name__ == "__main__":
    handler = CustomSMTPHandler()
    controller = Controller(handler, hostname='127.0.0.1', port=2526)
    controller.start()
    print("SMTP Server running on port 2526...")

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\nStopping the server...")
        controller.stop()  