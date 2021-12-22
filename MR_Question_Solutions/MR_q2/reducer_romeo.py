import sys

word_dict = {}
word_count = 0

for line in sys.stdin:
    line = line.strip()
    word, count= line.split('\t')
    count = int(count)

    if word in word_dict:
        word_dict[word]+=count
        
    else:
        word_dict[word] = count

#Reducer
for word in word_dict.keys():
    print("{}\t{}".format(word, word_dict[word]))
