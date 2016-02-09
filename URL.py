import urllib2

class URL:

	def __init__(self, url):
		self.url = url

	def fetch(self):
		print 'Attempting url fetch.'
		response = urllib2.urlopen(self.url)
		print 'Success.'
		html = response.read()
		return html