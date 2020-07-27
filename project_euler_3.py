# Project Euler Problem #3
# Largest prime factor
# Show HTML problem content  
# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

# Strategy: Loop through numbers (div) to determine if it
#			  is a divisor. If so, reset the max value to 
#		      quotient after dividing and restart.  Otherwise,
#			  increment the divisor and check again.

def problem3(n, div=2):
	while div < n:
		if not (n % div) and n//div > 1:
			n = n//div
			div = 2
		else:
			div += 1

	return n

if __name__ == "__main__":
	print(problem3(13195))			# 29
	print(problem3(600851475143))	# 6857
	print(problem3(790851475143))	# 149697421

