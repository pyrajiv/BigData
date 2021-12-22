import sys
for line in sys.stdin:
    line = line.strip()
    line = line.split(",")
    if line[0] == "Country":
        continue
    player = line[1]
    runs = line[2]
    print("{}\t{}".format(player, runs))   