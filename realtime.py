from google.transit import gtfs_realtime_pb2
import urllib
import time
import csv

stop_times_file = open('stop_times.txt')
stop_times= csv.reader(stop_times_file)
stop_times_list = list(stop_times)
trips = list(csv.reader(open('trips.txt')))
routes = list(csv.reader(open('routes.txt')))
print "Ready to Read Stream..."

feed = gtfs_realtime_pb2.FeedMessage()
response = urllib.urlopen('https://data.edmonton.ca/download/uzpc-8bnm/application%2Foctet-stream')
feed.ParseFromString(response.read())
for entity in feed.entity:
  if entity.HasField('trip_update') and entity.trip_update.trip.route_id=="9":
    trip_id=entity.trip_update.trip.trip_id
    print "Entity ID: {ident}\tRoute ID: {route_id}\tTrip ID: {trip_id}".format(ident=entity.id,route_id=entity.trip_update.trip.route_id,trip_id=entity.trip_update.trip.trip_id)
    for x in trips:
      if x[2].startswith(trip_id):
        for y in routes:
          if y[0] == x[0]:
            print y[2]
    for update in entity.trip_update.stop_time_update:
      if update.HasField('departure'):
        time_type = "Departure Time"
        time_value = update.departure.time
      if update.HasField('arrival'):
        time_type = "Arrival Time:"
        time_value = update.arrival.time
      print "Stop ID: {stop_id}\t{time_type} \t{depart_time}".format(stop_id=update.stop_id,time_type=time_type,depart_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(int(time_value))))
