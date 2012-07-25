#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

result = 2520
running = 1
factors = range(11, 21)
import math


def is_divisible2(r):
    running = 1
    while r < math.factorial(max(factors)) and running == 1:
        #print 'b'
        is_a_factor = []
        not_a_factor = []
        for x in factors:
            #print 'c'
            if r % x == 0:
                is_a_factor.append(x)
            else:
                not_a_factor.append(x)
        if len(is_a_factor) == len(factors):
            print r
            print 'omg!'
            running = 0
            break
        else:
            r += 2520
            #print r
            #print
            continue

is_divisible2(result)
