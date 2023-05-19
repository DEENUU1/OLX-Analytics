import os
import smtplib
from dotenv import load_dotenv

load_dotenv()

def send_email(subject: str, message: str, to: str):
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            email_body = f"Subject: {subject}\n\n{message}"
            server.login(os.getenv("EMAIL_USERNAME"), os.getenv("EMAIL_PASSWORD"))
            server.sendmail(os.getenv("EMAIL_USERNAME"), to, email_body)
    except Exception as e:
        return "Failed"