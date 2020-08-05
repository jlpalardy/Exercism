def recite(start_verse, end_verse):
	ordinalList = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth',
	'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']
	
	giftList = ['and a Partridge in a Pear Tree.', 'two Turtle Doves, ', 'three French Hens, ',
	'four Calling Birds, ', 'five Gold Rings, ', 'six Geese-a-Laying, ',
	'seven Swans-a-Swimming, ', 'eight Maids-a-Milking, ', 'nine Ladies Dancing, ',
	'ten Lords-a-Leaping, ', 'eleven Pipers Piping, ', 'twelve Drummers Drumming, ']
	
	finalList = []
	
	for verse in range(start_verse - 1, end_verse):
	
		printList = ['On the ', ' day of Christmas my true love gave to me: ']
		if verse == 0:
			printList.insert(1, ordinalList[verse])
			printList.append('a Partridge in a Pear Tree.')
			finalList.append(''.join(printList))

		else:	
			printList.insert(1,ordinalList[verse])
			for i in reversed(range(0, verse + 1)):
				printList.append(giftList[i])
			finalList.append(''.join(printList))

	return finalList
