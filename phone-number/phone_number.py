import re

class PhoneNumber:

	def clean(self):
		numDigitsOnly = re.sub(r'\D', '', self.input)
		
		#Check for proper number of digits		
		if len(numDigitsOnly) > 11:
			raise ValueError('This phone number has too many digits!')
		if len(numDigitsOnly) < 10:
			raise ValueError('This phone number has too few digits!')
		
		#Check if country code is included and wrong
		if len(numDigitsOnly) == 11 and numDigitsOnly[0] != '1':
			raise ValueError('This phone number isn\'t valid!')

		#If country code is there and correct, we need to remove it 
		# and check if the rest of the number is correct
		if len(numDigitsOnly) == 11 and numDigitsOnly[0] == '1':
			numNoCountryCode = numDigitsOnly[1:]
			if int(numNoCountryCode[0]) < 2 or int(numNoCountryCode[3]) < 2:
				raise ValueError('This phone number isn\'t valid!')
			else:
				return numNoCountryCode

		#If number has the correct number of digits and no area code as-is:
		else:
			if int(numDigitsOnly[0]) < 2 or int(numDigitsOnly[3]) < 2:
				raise ValueError('This phone number isn\'t valid!')
			else:
				return numDigitsOnly

	def pretty(self):
		return f'({self.area_code}) {self.exchange_code}-{self.subscriber_number}'

	def __init__(self, number):
			self.input = number
			self.number = self.clean()
			self.area_code = self.number[0:3]
			self.exchange_code = self.number[3:6]
			self.subscriber_number = self.number[6:]


