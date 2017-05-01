from google.transit import gtfs_realtime_pb2
import urllib
import time
import csv


print "Ready to Read Stream..."

feed = gtfs_realtime_pb2.FeedMessage()
response = urllib.urlopen('https://data.edmonton.ca/download/7qed-k2fc/application%2Foctet-stream')
feed.ParseFromString(response.read())
for entity in feed.entity:
  print "lat: {lat}\tlon: {lon}\tbearing:{bearing}".format(lat=entity.vehicle.position.latitude,lon=0,bearing=0)
