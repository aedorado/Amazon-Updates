from all_imports import *


class Product:

    def __init__(self, pid):
        self.pid = pid
        pass

    def giveNameToSelf(self):
        self.pname = getProductNameFromId(pid)

    def getProductNameFromId(self):
        url = URL('http://www.amazon.in/gp/product/' + self.pid + '/')
        html = url.fetch()

        if html == -1:
            sys.exit('~\n~\n~\n~\nUNABLE TO FETCH URL')

        preg_name = re.compile(
            '<span id="productTitle" class="a-size-large">(.*)?<\/span>')
        pname = preg_name.findall(html)
        pname = pname[0]
        re.sub(r"<.*?>", "", pname)
        self.pname = pname

    def updatePrice(self):
        url = URL('http://www.amazon.in/gp/product/' + self.pid)
        html = url.fetch()

        preg_price = re.compile('<span id="priceblock_(.*)?<\/span>')
        priceSpans = preg_price.findall(html)

        priceDict = {
            'saleprice': 0,
            'dealprice': 0,
            'ourprice': 0,
            'bookprice': 0}

        ebook = True
        for span in priceSpans:
            priceType = span[:span.find('"')]
            price = span[span.rfind('>') + 1:].replace(',', '').strip()
            priceDict[priceType] = float(price)
            ebook = False

        # special case for ebooks when all the above price are 0
        bookprice = ''
        if ebook:
            rebooks = 'currencyINR">&nbsp;&nbsp;<\/span>[ ]+[\d,]+\.[\d]+<\/span>'
            preg_name = re.compile(rebooks)
            pricespans = preg_name.findall(html)
            bookprice = []
            for span in pricespans:
                bookprice.append(re.findall('\d+', span)[0])
            priceDict['bookprice'] = ','.join(bookprice)

        print self.pid, priceDict

        db = DB()
        db.insert_price_table(
            pid=self.pid,
            saleprice=priceDict['saleprice'],
            dealprice=priceDict['dealprice'],
            ourprice=priceDict['ourprice'],
            bookprice=priceDict['bookprice'])

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
            print 'Product added successfully.\n'
