import smtplib
import ssl
import imghdr
from email.message import EmailMessage

email_sender = 'kiranmaruthi.developer@gmail.com'
email_password = 'rlslbastjxcaoqvt'

email_recever = 'kunakiranmaruthi@gmail.com'

subject = "Warning..! With Photo 1"
body = "Hello Kiran."

with open('images/WebPass.jpg', 'rb') as img:
    file_data = img.read()
    file_type = imghdr.what(img.name)
    file_name = img.name



em = EmailMessage()
em['From'] = email_sender
em['To'] = email_recever
em['subject'] = subject
em.set_content(body)

em.add_attachment(file_data,maintype='image', subtype=file_type, filename=file_name)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_recever, em.as_string())

