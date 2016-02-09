from DB import *

db = DB()

tracking_create = 'CREATE TABLE tracking (\
			id CHAR(10) PRIMARY KEY NOT NULL, \
			productName VARCHAR(256) NOT NULL, \
			addedOn TIMESTAMP DEFAULT CURRENT_TIMESTAMP \
			)'

db.query(tracking_create)
db.insert_tracking_table(idd='1234A', name='Yovan')

price_create = ''