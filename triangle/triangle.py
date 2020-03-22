from itertools import permutations

def isTriangle(sides):
	if len(sides) != 3:
		raise ValueError('Triangles must have 3 sides!')
	for sidesOrder in permutations(sides,3):
		if sidesOrder[0] + sidesOrder[1] < sidesOrder[2]:
			return False	
	
def equilateral(sides):
	if isTriangle(sides) == False:
		return False
	if set(sides) == {0}:
		return False
	return len(set(sides)) == 1

def isosceles(sides):
	if isTriangle(sides) == False:
		return False
	return len(set(sides)) < 3

def scalene(sides):
	if isTriangle(sides) == False:
		return False 
	return len(set(sides)) == 3	

def degenerate(sides):
	if isTriangle(sides) == False:
		return False
	for sidesOrder in permutations(sides,3):
		if sidesOrder[0] + sidesOrder[1] == sidesOrder[2]:
			return True
	return False	


