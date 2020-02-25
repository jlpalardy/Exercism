from __future__ import division
import math

class Rational:
	def __init__(self, numer, denom):
		self.numer = numer
		self.denom = denom

	def __eq__(self, other):
		#Takes into account non-reduced fractions and different
		#ways of expressing negative and positive fractions	
		reducedSelf = reduce(self.numer, self.denom)
		reducedOther = reduce(other.numer, other.denom)
		selfNeg = isNeg(self.numer, self.denom)
		otherNeg = isNeg(other.numer, other.denom)
		return abs(reducedSelf.numer) == abs(reducedOther.numer) and abs(reducedSelf.denom) == abs(reducedOther.denom) and selfNeg == otherNeg

	def __repr__(self):
		return '{}/{}'.format(self.numer, self.denom)

	def __add__(self, other):
		sumNumer = self.numer * other.denom + other.numer * self.denom
		sumDenom = self.denom * other.denom
		return reduce(sumNumer, sumDenom)

	def __sub__(self, other):
		subNumer = self.numer * other.denom - other.numer * self.denom
		subDenom = self.denom * other.denom
		return reduce(subNumer, subDenom)

	def __mul__(self, other):
		mulNumer = self.numer * other.numer
		mulDenom = self.denom * other.denom
		return reduce(mulNumer, mulDenom)

	def __truediv__(self, other):
		divNumer = self.numer * other.denom
		divDenom = self.denom * other.numer
		return reduce(divNumer, divDenom)

	def __abs__(self):
		absNumer = abs(self.numer)
		absDenom = abs(self.denom)
		return reduce(absNumer, absDenom)

	def __pow__(self, power):
		if abs(power) == power:
			powNum = self.numer ** power
			powDenom = self.denom ** power
		else:
			powNum = self.denom ** abs(power)
			powDenom = self.numer ** abs(power)
		return reduce(powNum, powDenom)

	def __rpow__(self, base):
		#Does not work for bases of type Rational!
		return (base ** self.numer) ** (1 / self.denom) 

def reduce(numer, denom):
	gcd = int(math.gcd(numer, denom))
	return Rational(int(numer/gcd), int(denom/gcd))

def isNeg(numer, denom):
	if (numer > 0 and denom > 0) or (numer < 0 and denom < 0):
		return False
	else:
		return True




