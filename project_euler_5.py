# Project Euler Problem #5
# Smallest multiple
# Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Strategy: Find the LCM of each number 1 to n.
#			 At each step, use the LCM from the previous step.

def lcm(x, y):
	if x > y:
		greater = x
	else:
		greater = y

	while True:
		if not (greater % x) and not (greater % y):
			return greater
		greater += 1

def problem5(n):
	p = 1
	for i in range(1, (n+1)):
		p = lcm(i, p)

	return p

if __name__ == "__main__":
	print(problem5(10))
	print(problem5(20))

