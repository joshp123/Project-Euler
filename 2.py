# Project Euler problem 2
fibb = set()
def fib(n):
	n1 = 0
	n2 = 1
	n3 = n1 + n2
	print(n3)
	while n3 < n:
		if n3 % 2 == 0:
			fibb.add(n3)
		n1 = n2
		n2 = n3
		n3 = n1 + n2
		print(n3)
	print(fibb)

def soln():
	fib(4000000)
	result = sum(fibb)
	print result

soln()

	
