import sys
for line in sys.stdin:
    line = line.strip()
    line = line.split(",")
    if line[0] == "ID":
        continue
    year = line[1]
    if year != "2004":
        continue
    org = line[17]
    print("{}\t1".format(org))