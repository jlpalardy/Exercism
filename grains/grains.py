def square(number):
	if number < 1 or number > 64:
		raise ValueError('Square number needs to be between 1 and 64 inclusive.')
	else:
		return 2 ** (number - 1)

def total():
	sum_list = [square(number) for number in range(1,65)]
	return sum(sum_list)


