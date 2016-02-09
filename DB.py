from all_imports import *

# DB class
class DB:

	def __init__(self):
		self.conn = db.connect('amzntrkr.db')
		self.cursor = self.conn.cursor()
		pass

	def all(self, table):
		self.cursor.execute('SELECT * FROM ' + table)

	def query(self, q):
		self.cursor.execute(q)

	def insert_tracking_table(self, pid='', name=''):
		q = 'INSERT INTO tracking (id, productName) VALUES (?, ?)'
		self.cursor.execute(q, [pid, name])
		self.conn.commit()

	def insert_price_table(self, pid='', saleprice=0, dealprice=0, ourprice=0):
		q = 'INSERT INTO price (productId, saleprice, dealprice, ourprice) VALUES (?, ?, ?, ?)'
		self.cursor.execute(q, [pid, saleprice, dealprice, ourprice])
		self.conn.commit()

	def toggle_tracking(self, pid):
		pass

	def delete(self, pid):
		q = 'DELETE FROM tracking WHERE id = ' + pid
		q = 'DELETE FROM price WHERE id = ' + pid
