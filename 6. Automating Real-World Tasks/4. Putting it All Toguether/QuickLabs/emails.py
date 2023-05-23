#!/usr/bin/env python3

import os
import smtplib
from email.message import EmailMessage

def generate_email(sender, receiver, subject, body, attachment_path):
    message = EmailMessage()
    message["From"] = sender
    message["To"] = receiver
    message["Subject"] = subject
    message.set_content(body)

    with open(attachment_path, "rb") as attachment:
        attachment_data = attachment.read()

    message.add_attachment(attachment_data, maintype="application", subtype="pdf", filename=os.path.basename(attachment_path))

    return message

def send_email(message):
    with smtplib.SMTP('localhost') as mail_server:
        mail_server.send_message(message)
