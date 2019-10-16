from email.mime.text import MIMEText
import smtplib

my_message = MIMEText('Hello, this is the message body','plain','utf-8')

from_addr = input('From: ')
password = input('Please type your password: ')
to_addr = input('To: ')
smtp_server = input('SMTP SERVER: ')

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], my_message.as_string())
