import re

# load list of positive words into a list
with open('positive.txt', 'r') as ifile:
    positive = ifile.read().splitlines()

# load list of negative words into a list
with open('negative.txt', 'r') as ifile:
    negative = ifile.read().splitlines()

# analyse the sentimentality of the text as a dictionary of word/score tuples

dictionary = {}

ifile = open('source.txt', 'r')

for line in ifile:
    words = re.sub("[^\w]", " ", line).split()
    for word in words:
        word = word.lower()
        if word in dictionary:
            if word in positive:
                dictionary[word] = dictionary[word] + 1
            if word in negative:
                dictionary[word] = dictionary[word] - 1
        else:
            if word in positive:
                dictionary[word] = 1
            elif word in negative:
                dictionary[word] = -1
            else:
                dictionary[word] = 0

ifile.close()

score = 0
for key, value in dictionary.items():
    score = score + value
    
# sort by weighted occurance
sorted_dictionary = sorted(dictionary.items(), key=lambda kv: kv[1])

# the ten most common positive words
for k, v in sorted_dictionary[:10]:
    print(k, v)

# the ten most common negative words
for k, v in sorted_dictionary[-10:]:
    print(k, v)

# the overall sentimentality
print('Overall score: ', score)

# the number of negative words
print('Negative words: ', sum(1 for k in dictionary if dictionary[k] < 0))

# the number of positive words
print('Positive words: ', sum(1 for k in dictionary if dictionary[k] > 0))

# the number of neutral words
print('Neutral words: ', sum(1 for k in dictionary if dictionary[k] == 0))
