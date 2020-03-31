import string

def is_isogram(input_string):
	letter_list = [char.lower() for char in input_string if char in string.ascii_letters]
	letter_list.sort()
	letter_set = set(letter_list)
	letter_set_list = list(letter_set)
	letter_set_list.sort()
	return letter_list == letter_set_list


