# problem 22 - names dot txt scores

import string


def scoreName(name):
    # score a name based on A = 1, B = 2 etc
    name = name[1:-1]  # strip ""
    score = sum([string.lowercase.index(x) + 1 for x in name.lower()])
    return score


def main():
    # names = []
    with open('names.txt', 'rbU') as f:
        namelist = f.read()
        names = string.split(namelist, ",")

    names.sort()

    score = 0
    print len(names)
    for i in xrange(0, len(names)):
        score = score + (scoreName(names[i]) * (i + 1))

    print score

    return


if __name__ == '__main__':
    main()
