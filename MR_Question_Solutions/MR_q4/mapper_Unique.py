import sys
for line in sys.stdin:
    line = line.strip()
    line = line.split(",")
    if line[0] == "ID":
        continue
    org = line[17]
    dest = line[18]
    print("{}\t{}".format(org, dest))