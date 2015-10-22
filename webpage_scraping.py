from urllib.request import urlopen
from bs4 import BeautifulSoup

contenturl = "http://www.sbmtd.gov/maps-and-schedules/schedules/w/t12272_0.htm"
soup = BeautifulSoup(urlopen(contenturl).read(),'html.parser')
table = soup.find('div', attrs={'id': 'container'})
rows = table.findAll('tr')
print (soup('table')[4].findAll('tr')[1].a.string)
# for tr in rows:
 # cols = tr.findAll('td')
 # if 'oddcolumn' in cols[0]['class']:
  # # currency row
  # transit, Colgio, Santa, Rusty = [c.text for c in cols]
  # print (Colgio)
  
  
  
