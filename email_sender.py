from flask import Flask, request, jsonify
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

def send_email(recipient_email, subject, message):
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = 'travel.exploooration@gmail.com'
    EMAIL_HOST_PASSWORD = 'blvz upxg bdih mqht'  # Use environment variables for sensitive data

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = EMAIL_HOST_USER
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the message
    msg.attach(MIMEText(message, 'plain'))

    try:
        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.starttls()
            server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
            server.send_message(msg)
        # lo.info(f"Email sent to {recipient_email} successfully!")
        return True, "Email sent successfully!"

    except Exception as e:
        # mail_logger.error(f"Failed to send email: {e}")
        return False, str(e)

@app.route('/send-email', methods=['POST'])
def send_single_email():
    data = request.get_json()
    recipient_email = data['recipient_email']
    subject = data['subject']
    message = data['message']
    
    success, response_message = send_email(recipient_email, subject, message)
    if success:
        return jsonify({'message': response_message}), 200
    else:
        return jsonify({'error': response_message}), 500

@app.route('/send-emails', methods=['POST'])
def send_multiple_emails():
    data = request.get_json()
    recipient_emails = data['recipient_emails']  # Expecting a list of recipient emails
    cc_emails = data.get('cc_emails', [])  # Optional CC emails
    subject = data['subject']
    message = data['message']
    
    success, response_message = send_emails(recipient_emails, cc_emails, subject, message)
    if success:
        return jsonify({'message': response_message}), 200
    else:
        return jsonify({'error': response_message}), 500

def send_emails(recipient_emails, cc_emails, subject, message):
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = 'travel.exploooration@gmail.com'
    EMAIL_HOST_PASSWORD = 'blvz upxg bdih mqht'  # Use environment variables for sensitive data    

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = EMAIL_HOST_USER
    msg['To'] = ', '.join(recipient_emails)  # Join multiple recipients with commas
    msg['Subject'] = subject

    # Attach the message
    msg.attach(MIMEText(message, 'plain'))  # For plain text

    # Add CC recipients if any
    if cc_emails:
        msg['Cc'] = ', '.join(cc_emails)  # Join CC recipients with commas
        recipient_emails += cc_emails  # Include CC emails in the recipient list for sending

    try:
        # Connect to the email server and send the email
        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
            server.send_message(msg)

        # mail_logger.info(f"Emails sent to {recipient_emails} successfully!")
        return True, "Emails sent successfully!"

    except Exception as e:
        # mail_logger.error(f"Failed to send emails: {e}")
        return False, str(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



# curl -X POST http://192.168.15.95:5000/send-email \
# -H "Content-Type: application/json" \
# -d '{"recipient_email": "recipient@example.com", "subject": "Test Subject", "message": "This is a test message."}'



# curl -X POST http://192.168.15.95:5000/send-emails \
# -H "Content-Type: application/json" \
# -d '{"recipient_emails": ["recipient1@example.com", "recipient2@example.com"], "cc_emails": ["cc@example.com"], "subject": "Test Subject", "message": "This is a test message."}'
