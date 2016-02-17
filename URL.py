import urllib2
import time


class URL:

    def __init__(self, url):
        self.url = url

    def fetch(self):
        print 'Attempting url fetch.'
        OK = False
        tries = 0
        while not OK:
            try:
                response = urllib2.urlopen(self.url)
                print 'Success : ' + self.url
                OK = True
            except urllib2.HTTPError as e:
                tries = tries + 1
                if tries >= 256:
                    return -1
                print 'Failure.\nAn HTTP error occured : ' + str(e.code)
                print 'Refetching : ' + self.url
            time.sleep(4)
        html = response.read()
        return html
