import sys

word_dict = {}

for line in sys.stdin:
    line = line.strip()
    word, count= line.split('\t')
    count = int(count)

    if word in word_dict:
        continue    
    else:
        word_dict[word] = count

#Reducer
max_length = 0
max_word = ""
for word in word_dict.keys():
    if word_dict[word] > max_length:
        max_length =  word_dict[word]
        max_word = word   
print("{}\t{}".format(max_word, max_length))
