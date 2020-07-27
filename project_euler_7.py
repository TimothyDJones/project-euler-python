# Project Euler Problem #7
# 10001st prime
# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
import math

def is_prime(n):
	if n <= 1:
		return False
	if n <= 3 or n == 5:
		return True
	if not (n % 2):
		return False
	for i in range(3, int(math.sqrt(n)) + 1, 2):
		if not (n % i):
			return False

	return True

def problem7(n):
	count = 0
	for i in range(1, 10000000):
		# print(i, is_prime(i))
		if is_prime(i):
			count += 1
			if count == n:
				return i

if __name__ == "__main__":
	print(problem7(6))
	print(problem7(10))
#	print(problem7(20))
#	print(problem7(100))
#	print(problem7(1000))
	print(problem7(10001))
