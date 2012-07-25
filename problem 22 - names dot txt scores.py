# problem 22 - names dot txt scores

import string


def scoreName(name):
    # score a name based on A = 1, B = 2 etc
    score = sum([string.lowercase.index(x) + 1 for x in name.lower()])
    return score


def main():
    # names = []
    with open('names.txt', 'rbU') as f:
        names = [line.strip() for line in f]
    print names

    names.sort()

    print names[0]

    for i in xrange(0, len(names) - 1):
        names[i] = scoreName(names[i]) * (i + 1)

    print sum(names)

    return


if __name__ == '__main__':
    main()
