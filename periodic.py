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
    db.cursor.execute('SELECT id FROM tracking')
    pidlist = db.cursor.fetchall()
    return pidlist


def buildDetailsList():
    db = DB()
    for pid in pidlist:
        t = UtilPeriodicPrice(Product(pid[0]))
        t.start()
    t.join()
    time.sleep(4)


def mailLastEntries(n):
    db = DB()
    updates = db.lastPriceEntries(n)
    mail = Mail()
    mail.setSub('Amazon Updates')
    msg = ''
    for upd in updates:
        msg = msg + '<a href="http://www.amazon.in/gp/product/' + \
            upd[0] + '" traget="_blank">' + upd[7] + '</a><br>'
        msg = msg + \
            ('Rs. ' + str(upd[1]) + ', Rs. ' + str(
                upd[2]) + ', Rs. ' + str(upd[3])) + '<br>'
        msg = msg + ('Bookprice : ' + upd[4]) + '<br>'
        msg = msg + ('Updated @ ' + upd[5]) + '<br><br>'
    mail.setMsg(msg)
    mail.send()

pidlist = buildpidList()
buildDetailsList()
mailLastEntries(len(pidlist))
