from all_imports import *

# DB class


class DB:

    def __init__(self):
        self.conn = db.connect('amzntrkr.db')
        self.cursor = self.conn.cursor()
        pass

    def all(self, table=''):
        q = 'SELECT * FROM ' + table
        self.cursor.execute(q)
        return self.cursor.fetchall()

    def query(self, q):
        self.cursor.execute(q)

    def insert_tracking_table(self, pid='', name=''):
        q = 'INSERT INTO tracking (id, productName) VALUES (?, ?)'
        self.cursor.execute(q, [pid, name])
        self.conn.commit()

    def insert_price_table(
            self, pid='', saleprice=0, dealprice=0, ourprice=0, bookprice=''):
        q = 'INSERT INTO price (productId, saleprice, dealprice, ourprice, bookprice) VALUES (?, ?, ?, ?, ?)'
        self.cursor.execute(
            q,
            [pid,
             saleprice,
             dealprice,
             ourprice,
             bookprice])
        self.conn.commit()

    def lastPriceEntries(self, n):
        q = 'SELECT * FROM price JOIN tracking ON price.productId=tracking.id ORDER BY price.addedOn DESC LIMIT ?'
        self.cursor.execute(q, [n])
        return self.cursor.fetchall()

    def delete(self, pid):
        q = 'DELETE FROM tracking WHERE id = ' + pid
        q = 'DELETE FROM price WHERE id = ' + pid
