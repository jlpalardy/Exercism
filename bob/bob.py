def response(hey_bob):
	hey_bob = hey_bob.strip()
	if hey_bob == '':
		return 'Fine. Be that way!'
	elif hey_bob.isupper() and hey_bob[-1] == '?':
		return 'Calm down, I know what I\'m doing!'
	elif hey_bob.isupper() and hey_bob[-1] != '?':
		return 'Whoa, chill out!'
	elif hey_bob.isupper() == False and hey_bob[-1] == '?':
		return 'Sure.'
	else:
		return 'Whatever.'

