import sys

years = {}

for line in sys.stdin:
    line = line.strip()
    year, runs = line.split("\t")
    runs = int(runs)
    if year in years.keys():
        if runs>=100:
            years[year] += 1
    else:
        if runs>=100:
            years[year] = 1

year_max = ""
year_maxCenturies = 0
for year in years.keys():
    if years[year] > year_maxCenturies:
        year_max = year
        year_maxCenturies = years[year]
print("{}".format(year_max))