

import re
pile = open('regex_sum_41647.txt')
gold = pile.read()
copier = re.findall("[0-9]+", gold)
dice = [int(i) for i in copier]
sum = 0
for k in dice:
	sum += k
print(sum)
