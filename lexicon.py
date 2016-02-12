import string

data_filename = "texts/all.txt"
output_filename = "lexicon.txt"
lexicon_counts_ouput = "lex_counts.txt"
with open(data_filename, 'r') as f:
    data = f.read()

data = data.lower()
exclude = set(string.punctuation)
data = ''.join(ch for ch in data if ch not in exclude)

word_array = data.split(" ")

word_map = {}
for word in word_array:
    if word not in word_map:
        word_map[word] = 1
    else:
        word_map[word] += 1

print "Unique words: %d" % len(word_map)

dictlist = []
for key, value in word_map.iteritems():
    temp = [key,value]
    dictlist.append(temp)

dictlist.sort(key=lambda x: x[1])
dictlist.reverse()

counts = {}
one_words = 0
two_words = 0
with open(output_filename, 'wb+') as output:
    for entry in dictlist:
        try:
            counts[str(entry[1])] += 1
        except:
            counts[str(entry[1])] = 1
        output.write(entry[0] + ": " + str(entry[1]) + "\n")

countslist = []
for key in counts:
    countslist.append((int(key), counts[key]))
countslist.sort(key=lambda x: x[0])
countslist
with open(lexicon_counts_ouput, "w") as output:
    output.write("# (number of time word appears): (number of words in this category), (percentage of total words)%\n")
    for entry in countslist:
        cur_str = "%s words: %d,  %f%%" % (entry[0], entry[1], (entry[1] / float(len(word_map)) * 100))
        print cur_str
        output.write(cur_str + "\n")
