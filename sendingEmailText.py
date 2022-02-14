#!/usr/bin/python

import base64
import smtplib

filename = "myTextEmail.txt"

# Read a file and encode it into base64 format
fo = open(filename, "rb")
filecontent = fo.read()
encodedcontent = base64.b64encode(filecontent)  # base64

sender = "senderEmail@mail.com"
reciever = "receiver@mail.com"

marker = "ZULKPERETES"

body = """
This is a test email to send an attachement.
"""
# Define the main headers.
part1 = """From: From Person <me@fromdomain.net>
To: To Person <zulkepretes@gmail.com>
Subject: Sending Attachement
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary=%s
--%s
""" % (
    marker,
    marker,
)

# Define the message action
part2 = """Content-Type: text/plain
Content-Transfer-Encoding:8bit

%s
--%s
""" % (
    body,
    marker,
)

# Define the attachment section
part3 = """Content-Type: multipart/mixed; name=\"%s\"
Content-Transfer-Encoding:base64
Content-Disposition: attachment; filename=%s

%s
--%s--
""" % (
    filename,
    filename,
    encodedcontent,
    marker,
)
message = part1 + part2 + part3

try:
    smtpObj = smtplib.SMTP("localhost")
    smtpObj.sendmail(sender, reciever, message)
    print("Successfully sent email")
except Exception:
    print("Error: unable to send email")
