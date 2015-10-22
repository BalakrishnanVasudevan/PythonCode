from urllib.request import urlopen
from bs4 import BeautifulSoup

contenturl = "http://www.bank.gov.ua/control/en/curmetal/detail/currency?period=daily"
soup = BeautifulSoup(urlopen(contenturl).read(),'html.parser')
table = soup.find('div', attrs={'class': 'content'})
rows = table.findAll('tr')
for tr in rows:
 cols = tr.findAll('td')
 if 'cell_c' in cols[0]['class']:
  # currency row
  digital_code, letter_code, units, name, rate = [c.text for c in cols]
  print (digital_code, letter_code, units, name, rate)