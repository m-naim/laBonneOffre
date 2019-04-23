# send_email.py

from email.headerregistry import Address
from email.message import EmailMessage
import os
import smtplib

from dotenv import load_dotenv

load_dotenv()




def create_email_message(from_address, to_address, subject, body):
    msg = EmailMessage()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject
    msg.set_content(body)
    return msg

def send(body):
    # Gmail details
    email_address = os.environ.get("EMAIL_ADDRESSE")
    email_password = os.environ.get("PASSWORD") 

    # Recipent
    to_address = (
        Address(display_name='naim', username='pgamern19', domain='gmail.com'),
    )

    if __name__ == '__main__':
        msg = create_email_message(
            from_address=email_address,
            to_address=to_address,
            subject='Hello World',
            body= body
        )

        with smtplib.SMTP('smtp.gmail.com', port=587) as smtp_server:
            smtp_server.ehlo()
            smtp_server.starttls()
            smtp_server.login(email_address, email_password)
            smtp_server.send_message(msg)