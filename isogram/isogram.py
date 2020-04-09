import string

def is_isogram(input_string):
	letter_list = [char.lower() for char in input_string if char in string.ascii_letters]
	letter_set = set(letter_list)
	return len(letter_list) == len(letter_set)



