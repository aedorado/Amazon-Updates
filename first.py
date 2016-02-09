from all_imports import *

url = 'http://www.amazon.in/gp/product/'
# pid = 'B00KDRQ2RU'
# pid = 'B011RG8SOU'
# pid = 'B00K1Y2CDS'
pid = 'B00MFQYSPA'
# pid = 'B00P90XSPK'

response = urllib2.urlopen(url + pid + '/')
html = response.read()

print 'Fetched..'

preg_name = re.compile('<span id="productTitle" class="a-size-large">(.*)?<\/span>')
pname = preg_name.findall(html)
pname = pname[0]
re.sub(r"<.*?>", "", pname)

preg_price = re.compile('<span id="priceblock_(.*)?<\/span>')
priceSpans = preg_price.findall(html)

priceDict = {
	'saleprice': 0,
	'dealprice': 0,
	'ourprice': 0
}

for span in priceSpans:
	priceType = span[:span.find('"')]
	price = span[span.rfind('>') + 1:].replace(',', '').strip()
	priceDict[priceType] = float(price)

print priceDict['saleprice']
print priceDict['dealprice']
print priceDict['ourprice']

db = DB()
db.insert_tracking_table(pid=pid, name=pname)
db.insert_price_table(pid=pid, saleprice=priceDict['saleprice'], dealprice=priceDict['dealprice'], ourprice=priceDict['ourprice'])