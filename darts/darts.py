import math

def score(x, y):
	#Formula for a circle of radius r: x**2 + y**2 = r**2
	#outer circle: radius = 10 u, radius**2 = 100 u**2, points = 1
	#middle circle: radius = 5 u, radius**2 = 25 u**2, points = 5
	#inner circle: radius = 1 u, radius**2 = 1 u**2,  points = 10

	testValue = x**2 + y**2

	if testValue <= 1:
		return 10

	elif testValue <= 25:
		return 5

	elif testValue <= 100:
		return 1

	else:
		return 0
    
