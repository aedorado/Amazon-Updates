from DB import *

db = DB()

tracking_create = 'CREATE TABLE tracking (\
			id CHAR(10) PRIMARY KEY NOT NULL, \
			productName VARCHAR(256) NOT NULL, \
			addedOn TIMESTAMP DEFAULT CURRENT_TIMESTAMP \
			)'


price_create = 'CREATE TABLE price (\
			productId CHAR(10) NOT NULL, \
			saleprice DECIMAL(9, 2), \
			dealprice DECIMAL(9, 2), \
			ourprice  DECIMAL(9, 2), \
			addedOn TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL, \
			PRIMARY KEY(productId, addedOn) \
			)'

# db.query(tracking_create)
# db.query(price_create)
# db.insert_tracking_table(idd='1234A67890', name='Yovan')
