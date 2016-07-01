from geoip import geolite2
match = geolite2.lookup('216.58.192.228')
#print match.timezone, match.country, match.continent
print match.to_dict()
