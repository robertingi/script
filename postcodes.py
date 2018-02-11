import csv
import urllib.request, json
import pprint
from math import cos, asin, sqrt
postnumer = ['101','102','103','104','105','107','108','109','110','111','112','113','116','170','190']
postalcode = 0
csvfile = open('cleantest.csv')
csvcreate = open('output.csv', 'a')
reader = csv.reader(csvfile)
writer = csv.writer(csvcreate, lineterminator='\n')
alls = []
next(reader)
file = open("IS.txt", encoding="utf8")
postcodes = {}
for row in file:
    lis = list(filter(None,row.split("\t")))
    p = str(lis[1])
    if(p in postnumer):
        postcodes[(lis[3],lis[4])] = p
count = 0
writer.writerow(['room_id','survey_id','host_id','room_type','city','reviews',
                 'overall_satisfaction','accommodates','bedrooms',
                 'price','minstay','latitude','longitude','last_modified',
                 'location','postcode'])

def distance(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295
    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p)*cos(lat2*p) * (1-cos((lon2-lon1)*p)) / 2
    return 12742 * asin(sqrt(a))

def closest(data, v):
    return min(data, key=lambda p: distance(float(v[0]),float(v[1]),float(p[0]),float(p[1])))

for row in reader:
    count = count + 1
    lat = row[11]
    lang = row[12]
    postal_code = -1
    tup = (lat, lang)
    nearest = 0
    postal_code = closest(postcodes,tup)
    row.append(postcodes[postal_code])
    writer.writerow(row)
csvcreate.close()
print("done")
