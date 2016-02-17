import smtplib
from Config import *

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Mail:

    msg = MIMEMultipart('alternative')
    msg['From'] = Config.mailuser
    msg['To'] = Config.mailto

    def __init__(self):
        pass

    def setRec(self, to):
        self.to = to

    def setSub(self, sub):
        self.msg['Subject'] = sub

    def setMsg(self, html):
        html = MIMEText(html, 'html')
        self.msg.attach(html)

    def send(self):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(Config.mailuser, Config.mailpass)
        server.sendmail(Config.mailuser, Config.mailto, self.msg.as_string())
        server.quit()
        pass

# m = Mail()
# m.setMsg('hello how are you?')
# m.send()
