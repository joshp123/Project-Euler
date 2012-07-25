# Project Euler problem 16

# Find the sum of the digits in the number 2^1000!

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
	x = 2**(z)
	list_digits(x)
	return
