def isPalindrome(string):
	if string == str(string[::-1]):
		return 1	# string reversed = string
	else:
		return 0 # not a palindrome

palindromes = []

for num1 in xrange(999,100,-1):
	for num2 in xrange(999,100,-1):
		product = num1 * num2
		if isPalindrome(product) == 1:
			palindromes.append(product)
		pass
	pass

print 'The largest palindrome from the product of 2 three digit numbers is: ' + repr(max(palindromes))