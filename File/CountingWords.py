counts = dict()
print('Enter a line of text: ')
line = input()

words = line.split()        #we get a list of words

print('Words: ',words)

print('Counting...')
for word in words:
    counts[word] = counts.get(word,0) + 1
print('Counts',counts)