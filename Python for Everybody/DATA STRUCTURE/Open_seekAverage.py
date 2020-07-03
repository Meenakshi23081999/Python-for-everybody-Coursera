fname = raw_input('Enter file name: ')
fhandle = open(fname)

x = 'X-DSPAM-Confidence:'
y = len(x)
count = 0
total = 0


for line in fhandle:
    if line.startswith('X-DSPAM-Confidence:'):
        line_number = line[19:]
        line_float = float(line_number)

        count += 1

        total += line_float
        

print 'Number of numbers:', count

print 'Sum of numbers:', total

print 'Average of numbers:', total / count

