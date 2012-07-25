# john's code is better than mine

import string


def getNameScore(name):
    return sum([(string.lowercase.index(x) + 1) for x in name.lower()])

names = map(lambda x: x.replace('"', '').lower(), open('names.txt').readlines()[0].split(","))
names.sort()
score = 0

for position, name in enumerate(names):
    namescore = getNameScore(name)
    score += ((position + 1) * namescore)

print score
