# Problem 21 - Sum of amicable numbers

from math import *


def getSumDivisors(x):  # function to get the sum of the numbers that divide evenly into x

    divisors = []

    for i in xrange(1,int(sqrt(x))):  # only test up to sqrt(x) to be efficient
        if x % i == 0:  # if x%i = 0, it evenly divides, so append i and its partner factor, x/i
            divisors.append(i)
            if x / i != x:  # this shouldn't be necessary (it would only happen if i is sqrt(x) ) but just incase i fucked something up lolz
                divisors.append(x/i)
        else:
            continue
    if sqrt(x) % 1 == 0:  # if sqrt(x) is an integer, i.e. if x is a square number (you would think using int(sqrt(x)) to test is faster but actually modulo is. The more you know!
        divisors.append(sqrt(x))

    # print divisors
    return sum(divisors)


def isAmicable(x):  # if the sum of divisors of x = a, and the sum of divisors of a = x, a and x are amicable
    a = getSumDivisors(x)
    # print a
    b = getSumDivisors(a)
    # print b

    if b == x:
        return True
    else:
        return False


def main():
    isAmicable(220)
    pass


if __name__ == '__main__':
    main()