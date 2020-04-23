def recite(start_verse, end_verse):
	ordinalList = ['first', 'second', 'third', 'fourth', 'fifth',
'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']
	verseList = ['and a Partridge in a Pear Tree', 'two Turtle Doves,',
'three French Hens,', 'four Calling Birds,', 'five Golden Rings,',
'six Geese-a-Laying,', 'seven Swans-a-Swimming,', 'eight Maids-a-Milking,', 'nine Ladies Dancing,', 'ten Lords-a-Leaping,', 'eleven Pipers Piping,', 'twelve Drummers Drumming,']


	for verse in range(end_verse): 
		printString = 'On the ' + ordinalList[verse] + ' day of Christmas my true love gave to me:\n'

		if verse == 0:
			print(printString + 'a Partridge in a Pear Tree.')

		else:
			for verseNumber in reversed(range(0, verse + 1)):
				if verseNumber == 0:
					printString += verseList[verseNumber] + '.' + '\n'
				else:
					printString += verseList[verseNumber] + '\n'

		print(printString)

recite(3,7)

