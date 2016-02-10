from all_imports import *



class Wishlist:

    # nested Class
    class UtilThread(Thread):

        productList = []

        def __init__(self, url, tid):
            Thread.__init__(self)
            self.url = url
            self.tid = tid

        def run(self):
            print 'Thread ' + str(self.tid) + ' started.'
            html = self.url.fetch()
            soup = BeautifulSoup(html, 'html.parser')
            prods = soup.findAll('a',  {'id': re.compile('itemName_')})
            for prod in prods:
                href = prod['href'][1:]
                self.productList.append(Product(href[(href.find('/') + 1):(href.rfind('?'))]))
            
            print 'Thread ' + str(self.tid) + ' has finished building product list.'
            print 'Thread ' + str(self.tid) + ' has found ' + str(len(self.productList)) + ' products.'
            
            for prod in self.productList:
                prod.startTracking()

            print 'Thread ' + str(self.tid) + ' has tracked required products.'
            print 'Thread ' + str(self.tid) + ' finished.'
    
    # Wishlist Class Content

    productList = []

    def __init__(self, url):
        self.url = URL(url)
        self.numpages = self.scrapeNumPages()

    def scrapeNumPages(self):
        # html = self.url.fetch()
        # soup = BeautifulSoup(html, 'html.parser')
        # listbutton = soup.find('div', {'id': 'wishlistPagination'}).findAll(
        #     'li', {'class': re.compile('a-(.*)?')})
        # print str(len(listbutton) - 1) + ' page(s) found.'
        # return len(listbutton)
        return 3

    def runProductListBuilder(self):
        for tid in range(1, self.numpages):
            wpurl = URL(
                'https://www.amazon.com/gp/registry/wishlist/EKV4MG2FDII1/?page=' + str(tid))
            self.UtilThread(wpurl, tid).start()
            # html = wpurl.fetch()
            # soup = BeautifulSoup(html, 'html.parser')
            # prods = soup.findAll('a',  {'id': re.compile('itemName_')})

            # for prod in prods:
            #     href = prod['href'][1:]
            #     print href
            #     self.productList.append(
            #         href[(href.find('/') + 1):(href.rfind('?'))])
            # print self.productList

# wl =
# Wishlist('https://www.amazon.com/gp/registry/wishlist/EKV4MG2FDII1/ref=cm_wl_sortbar_v_page_2?ie=UTF8&page=2')
wl = Wishlist(
    'http://www.amazon.ca/gp/registry/wishlist/N7YMAZYY4KDN/ref=cm_wl_sortbar_v_page_2?ie=UTF8&page=2')
wl.runProductListBuilder()


