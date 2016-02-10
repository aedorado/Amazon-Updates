# import argparse

# class StartTracking(argparse.Action):
# 	def __call__(self, parser, namespace, values, option_string=None):
# 	    print('%r %r %r' % (namespace, values, option_string))
# 	    setattr(namespace, self.dest, values)

# parser = argparse.ArgumentParser()
# parser.add_argument('--foo', action=StartTracking)
# parser.add_argument('bar', action=StartTracking)
# args = parser.parse_args('--foo 2'.split())
# print args

from all_imports import *

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--purl', type=str, help='Add said id to database')
parser.add_argument('-w', '--wurl', type=str,
                    help='Add all items from wishlist to database.')

args = parser.parse_args()

if not ((args.purl == None) ^ (args.wurl == None)):
    print 'Please input only product url or wishlist url.'
elif args.purl:
    args.purl = args.purl[:args.purl.rfind('/')]
    args.purl = args.purl[args.purl.rfind('/') + 1:]
    # print args.purl
    product = Product(args.purl)
    product.startTracking()
elif args.wurl:
    wl = Wishlist(args.wurl)
    wl.trackAllinWL()
