import sys
import string

for line in sys.stdin:
    line = line.strip()
    line = line.translate(str.maketrans('', '', string.digits))
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.split(' ')
    for i in line:
        print('%s,1' %(i.lower()))

