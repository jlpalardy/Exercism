def recite(start_verse, end_verse):
	ordinalList = ['first', 'second', 'third', 'fourth', 'fifth',
'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']
	verseList = ['and a Partridge in a Pear Tree.', 'two Turtle Doves, ',
'three French Hens, ', 'four Calling Birds, ', 'five Golden Rings, ',
'six Geese-a-Laying, ', 'seven Swans-a-Swimming, ', 'eight Maids-a-Milking, ', 'nine Ladies Dancing, ', 'ten Lords-a-Leaping, ', 'eleven Pipers Piping, ', 'twelve Drummers Drumming, ']

	printString = ''
	
	for verse in range(start_verse - 1, end_verse):
		printString += '\nOn the ' + ordinalList[verse] + ' day of Christmas my true love gave to me:\n'
		
		if verse == 0:
			printString += 'a Partridge in a Pear Tree.\n'

		else:
			for verseNumber in reversed(range(0, verse + 1)):
				printString += verseList[verseNumber] + '\n'

	return printString

