from all_imports import *

class Product:

	db = DB()

	def __init__(self, pid):
		self.pid = pid
		pass

	def giveNameToSelf(self):
		self.pname = getProductNameFromId(pid)

	def getProductNameFromId(self):
		url = URL('http://www.amazon.in/gp/product/' + self.pid + '/')
		html = url.fetch()
		preg_name = re.compile('<span id="productTitle" class="a-size-large">(.*)?<\/span>')
		pname = preg_name.findall(html)
		pname = pname[0]
		re.sub(r"<.*?>", "", pname)
		self.pname = pname

	def isTracked(self):
		self.db.cursor.execute("SELECT COUNT(*) FROM tracking WHERE id = ?", [self.pid])
		return (self.db.cursor.fetchone()[0] == 1)

	def startTracking(self):
		self.db.insert_tracking_table(pid=self.pid, name=self.pname)