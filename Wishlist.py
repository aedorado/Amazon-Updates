from all_imports import *


class Wishlist:

    productList = []

    def __init__(self, url):
        self.url = URL(url)

    def scrapeNumPages(self):
        html = self.url.fetch()
        soup = BeautifulSoup(html, 'html.parser')
        listbutton = soup.find('div', {'id': 'wishlistPagination'}).findAll(
            'li', {'class': re.compile('a-(.*)?')})
        self.numpages = len(listbutton)
        print str(self.numpages - 1) + ' page(s) found.'

    def buildProductList(self):
        for num in range(1, self.numpages):
            wpurl = URL(
                'https://www.amazon.com/gp/registry/wishlist/EKV4MG2FDII1/?page=' + str(num))
            html = wpurl.fetch()
            soup = BeautifulSoup(html, 'html.parser')
            prods = soup.findAll('a',  {'id': re.compile('itemName_')})

            for prod in prods:
                href = prod['href'][1:]
                print href
                self.productList.append(
                    href[(href.find('/') + 1):(href.rfind('?'))])
            print self.productList
        pass

    def trackAllProducts():
        pass

# wl =
# Wishlist('https://www.amazon.com/gp/registry/wishlist/EKV4MG2FDII1/ref=cm_wl_sortbar_v_page_2?ie=UTF8&page=2')
wl = Wishlist(
    'http://www.amazon.ca/gp/registry/wishlist/N7YMAZYY4KDN/ref=cm_wl_sortbar_v_page_2?ie=UTF8&page=2')
wl.scrapeNumPages()
wl.buildProductList()
