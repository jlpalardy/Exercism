def steps(number):
	if number < 1:
		raise ValueError('Number must be > 1!')
	if number == 1:
		return 0

	steps = 0
	while number != 1:
		if number % 2 == 0:
			number = number / 2
		else:
			number = 3*number + 1
		steps += 1
		if number == 1:
			return steps

