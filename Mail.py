import smtplib
from Config import *

class Mail:

	def __init__(self):
		pass

	def setRec(self, to):
		self.to = to

	def setSub(self, sub):
		self.sub = sub

	def setMsg(self, msg):
		self.msg = msg

	def send(self):
		print self.msg
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.ehlo()
		server.starttls()
		server.ehlo()
		server.login(Config.mailuser, Config.mailpass)
		server.sendmail(Config.mailuser, Config.mailto, self.msg)
		server.quit()
		pass

# m = Mail()
# m.setMsg('hello how are you?')
# m.send()