from all_imports import *


class Product:

    def __init__(self, pid):
        self.pid = pid
        pass

    def giveNameToSelf(self):
        self.pname = getProductNameFromId(pid)

    def getProductNameFromId(self):
        url = URL('http://www.amazon.ca/gp/product/' + self.pid + '/')
        html = url.fetch()
        preg_name = re.compile(
            '<span id="productTitle" class="a-size-large">(.*)?<\/span>')
        pname = preg_name.findall(html)
        pname = pname[0]
        re.sub(r"<.*?>", "", pname)
        self.pname = pname

    def isTracked(self):
    	db = DB()
        db.cursor.execute(
            "SELECT COUNT(*) FROM tracking WHERE id = ?", [self.pid])
        return (db.cursor.fetchone()[0] == 1)

    def startTracking(self):
    	db = DB()
    	if self.isTracked():
    		print 'Tracked already : ' + self.pid
    	elif not self.isTracked():
	        print 'Untracked Product : ' + self.pid
	        print 'Fetching Details.'
	        self.getProductNameFromId()
	        print 'Product Name : ' + self.pname
	        print 'Starting to track.'
	        db.insert_tracking_table(pid=self.pid, name=self.pname)
	        print 'Product added successfully.'
