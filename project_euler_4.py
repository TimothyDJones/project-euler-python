# Project Euler Problem #4
# Largest palindrome product
#  Problem 4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# Strategy: Count down from largest possible number
#			  and check to see if it's a palindrome.

def problem4(digits):
	x = 0
	print((10**digits - 1)**2)
	for i in range((10**digits - 1), 0, -1):
		for j in range((10**digits - 1), 0, -1):
			a = str(i * j)
			if a == a[::-1] and (i * j) > x:
				x = (i * j)

	return x

if __name__ == "__main__":
	print(problem4(2))			
	print(problem4(3))
	print(problem4(4))

