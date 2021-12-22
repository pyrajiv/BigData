import sys
for line in sys.stdin:
    line = line.strip()
    line = line.split(",")
    if line[0] == "ID":
        continue
    year = line[1]
    src = line[17]
    dest = line[18]
    if src == "NA" or dest == "NA":
        continue

    #key = max(src,dest)+min(src,dest)
    key = year+src
    print("{},1".format(key))