def is_valid(isbn):
	isbnDigitsOnly = isbn.replace('-', '')
	#Check for proper length, whether X is in the proper position (if there at
	#all)
	if len(isbnDigitsOnly) != 10:
		return False
	if 'X' in isbnDigitsOnly and isbnDigitsOnly[9] != 'X':
		return False
	else:
		#Convert to int list form for use in the formula, convert X to 10
		isbnList = list(isbnDigitsOnly)
		if isbnList[9] == 'X':
			isbnList[9] = '10'
		#Check for any non-integer elements in our isbn
		for element in isbnList:
			if element not in '1234567890' and element != '10':
				return False 
		isbnListDigits = [int(x) for x in isbnList]
		
		#The formula has us multiplying the first number in the list by 10, 
		#the second by 9, etc and adding all these products. We then take the mod
		#of that with 11. Use a loop to do a running total of products, and return
		#truth value of total % 11 == 0.
		total = 0
		i = 10

		for number in isbnListDigits:
			total += number * i
			i -= 1

		return total % 11 == 0

