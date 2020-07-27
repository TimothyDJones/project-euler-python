# Project Euler Problem #1
# Multiples of 3 and 5
# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def problem1(max):
	sum = 0
	for i in range(max):
		if (not (i % 3) or not (i % 5)):
			sum += i

	return sum

if __name__ == "__main__":
	print(problem1(10))
	print(problem1(100))
	print(problem1(1000))
