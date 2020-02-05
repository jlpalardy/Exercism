def leap_year(year):
	try:
		return (year%4 == 0 and year%100 != 0) or (year%400 == 0)
	except ValueError:
		raise Exception("That's not a number!")
	

