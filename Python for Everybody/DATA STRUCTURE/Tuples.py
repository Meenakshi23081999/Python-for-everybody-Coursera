
fhandle = open('mbox-short.txt')


counts = dict()

for line in fhandle:
    words = line.split()

    
    if len(words) < 1:
        continue

    if words[0] == 'From:':
        continue

    if words[0] != 'From':
        continue

    word = words[5]

    word = word.split(':')
    num = word[0]

    counts[num] = counts.get(num, 0) + 1

counts = counts.items()

counts_sorted = sorted(counts)

for k, v in counts_sorted:
    print k, v
