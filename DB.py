from all_imports import *

# DB class
class DB:

	def __init__(self):
		self.conn = db.connect('amzntrkr.db')
		self.cursor = self.conn.cursor()
		pass

	def query(self, q):
		self.cursor.execute(q)

	def insert_tracking_table(self, idd='', name=''):
		print idd
		print name
		q = ''
		self.cursor.execute(q);

		pass
