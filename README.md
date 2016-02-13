# Amazon-Updates

Never miss the lowest prices of your favorite products again.


- For help:

    `python start.py -h`

- For adding a single product:

    `python start.py -p [productid]`



- For adding all products from Wishlist:

    `python start.py -w [wishlistid]`
  
  
Then a crontab in Unix based OS. Type `crontab -e` in terminal.

In the file add the line : `* */2 * * * python path/to/periodic.py > /dev/null`
if you want updates every 2 hours.

Make changes in `Config.py` file and add your actual gmail username and password. Also add the mail address.

Enjoy lowest price alerts. :) 
