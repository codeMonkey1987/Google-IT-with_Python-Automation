#!/usr/bin/env python3

import os
import datetime
import reports
import emails

date_time = datetime.datetime.now().strftime('%Y-%m-%d')

def create_pdf(path):
    pdf = ""
    for file in os.listdir(path):
        if file.endswith(".txt"):
            with open(path + file, 'r') as new_file:
                item_list = new_file.readlines()
                name = item_list[0]
                weight = item_list[1]
                pdf += "name: " + name + "<br/>" + "weight: " + weight + "<br/><br/>"
    return pdf


if __name__ == "__main__":
    path = "supplier-data/descriptions/"
    title = "Process Updated on " + date_time
    pdf = create_pdf(path)
    reports.generate_report("/tmp/processed.pdf", title, pdf)


    sender= "automation@example.com"
    receiver = "{}@example.com".format(os.environ["USER"])
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    attch = "/tmp/processed.pdf"
    message = emails.generate_email(sender, receiver, subject, body, attch)
    emails.send_email(message)