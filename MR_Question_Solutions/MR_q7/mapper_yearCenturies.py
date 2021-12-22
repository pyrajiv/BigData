import sys
for line in sys.stdin:
    line = line.strip()
    line = line.split(",")
    if line[0] == "Country":
        continue
    country = line[0]
    if country != "India":
        continue
    year = line[3][-4:]
    runs = line[2]
    print("{}\t{}".format(year, runs))   