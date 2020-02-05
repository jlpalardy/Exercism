def proteins(strand):
	codonList = [strand[i:i+3] for i in range(0, len(strand), 3)]
	proteinList = []
	codonDict = {
	'AUG':'Methionine',
	'UUU':'Phenylalanine',
	'UUC':'Phenylalanine',
	'UUA':'Leucine',
	'UUG':'Leucine',
	'UCU':'Serine',
	'UCC':'Serine',
	'UCA':'Serine',
	'UCG':'Serine',
	'UAU':'Tyrosine',
	'UAC':'Tyrosine',
	'UGU':'Cysteine',
	'UGC':'Cysteine',
	'UGG':'Tryptophan'
	}

	for codon in codonList:
		if codon == 'UAA' or codon == 'UAG' or codon == 'UGA':
			break
		else:
			proteinList.append(codonDict[codon])

	return proteinList
		

