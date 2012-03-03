# Quadratic.py
# Calculates roots from the quadratic equation
# ps this owns, fuck you c

from cmath import *

def sign(x):
	if(x >= 0):
		sign = '+'
	else:
		sign = '-'
	return sign


def quadratic(a,b,c):
	print "Computing roots of the quadratic equation ", a, ' x^2 ', sign(b), b, " x ", sign(c), c, " = 0"
	det = (b**2) - (4*a*c)
	root1 = (-b + sqrt(det))/(2*a)
	root2 = (-b - sqrt(det))/(2*a)
	root1 = round(root1.real,2) + 1j*round(root1.imag,2)
	root2 = round(root2.real,2) + 1j*round(root2.imag,2)
	if(det > 0):
		print 'There are 2 real roots of this equation, they are: \nx =', root1, '\nx =', root2
	elif(det == 0):
		print 'There is 1 distinct real root of this equation, it is: \nx =', root1
	else:
		print 'There are 2 distinct complex roots of this equation, they are: \nx =', root1, '\nx =', root2
	return
 
while True:
	try:
		a = float(raw_input("Enter the quadratic coefficient "))
		b = float(raw_input("Enter the linear coefficient "))
		c = float(raw_input("Enter the constant term "))
		break
	except ValueError:
		print 'This is not a valid number'
		
quadratic(a,b,c)
