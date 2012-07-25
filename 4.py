# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

def list_multiples():
	multiples = []
	pallindromes = []
	r1 = range(111,1000)
	for i in r1:
		multiples.append(r1*i)
	for i in multiples:
		d = str(i)
		l = len(d)
		p1 = int(d[-i:-0])
		p2 = int(d[0:i])
		if p1 == p2:
			pallindromes.append(i)
	print max(pallindromes)

list_multiples()
