from all_imports import *

url = 'http://www.amazon.in/gp/product/'
# pid = 'B00KDRQ2RU'
pid = 'B011RG8SOU'
# pid = 'B00K1Y2CDS'
# pid = 'B00MFQYSPA'
# pid = '8120340078'
# pid  = '8173711461'

response = urllib2.urlopen(url + pid + '/')
html = response.read()
soup = BeautifulSoup(html)
# print html

# pricedivs = soup.findAll('div', {'class': 'top-level'})
# for div in pricedivs:
# 	# print div
# 	ancs = div.findAll('a', {'class': 'a-link-normal'})
# 	f = open('temp', 'w')
# 	for anc in ancs:
# 		f.write(anc.findAll('span')[0].get_text() + '\n')
	
# 	print '\n\n\n\n'


# print 'Fetched..'
# re2 = '<span class="currencyINR">.*?</span>.*[\d]</span>'
re1 = 'currencyINR">&nbsp;&nbsp;<\/span>[ ]+[\d,]+\.[\d]+<\/span>'
preg_name = re.compile(re1)
pname = preg_name.findall(html)
for name in pname:
	print name

# <a id="a-autoid-
#<a id="a-autoid(.*)<\/a>
# preg_price = re.compile('<span id="priceblock_(.*)?<\/span>')
# priceSpans = preg_price.findall(html)

# priceDict = {
#     'saleprice': 0,
#         'dealprice': 0,
#         'ourprice': 0
# }

# for span in priceSpans:
#     priceType = span[:span.find('"')]
#     price = span[span.rfind('>') + 1:].replace(',', '').strip()
#     priceDict[priceType] = float(price)

# print priceDict['saleprice']
# print priceDict['dealprice']
# print priceDict['ourprice']

# db = DB()
# print pid, pname
# db.insert_tracking_table(pid=pid, name=pname)
# db.insert_price_table(pid=pid, saleprice=priceDict[
                      # 'saleprice'], dealprice=priceDict['dealprice'], ourprice=priceDict['ourprice'])
