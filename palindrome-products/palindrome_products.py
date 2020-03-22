def largest(min_factor, max_factor):
	if min_factor > max_factor:
		raise ValueError('Min factor must be smaller than max factor!')
	palindromes = palindromeCheck(getProducts(min_factor, max_factor))
	if len(palindromes) < 1:
		print('There are no palindrome numbers in this range!')
		return (None, [])
	maxPalindrome = max(palindromes.values())
	factorsList = [key for key, val in palindromes.items() if val == maxPalindrome]
	print(f'The max palindrome is {maxPalindrome}, and its factors are {factorsList}')
	return (maxPalindrome, factorsList) 

def smallest(min_factor, max_factor):
	if min_factor > max_factor:
		raise ValueError('Min factor must be smaller than max factor!')
	palindromes = palindromeCheck(getProducts(min_factor, max_factor))
	if len(palindromes) < 1:
		print('There are no palindrome numbers in this range!')
		return (None, [])
	minPalindrome = min(palindromes.values())
	factorsList = [key for key, val in palindromes.items() if val == minPalindrome]
	print(f'The min palindrome is {minPalindrome}, and its factors are {factorsList}')
	return (minPalindrome, factorsList) 

def getProducts(min_factor, max_factor):
	productDict = {}
	for factor1 in range(min_factor, max_factor + 1):
		for factor2 in range(min_factor, max_factor + 1):
			if factor2 < factor1:
				continue
			productDict.update({(factor1, factor2): factor1 * factor2})
	#print(f'Products: {productDict}')
	return productDict
			
def palindromeCheck(dictionary):
	factorsList = [factorKey for factorKey in dictionary.keys()]
	productsList = [dictionary[factorKey] for factorKey in dictionary.keys()]
	palindromeDict = {}

	for i in range(len(productsList)):
		productStr = str(productsList[i])
		revProductStr = productStr[::-1]
		if productStr == revProductStr:
			palindromeDict.update({factorsList[i]:productsList[i]})
	return palindromeDict

		


