# problem 22 - names dot txt scores

import string


def scoreName(name):
    # score a name based on A = 1, B = 2 etc
    name = str(name.lower)  # this means we can get indeces easily
    letter_scores = []
    for x in xrange(0, len(name) - 1):
        letter_scores[x] = string.lowercase.index(name[x])

    for x in xrange(0, len(letter_scores) - 1):
        letter_scores = letter_scores[x] + 1

    score = sum(letter_scores)
    return score


def main():
    names = []
    with open('names.txt', 'rbU') as f:
        names = [line.strip() for line in f]

    names.sort()

    print names[1:10]

    for i in xrange(0, len(names) - 1):
        names[i] = scoreName(names[i]) * (i + 1)

    print 'The sum of all the name scores is:' + repr(int(sum(names)))

    return


if __name__ == '__main__':
    main()
