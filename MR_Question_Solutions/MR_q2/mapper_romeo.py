import sys
for line in sys.stdin:
    line = line.strip()
    line = line.split(" ")
    for word in line:
        if word.lower() == "romeo":
            print ('{}\t1'.format(word.title()))
        
