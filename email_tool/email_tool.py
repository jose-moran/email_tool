import smtplib
import traceback

from environs import Env

from email_tool.email_msg import email_msg, get_time
from email_tool.email_sender import MailSender


def send_email(msg: str, header: str, recipient: str) -> None:
    env = Env()
    env.read_env()

    smtp_server = env("SMTP_SERVER")
    port = env.int("SMTP_PORT")
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


class EmailMonitor:
    """
    Context manager to monitor code execution and send an email, with the option to send an email in case of an error.
    """

    def __init__(self, msg: str, header: str, recipient: str, timezone: str = "Europe/Paris"):
        self.recipient = recipient
        self.header = header
        self.msg = msg
        self.msg_timezone = timezone

    def __enter__(self):
        return self  # Return context manager object if needed

    def __exit__(self, exc_type, exc_value, tb):
        if exc_type is not None:
            # Prepare the message
            time = get_time(self.msg_timezone)
            error_message = "".join(traceback.format_exception(exc_type, exc_value, tb))
            msg = f"An error occurred: \n\n{error_message} \n\n Script execution stopped at {time}."

            # Send email (assuming send_email is a function you've defined)
            send_email(msg=msg, header=self.header, recipient=self.recipient)

            # Return False to propagate the exception, True to suppress it
            return False  # Change to True if you do not want to propagate the exception
        else:
            exec_time = get_time(self.msg_timezone)
            self.msg += f"\n\nScript execution completed at {exec_time}."
            send_email(msg=self.msg, header=self.header, recipient=self.recipient)
            return True
