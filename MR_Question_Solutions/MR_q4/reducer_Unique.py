import sys

flights = []
count = 0

for line in sys.stdin:
    line = line.strip()
    org, dest = line.split("\t")
    flight = []
    flight.append(org)
    flight.append(dest)
    flag = True
    for f in flights:
        if f[0] == flight[0] and f[1] == flight[1]:
            flag = False
    if flag:
        flights.append(flight)
        count+=1
print(count)