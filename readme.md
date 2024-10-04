http://192.168.15.95:9999/email/send


{"recipientEmail": "recipient@example.com", "subject": "Test Email", "message": "This is a test email."}



http://192.168.15.95:9999/email/send-cc

{
    "to": "chinmay09jena@gmail.com",
    "cc": ["chinmay.jena7878@gmail.com"],//separated by comma
    "subject": "Test Email",
    "message": "This is a test email with CC."
}


{
    "to": "chinmay09jena@gmail.com",
    "cc": [], //null
    "subject": "Test Email",
    "message": "This is a test email with CC."
}


http://192.168.15.95:5000/send-email



{
    "recipient_email": "chinmay09jena@gmail.com",
    "subject": "Test Email",
    "message": "Hello, this is a test email!"
}





curl -X POST http://192.168.15.95:5000/send-email \
-H "Content-Type: application/json" \
-d '{"recipient_email": "recipient@example.com", "subject": "Test Subject", "message": "This is a test message."}'



curl -X POST http://192.168.15.95:5000/send-emails \
-H "Content-Type: application/json" \
-d '{"recipient_emails": ["recipient1@example.com", "recipient2@example.com"], "cc_emails": ["cc@example.com"], "subject": "Test Subject", "message": "This is a test message."}'
