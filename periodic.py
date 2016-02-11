from all_imports import *

class UtilPeriodicPrice(Thread):

    def __init__(self, prod):
        Thread.__init__(self)
        self.prod = prod

    def run(self):
    	print 'Running Thread for product :' + self.prod.pid
    	self.prod.updatePrice()
    	print 'Completed Thread for product :' + self.prod.pid

def buildpidList():
	db = DB()
	db.cursor.execute('SELECT id FROM TRACKING')
	pidlist = db.cursor.fetchall()
	return pidlist

def buildDetailsList():
	db = DB()
	for pid in pidlist:
		t = UtilPeriodicPrice(Product(pid[0]))
		t.start()
	t.join()
	time.sleep(2)


def mailLastEntries(n):
	db = DB()
	updates = db.lastPriceEntries(n)
	print updates


pidlist = buildpidList()
buildDetailsList()
mailLastEntries(len(pidlist))