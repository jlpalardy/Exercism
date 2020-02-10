def classify(number):
	if number <= 0 or isinstance(number, int) == False:
		raise ValueError('Number must be a natural number!') 
	elif aliquotSum(number) > number:
		return 'abundant'
	elif aliquotSum(number) == number:
		return 'perfect'
	elif aliquotSum(number) < number:
		return 'deficient'

def aliquotSum(number):
	factorList = [possibleFactor for possibleFactor in range(1,number) 
if number % possibleFactor == 0]
	return sum(factorList)



