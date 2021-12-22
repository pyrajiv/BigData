import sys

word_dict = {}
word_count = 0
for line in sys.stdin:
    line = line.strip()
    word, count = line.split(',')
    count = int(count)
    if word in word_dict:
        word_dict[word][0] += count
    else:
        word_dict[word] = []
        word_dict[word].append(count)

for word in word_dict.keys():
    print(word + "," + str(word_dict[word][0]))