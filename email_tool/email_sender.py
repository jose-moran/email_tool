import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class MailSender:
    def __init__(self, smtp_server: str, port: int, email: str, password: str):
        self.smtp_server = smtp_server
        self.port = port
        self.email = email
        self.password = password

        # Create a secure SSL context
        self.server = smtplib.SMTP(smtp_server, port)
        self.server.starttls()  # Secure the connection

    def login(self):
        self.server.login(self.email, self.password)

    def quit(self):
        self.server.quit()

    def send_email(self, to_email: str, subject: str, body: str):
        msg = MIMEMultipart()

        msg["From"] = self.email
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        self.server.sendmail(self.email, to_email, msg.as_string())
