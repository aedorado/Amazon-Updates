import sqlite3 as db
import hashlib
import uuid
# import bcrypt
# salt = bcrypt.gensalt()
# print salt

conn = db.connect('egrocery.db')
cursor = conn.cursor()

cont = raw_input('Insert values? y/n\n>> ')

while cont == 'y' or cont == 'Y':

    table = raw_input(
        '--------\nCHOOSE TABLE\nfeedback\norder\nproduct\nretailer\nuser\nwholeseller\n>> ')

    if table == 'u':
        inputdata = raw_input(
            'Enter SPACE SEPERATED values for\nemail password type region username\n')
        inputdata = inputdata.split(' ')
        salt = uuid.uuid4().hex
        print salt
        # sql = "INSERT INTO user (user_id, email, password, salt, type, region, username) VALUES (NULL, ?, ?, ?, ?, ?, ?)", (inputdata[0], inputdata[1], salt, inputdata[2], inputdata[3], inputdata[4])
        # cursor.execute("INSERT INTO user (user_id, email, password, salt,
        # type, region, username) VALUES (NULL, %s, %s, %s, %s, %s, %s)",
        # (inputdata[0], inputdata[1], salt, inputdata[2], inputdata[3],
        # inputdata[4]))
        cursor.execute("INSERT INTO user (user_id, email, password, salt, type, region, username) VALUES (NULL, ?, ?, ?, ?, ?, ?)", (
            inputdata[0], inputdata[1], salt, inputdata[2], inputdata[3], inputdata[4]))
        # print sql
        conn.commit()

    elif table == 'f':
        inputdata = raw_input(
            'Enter SPACE SEPERATED values for\nuser_id type\n')
        inputdata = inputdata.split(' ')
        description = raw_input('Enter description:\n')
        cursor.execute("INSERT INTO feedback (user_id, type, description) VALUES (?, ?, ?)", (
            inputdata[0], inputdata[1], description))
        conn.commit()

    elif table == 'p':
        inputdata = raw_input(
            'Enter SPACE SEPERATED values for\nname government_price\n')
        inputdata = inputdata.split(' ')
        description = raw_input('Enter description:\n')
        cursor.execute("INSERT INTO product (product_id, name, description, government_price) VALUES (NULL, ?, ?, ?)", (
            inputdata[0], description, inputdata[1]))
        conn.commit()

    elif table == 'o':
        inputdata = raw_input(
            'Enter SPACE SEPERATED order for\nuser_id user_id_product_id cost quantity\n')
        inputdata = inputdata.split(' ')
        cursor.execute("INSERT INTO orders (user_id, user_id_product_id, cost, quantity) VALUES (?, ?, ?, ?)", (
            inputdata[0], inputdata[1], inputdata[2], inputdata[3]))
        conn.commit()

    elif table == 'r':
        inputdata = raw_input(
            'Enter SPACE SEPERATED values for\nuser_id_product_id sp quantity\n')
        inputdata = inputdata.split(' ')
        cursor.execute("INSERT INTO retailer (user_id_product_id, sellingprice, quantity) VALUES (?, ?, ?)", (
            inputdata[0], inputdata[1], inputdata[2]))
        conn.commit()

    elif table == 'w':
        inputdata = raw_input(
            'Enter SPACE SEPERATED values for\nuser_id_product_id cp sp quantity\n')
        inputdata = inputdata.split(' ')
        cursor.execute("INSERT INTO wholeseller (user_id_product_id, costprice, sellingprice, quantity) VALUES (?, ?, ?, ?)", (
            inputdata[0], inputdata[1], inputdata[2], inputdata[3]))
        conn.commit()

    cont = raw_input(
        'VALUES INSERTED IN TABLE\n\n***** Insert values? y/n\n>> ')


# hashed_password = hashlib.sha512(password + salt).hexdigest()
