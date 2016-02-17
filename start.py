from all_imports import *

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--purl', type=str, help='Add said id to database')
parser.add_argument(
    '-w',
     '--wurl',
     type=str,
     help='Add all items from wishlist to database.')
parser.add_argument(
    '-s',
     '--show',
     help='Show all entries in db.',
     action='store_true')

args = parser.parse_args()

if not ((args.purl is None) ^ (args.wurl is None)):
    print 'Please input only product url or wishlist url.'
elif args.purl:
    # args.purl = args.purl[:args.purl.rfind('/')]      # uncommet if entering url of product
    # args.purl = args.purl[args.purl.rfind('/') + 1:]  # as above
    product = Product(args.purl)
    product.startTracking()
elif args.wurl:
    # wl = Wishlist(args.wurl)  # uncomeent if entering url of wishlist
    wl = Wishlist('http://www.amazon.in/gp/registry/wishlist/' + args.wurl)
    wl.trackAllinWL()

if args.show:
    db = DB()
    alltr = db.all(table='tracking')
    if len(alltr) == 0:
        print 'No items added yet.'
    i = 0
    for entry in alltr:
        i = i + 1
        print str(i) + ') ' + entry[1] + '\n\thttp://www.amazon.in/gp/product/' + entry[0]
