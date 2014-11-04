# project Euler problem 3

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?
import math 

def isFactor(num1, num2):
    if num1 % num2 == 0:
        return True
    else:
        return False

def isPrimeFactor(num, primes):
    retval = True
    for p in primes:
        if isFactor (num, p):
            return False
    return retval

start_number = 600851475143

primes = []
initial = 3

while (initial < math.sqrt(start_number)):
    if isFactor(start_number, initial):
        if isPrimeFactor(initial, primes):
            primes.append(initial)
            print initial
    initial += 2 # skip even numbers, 3 -> 5 etc

print "last prime should be final val printed above"



