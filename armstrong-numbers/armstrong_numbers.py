def is_armstrong_number(number):
	digitList = [int(i) for i in str(number)]
	numDigits = len(digitList)
	armstrongSum = 0

	for digit in digitList:
		armstrongSum += digit ** numDigits

	return True if armstrongSum == number else False
		
