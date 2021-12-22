import sys
flight = {}
for line in sys.stdin:
    line = line.strip()
    country, year, runs = line.split(',')
    #year = int(year)
    runs = int(runs)
    cent = 0
    if runs >= 100:
        cent = 1
    key = country+year
    if key in flight:
        flight[key] += cent
    else:
        flight[key] = cent
        #flight[year].append(count)
        #flight[year].append(delay)
#for key in flight.keys():
    #average = float(flight[year][1])/float(flight[year][0])
    #print("{}\t{}".format(year, average))
keymax = max(flight, key=flight.get)
print('max: ',keymax,flight[keymax])
print('countyear:India1992:', flight['India1992'])
print('countyear:India2011:', flight['India2011'])
print('countyear:India1999:', flight['India1999'])
print('countyear:India1998:', flight['India1998'])