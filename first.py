from all_imports import *

url = 'http://www.amazon.in/gp/product/'
pid = 'B00KDRQ2RU'
# pid = 'B011RG8SOU'
# pid = 'B00K1Y2CDS'

response = urllib2.urlopen(url + pid + '/')
html = response.read()

print 'Fetched..'

preg_name = re.compile('<span id="priceblock_(.*)?<\/span>')
priceSpans = preg_name.findall(html)

for span in priceSpans:
	price_type = span[:span.find('"')]
	price = span[span.rfind('>') + 1:].replace(',', '').strip()
	print price
	print price_type
