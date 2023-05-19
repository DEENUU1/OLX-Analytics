import os
import smtplib
from dotenv import load_dotenv
from typing import Any
from email.message import EmailMessage

load_dotenv()

def send_email(subject: str, message: Any, to: str):
    email = EmailMessage()
    email["Subject"] = subject
    email["From"] = os.getenv("EMAIL_USERNAME")
    email["To"] = to
    email.set_content(str(message))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(os.getenv("EMAIL_USERNAME"), os.getenv("EMAIL_PASSWORD"))
        server.send_message(email)
