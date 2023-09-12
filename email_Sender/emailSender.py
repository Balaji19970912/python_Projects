from email.message import EmailMessage
from app_password import password

import ssl
import smtplib

email_Sender = 'balaji.s@qualesce.com'
email_Password = password

email_Receiver = 'balaji.s@qualesce.com'

subject = 'Send Mail From Python'
body = """
Checking complete code works for sending mail or not! If received Happy:)
"""

em = EmailMessage()
em['From'] = email_Sender
em['To'] = email_Receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.office365.com', 465, context=context) as SMTP:
    smtp.login(email_Sender, email_Password)
    smtp.sendmail(email_Sender, email_Receiver, em.as_string())