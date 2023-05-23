#!/usr/bin/env python3

import os
from datetime import date
import reports
import emails

desc_path = os.path.expanduser('~') + '/supplier-data/descriptions/'

def process_data(data):
    report = []
    for item in data:
        report.append("name: {}<br/>weight: {}".format(item[0], item[1]))
    return "<br/><br/>".join(report)

text_data = []
for text_file in os.listdir(desc_path):
    with open(os.path.join(desc_path, text_file), 'r') as f:
        text_data.append([line.strip() for line in f.readlines()])

if __name__ == "__main__":
    summary = process_data(text_data)
    title = "Processed Update on {}".format(date.today().strftime("%B %d, %Y"))
    attachment = "/tmp/processed.pdf"
    reports.generate_report(attachment, title, summary)

    username = "student-01-762b3df1d2aa"
    sender = "automation@example.com"
    receiver = "{}@example.com".format(username)
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    message = emails.generate_email(sender, receiver, subject, body, attachment)
    emails.send_email(message)
