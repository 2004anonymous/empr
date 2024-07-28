import smtplib
from email.mime.text import MIMEText

def sendVerifyMail(to_email, subject, body):
    # Email account credentials
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    from_email = 'rahulrgogoi4@gmail.com'
    from_password = 'hrvf vaoz obzy gaea '  # Use an app password if you have 2FA enabled

    # Create the email content
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    # Connect to the SMTP server and send the email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection
        server.login(from_email, from_password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.close()
        print('Email sent successfully!')
    except Exception as e:
        print(f'Failed to send email: {e}')

# Example usage
# to_email = 'xa1244661@gmail.com'
# subject = 'Hello anon !'
# body = 'You are one step away to access all the features of ChatingPoint and connect with your friends and family and your gropu. you can discus your doubts and solve other doubt. Please click here to complete your registration. https://test-aniflicks.onrender.com'
# sendVerifyMail(to_email, subject, body)