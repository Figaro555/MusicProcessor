import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from project.Configs.EmailConfig import *
from project.Reporters.ReportSenders.AbstractSender import AbstractSender


class MailSender(AbstractSender):
    def __init__(self):
        self.server = smtplib.SMTP(server_name, port)
        self.server.ehlo()
        self.server.starttls()
        self.server.login(user, password)

    def send(self, file_data, file_name, subject):
        message = MIMEMultipart()
        message["From"] = sender
        message["To"] = recipient
        message["Subject"] = subject

        attachment = MIMEText(file_data)
        attachment.add_header('Content-Disposition', 'attachment',
                              filename=file_name)
        message.attach(attachment)

        self.server.send_message(message)

        print("[INFO] Email report was sent")


