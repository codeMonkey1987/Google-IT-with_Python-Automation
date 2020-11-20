#!/usr/bin/env python3

import os
import psutil
import shutil
import socket
import emails



# if usage is over 80%
def cpu_check():
    cpu_usage = psutil.cpu_percent(1)
    if cpu_usage > 80:
        return True

# if available disk space is lower than 20%
def disk_check():
    disk_usage = shutil.disk_usage("/")
    disk_total = disk_usage.total
    disk_used = disk_usage.used
    percentage = disk_used / disk_total * 100
    if percentage > 20:
        return True

# if available memory is less than 500MB
def memory_check():
    available = psutil.virtual_memory().available
    convert_to_mb = available / 1024 ** 2
    if convert_to_mb < 500:
        return True

# if hostname "localhost" cannot be resolved to "127.0.0.1"
def hostname_check():
    address = socket.gethostbyname('localhost')
    if not address is "127.0.0.1":
        return True


def alert_email(error):
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ["USER"])
    subject = error
    body = "Please check your system and resolve the issue as soon as possible."
    message = emails.generate_email(sender, receiver, subject, body)
    emails.send_email(message)

if cpu_check():
    subject = "Error - CPU usage is over 80%"
    alert_email(subject)

if disk_check():
    subject = "Error - Available disk space is less than 20%"
    alert_email(subject)

if memory_check():
    subject = "Error - Available memory is less than 500MB"
    alert_email(subject)

if hostname_check():
    subject = "Error - localhost cannot be resolved to 127.0.0.1"
    alert_email(subject)
