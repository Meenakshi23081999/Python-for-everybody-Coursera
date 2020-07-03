fname = raw_input('Enter file name: ')
fhandle = open(fname)
count = 0

for line in fhandle:
    line = line.rstrip()
    word = line.split()

    
    if len(word) < 1:
        continue

    if word[0] != 'From':
        continue
    else:
        count += 1

    print word[1]

print "There were", count, "lines in the file with From as the first word"