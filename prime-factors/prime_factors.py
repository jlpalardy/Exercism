'''This solution relies on a method, primesieve, that uses the Sieve of Erastosthenes to find primes less than value. Unfortunately, the solution breaks when the value is too large.'''

def factors(value):
	if value < 2:
		return []
	primesList = primesieve(value)
	factorList = []
	for prime in primesList:
		while value > 1 and value % prime == 0:
			value = value / prime
			factorList.append(prime)		
	return factorList

def primesieve(upper_limit):
	primes = list(range(2,upper_limit + 1))
	for number in range(2,upper_limit + 1):
		multiplier = 2
		while number * multiplier <= primes[-1]:
			if number * multiplier in primes:
				primes.remove(number * multiplier)
			multiplier += 1
	return primes
		
		
