# Project Euler problem 20

# Find the sum of the digits in the number 100!

# (For example, the sum of the digits in 10! is 27; 10! = 3628800)

import math

def list_digits(x):
	 digits = []
	 y = str(x)
	 l = len(y)
	 # makes a list of all the digits in x
	 for i in y:
	 	r = int(i)
	 	digits.append(r)
	 result = sum(digits)
	 print result

def solve(z):
	x = math.factorial(z)
	list_digits(x)
	return
