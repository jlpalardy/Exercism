def slices(series, length):
	substringList = []
	if len(series) < 1:
		raise ValueError('Series has to be nonempty!')
	elif length <= 0:
		raise ValueError('Length has to be greater than 0!')
	elif length > len(series):
		raise ValueError('Choose a shorter length!')
	else:
		i = 0
		while i+length <= len(series):
			substringList.append(series[i:i+length])
			i += 1
	return substringList
