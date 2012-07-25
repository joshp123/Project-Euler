# Project Euler problem 3 - Prime factors
#
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
primes = []
numbers = []
factors = []
multiples = []
def largest_factor(x):
	print 'starting largest factor'
	prime_factors(x)
	l = int(len(factors)) - 1
	print '# of prime factors: '
	print l
	largest = factors[l]
	print 'Larges prime factor is: '
	print largest
	return largest

def prime_factors(x):
	print 'starting prime factors'
	factors = []
	print 'Do any primes exist yet? (Hopefully not!)'
	print primes
	prime_sieve(x) # calculate primes up to x
	print 'K, primes done, now dividing all primes by:'
	print x
	print 'and incase you forgot what the primes were, they are:'
	print primes
	for q in primes:
		print 'NIGGER DEATH'
		if q % x == 0:
			factors.append(q) # if divides perfectly into x, it is a prime factor of x
	
	print 'The calculated prime factors are: '
	print factors
	return factors

def prime_sieve(x):
	# returns all primes up to but not including sqrt(x)
	print 'starting sieve routine'
	primes = []
	numbers = [2]

	for i in xrange(3, int(x**0.5) + 1, 2):		# adds all numbers from 2 to n to numbers
		numbers.append(i)
	
	while True:
		if len(numbers) == 0:
			break
		
		prime = numbers[0] # prime = first number 
		primes.append(prime) #adds prime to list
		multiples = [] # new set of multiples that we remove from numbers

		for n in numbers:
			if n % prime == 0:  
				multiples.append(n) # if n/prime has no remainder, it is a multiple
			
		for n in multiples:
			numbers.remove(n) # remove multiples from numbers
	print 'Done with primes, they are:'
	print primes
	return primes

while True:
     try:
         x = int(raw_input("What number would you like to calculate the prime factors of? "))
         break
     except ValueError:
         print "This is not a valid number"
    
largest_factor(x)
#prime_factors(x)
#prime_sieve(x)
#prime_factors(x)
#largest_factor(x)

		

	
