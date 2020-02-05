def reverse(text):
	textArray = list(text)
	reverseArray = []

	i = len(textArray) - 1
	while i >= 0 :
		reverseArray.append(textArray[i])
		i -= 1

	return ''.join(reverseArray)

