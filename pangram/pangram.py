def is_pangram(sentence):
	import string

	s = sentence.lower()
	unique = []
	
	for char in s:
		if ((char in string.ascii_lowercase) and (char not in unique)):
			unique.append(char)

	return len(unique) == 26
