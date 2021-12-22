import sys
flight = {}
for line in sys.stdin:
    line = line.strip()
    key, count = line.split(',')
    count = int(count)
    if key in flight:
        flight[key] += count
    else:
        flight[key] = 1
        #flight[year].append(count)
        #flight[year].append(delay)
#for key in flight.keys():
    #average = float(flight[year][1])/float(flight[year][0])
    #print("{}\t{}".format(year, average))
keymax = max(flight, key=flight.get)
print('max: ',keymax,flight[keymax])
print('yearsrc:2004ORD:', flight['2004ORD'])
print('yearsrc:2004CLT:', flight['2004CLT'])
print('yearsrc:2004LAS:', flight['2004LAS'])