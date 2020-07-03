fhandle = open('romeo.txt')
words = []

for line in fhandle:
    line = line.rstrip().split()
    for word in line:
        if word not in words:
            words.append(word)

print sorted(words)

