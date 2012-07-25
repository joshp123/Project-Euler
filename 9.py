# problem 9 - pythagorean triplets

import math


def main():
    a = 1
    b = 2

    for a in xrange(1, 500):
        for b in xrange(2, 500):
            c = math.sqrt(pow(b, 2) + pow(a, 2))
            if a + b + c == 1000:
                print "a = " + repr(a) + "b = " + repr(b) + "c = " + repr(c)
                print a * b * c


if __name__ == '__main__':
    main()
