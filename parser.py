# import argparse

# class StartTracking(argparse.Action):
# 	def __call__(self, parser, namespace, values, option_string=None):
# 	    print('%r %r %r' % (namespace, values, option_string))
# 	    setattr(namespace, self.dest, values)

# parser = argparse.ArgumentParser()
# parser.add_argument('--foo', action=StartTracking)
# # parser.add_argument('bar', action=StartTracking)
# args = parser.parse_args('--foo 2'.split())
# print args

from all_imports import *

parser = argparse.ArgumentParser()
parser.add_argument("pid", type=str, help="Add said id to database")

args = parser.parse_args()

product = Product(args.pid)
if not product.isTracked():
	print 'Untracked Product.\nFetching Details.'
	product.getProductNameFromId()
	print 'Product Name : ' + product.pname
	print 'Starting to track.'
	product.startTracking()
	print 'Product added successfully.'
else:
	print 'Already Tracking.'
