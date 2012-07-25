# problem 10: sum of al primes below 2 million


def main():
    prime_count = 1
    # sieve
    primes = []
    primes.append(2)
    for x in xrange(3, 2000000, 2):  # go in steps of 2 to save effort
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
    print sum(primes)

if __name__ == '__main__':
    main()
