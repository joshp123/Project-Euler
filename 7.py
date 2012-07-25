# problem 7: 10001st prime.py


def main():
    n = 10001
    # n = 10001  # calculate the first n primes
    prime_count = 1
    # sieve
    primes = []
    primes.append(2)
    for x in xrange(3, 1000000000, 2):  # go in steps of 2 to save effort, 100000000 is just a big number, idk how to figure out how to estimate the upper bound of n primes based on n
        factors = 0
        for y in xrange(0, len(primes) - 1):  # see if x is divisible by any primes so far, if not, y is prime
            if x % primes[y] == 0:
                factors += 1
                break  # if there are factors, don't bother calculating any more
        if factors == 0:
            primes.append(x)
            prime_count += 1
            # print "Prime # " + repr(prime_count) + " = " + repr(primes[-1])
            # print primes
            if prime_count == n:  # was going to use a while loop but it broke, welp
                print primes[-1]
                break

if __name__ == '__main__':
    main()
