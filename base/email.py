import os
import smtplib
from email.message import EmailMessage
from typing import Any

from dotenv import load_dotenv

load_dotenv()


def send_email(subject: str, message: Any, to: str):
    email = EmailMessage()
    email["Subject"] = subject
    email["From"] = os.getenv("EMAIL_USERNAME")
    email["To"] = to
    email.set_content(str(message))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        try:
            server.login(os.getenv("EMAIL_USERNAME"), os.getenv("EMAIL_PASSWORD"))
        except Exception as e:
            return f"Failed to login to email {e}"

        try:
            server.send_message(email)
        except Exception as e:
            return f"Failed to send email {e}"
