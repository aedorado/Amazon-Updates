from all_imports import *

class UtilPeriodicPrice(Thread):

    def __init__(self, pid):
        Thread.__init__(self)
        self.pid = pid

    def run(self):
    	print 'running'

    	url = URL('http://www.amazon.in/gp/product/' + self.pid)
    	html = url.fetch()

    	preg_price = re.compile('<span id="priceblock_(.*)?<\/span>')
    	priceSpans = preg_price.findall(html)

    	priceDict = {'saleprice': 0, 'dealprice': 0, 'ourprice': 0	}

    	for span in priceSpans:
    		priceType = span[:span.find('"')]
    		price = span[span.rfind('>') + 1:].replace(',', '').strip()
    		priceDict[priceType] = float(price)

    	print self.pid, priceDict

    	db = DB()
    	db.insert_price_table(pid=self.pid, saleprice=priceDict['saleprice'], dealprice=priceDict['dealprice'], ourprice=priceDict['ourprice'])


def buildpidList():
	db = DB()
	db.cursor.execute('SELECT id FROM TRACKING')
	pidlist = db.cursor.fetchall()
	return pidlist

detailslist = []
def buildDetailsList():
	db = DB()
	for pid in pidlist:
		UtilPeriodicPrice(pid[0]).start()

pidlist = buildpidList()
buildDetailsList()