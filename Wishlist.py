from all_imports import *
import time


class UtilFetchProduct(Thread):

    def __init__(self, prod):
        Thread.__init__(self)
        self.prod = prod

    def run(self):
        self.prod.startTracking()
        pass


class UtilWLPageFetch(Thread):

    def __init__(self, url, tid):
        Thread.__init__(self)
        self.url = url
        self.tid = tid

    def run(self):
        productList = []
        print 'Thread ' + str(self.tid) + ' started.'
        html = self.url.fetch()
        soup = BeautifulSoup(html, 'html.parser')
        prods = soup.findAll('a', {'id': re.compile('itemName_')})
        for prod in prods:
            href = prod['href'][1:]
            pr = Product(href[(href.find('/') + 1):(href.rfind('?'))])
            if not pr.isTracked():
                print 'Untracked : ' + pr.pid
                productList.append(pr)
            else:
                print 'Already tracked : ' + pr.pid

        print 'Thread ' + str(self.tid) + ' has finished building product list.'
        print 'Thread ' + str(self.tid) + ' has found ' + str(len(productList)) + ' products.'

        for prod in productList:
            UtilFetchProduct(prod).start()
            pass

        print 'Thread ' + str(self.tid) + ' has tracked required products.'
        print 'Thread ' + str(self.tid) + ' finished.'


class Wishlist:

    # Wishlist Class Content

    def __init__(self, url):
        self.url = URL(url)
        self.numpages = self.scrapeNumPages()

    def scrapeNumPages(self):
        html = self.url.fetch()
        soup = BeautifulSoup(html, 'html.parser')
        if not soup.find('div', {'id': 'wishlistPagination'}):
            print '1 Page found.'
            return 2
        listbutton = soup.find('div', {'id': 'wishlistPagination'}).findAll(
            'li', {'class': re.compile('a-(.*)?')})
        print str(len(listbutton) - 1) + ' page(s) found.'
        return len(listbutton)

    def trackAllinWL(self):
        for tid in range(1, self.numpages):
            wpurl = URL(self.url.url + '?page=' + str(tid))
            UtilWLPageFetch(wpurl, tid).start()

# wl = Wishlist('http://www.amazon.ca/gp/registry/wishlist/N7YMAZYY4KDN/ref=cm_wl_sortbar_v_page_2?ie=UTF8&page=2')
# wl = Wishlist('https://www.amazon.com/gp/registry/wishlist/EKV4MG2FDII1/ref=cm_wl_sortbar_v_page_2?ie=UTF8&page=2')
# wl.trackAllinWL()
