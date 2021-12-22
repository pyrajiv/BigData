import sys
for line in sys.stdin:
    line = line.strip()
    line = line.split()
    for word in line:
        length = len(word)
        if length>14:
            continue
        print('{}\t{}'.format(word, length))
    