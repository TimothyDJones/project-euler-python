# Project Euler Problem #2
# Even Fibonacci numbers
# Problem 2
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.


def problem2(max):
	s = 0
	x = [1, 1]
	while x[1] < 4000000 and x[1] < max:
		next = sum(x)
		if not (next % 2):
			s += next

		x = [x[1], next]
	return s

if __name__ == "__main__":
	print(problem2(1000))
	print(problem2(10000))
	print(problem2(100000))
	print(problem2(1000000))
	print(problem2(10000000))
