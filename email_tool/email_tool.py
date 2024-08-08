import smtplib

from environs import Env

from email_tool.email_msg import email_msg
from email_tool.email_sender import MailSender


def send_email(msg: str, header: str, recipient: str) -> None:
    env = Env()
    env.read_env()

    smtp_server = env("SMTP_SERVER")
    port = env.int("PORT")
    email = env("EMAIL")
    password = env("PASSWORD")

    server = smtplib.SMTP(smtp_server, port)
    server.starttls()

    try:
        mail_sender = MailSender(smtp_server, port, email, password)
        mail_sender.login()
        email_message = email_msg(msg)
        mail_sender.send_email(recipient, header, email_message)
    except smtplib.SMTPException as e:
        print(f"An error occurred: {e}")
    finally:
        server.quit()
