import os		# to interact with os
import re 		# to use regular expressions
import sys
import sqlite3 as db  # for database
import argparse
from threading import Thread

from bs4 import BeautifulSoup
from DB import *
from URL import *
from Product import *
from Wishlist import *
from Mail import *

# sys.stdout = open('logs/log_file', 'w')
