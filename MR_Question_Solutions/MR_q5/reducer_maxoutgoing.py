import sys

flights = {}

for line in sys.stdin:
    line = line.strip()
    org, count = line.split("\t")
    count = int(count)
    if org in flights.keys():
        flights[org] += count
    else:
        flights[org] = count

max_count = 0
max_flight = ""

for f in flights.keys():
    if flights[f] > max_count:
        max_flight = f
        max_count = flights[f]

print("{}\t{}".format(max_flight, max_count))
