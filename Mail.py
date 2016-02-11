import smtplib

class Mail:

	username = ''
	password = ''

	def __init__(self):
		pass

	def setRec(self, to):
		self.to = to

	def setSub(self, sub):
		self.sub = sub

	def send(self):
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.ehlo()
		server.starttls()
		server.ehlo()
		server.login("@gmail.com", "")
		msg = "This is awesome baby!"
		server.sendmail("@gmail.com", "a@a", msg)
		server.quit()
		pass

# server.login("YOUR EMAIL ADDRESS", "YOUR PASSWORD")
# server.sendmail("YOUR EMAIL ADDRESS", "THE EMAIL ADDRESS TO SEND TO", msg)