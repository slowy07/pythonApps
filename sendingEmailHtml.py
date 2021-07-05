import smtplib

sender = "email@domain.com"
receiver = "email@domain.com"

message = f"""From: From Person {sender}
To: To Person {receiver}
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP HTML e-mail test

This is an e-mail message to be sent in HTML format

<b>zulkepretes make simplest ostest.</b>
<h1>zulkepretes still making simplest ostest.</h1>
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receiver, message)         
   print("Successfully sent email")
except smtplib.SMTPException:
   print("Error: unable to send email")