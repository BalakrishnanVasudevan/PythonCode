from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime

contenturl = "http://www.sbmtd.gov/maps-and-schedules/schedules/w/t12252_0.htm"
contenturl2 = "http://www.sbmtd.gov/maps-and-schedules/schedules/w/t12252_1.htm"
contenturl3 = "http://www.sbmtd.gov/maps-and-schedules/schedules/w/t12272_0.htm"
contenturl4 = "http://www.sbmtd.gov/maps-and-schedules/schedules/w/t12272_1.htm"
soup = BeautifulSoup(urlopen(contenturl).read(),'html5lib')
soup2 = BeautifulSoup(urlopen(contenturl2).read(),'html5lib')
soup3 = BeautifulSoup(urlopen(contenturl3).read(),'html5lib')
soup4 = BeautifulSoup(urlopen(contenturl4).read(),'html5lib')
soup.unicode
soup2.unicode
soup3.unicode
soup4.unicode
table = soup.find('div', attrs={'id': 'container'})
table2 = soup2.find('div', attrs={'id': 'container'})
table3 = soup3.find('div', attrs={'id': 'container'})
table4 = soup4.find('div', attrs={'id': 'container'})
rows = table.findAll('tr')
rows2 = table2.findAll('tr')
rows3 = table3.findAll('tr')
rows4 = table4.findAll('tr')
print ("\nMTD-11 Schedules \nTowards Storke and Hollister \n")
dnow = datetime.now()
for tr in rows:
 cols = tr.findAll('td')
 if len(cols) == 9:
  time = cols[7].find(text=True)
  print (time)
  # pic = time.split(':')
  # new = int(pic[0])
  # tim = dnow.hour
  # if (new>tim):
   # print ('pic: ',pic,'new: ',new,'tim: ',tim)
   # print (time)
print ("\nTowards Downtown \n")  
for tr2 in rows2:
 cols2 = tr2.findAll('td')
 if len(cols2) == 9:
  time2 = cols2[1].find(text=True)
  print (time2)
print ("\nMTD-24x Schedules \nTowards Storke and Hollister\n(Scheduled arrival at UCSB)\n")
for tr3 in rows3:
 cols3 = tr3.findAll('td')
 if len(cols3) == 8:
  time = cols3[1].find(text=True)
  print (time)
print ("\nTowards Downtown SB\n(Scheduled arrival at UCSB)\n")
for tr4 in rows4:
 cols4 = tr4.findAll('td')
 if len(cols4) == 4:
  time = cols4[2].find(text=True)
  print (time)