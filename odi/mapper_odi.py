import sys
for line in sys.stdin:
    line = line.strip()
    line = line.split(",")
    if line[0] == "Country":
        continue
    country = line[0]
    date = line[3]
    runs = line[2]
    #dest = line[18]
    if country == "NA" or runs == "NA" or date == 'NA':
        continue
    year = date.split('-')[-1]
    #key = max(src,dest)+min(src,dest)
    #key = year+src
    print("{},{},{}".format(country,year,runs))