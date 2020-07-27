# Project Euler Problem #6
# Sum square difference 
# Problem 6
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def problem6(n):
	x, y = 0, 0
	for i in range(1, (n+1)):
		x += i**2
		y += i

	return (y**2 - x)

if __name__ == "__main__":
	print(problem6(10))
	print(problem6(20))
	print(problem6(100))

