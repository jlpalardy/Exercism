def square_of_sum(number):
	#Using the Gaussian sum for the sum of the first n natural 		numbers
	return (number*(number + 1)/2)**2

def sum_of_squares(number):
	#Formula taken from here: https://trans4mind.com/	personal_development/mathematics/series/sumNaturalSquares.htm
	return round(number**3/3 + number**2/2 + number/6,0)

def difference_of_squares(number):
	return square_of_sum(number) - sum_of_squares(number)
