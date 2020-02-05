def to_rna(dna_strand = ''):
	rna_strand = ''
	for nucleotide in dna_strand:
		if nucleotide == 'G':
			rna_strand = rna_strand + 'C'
		elif nucleotide == 'C':
			rna_strand = rna_strand + 'G'
		elif nucleotide == 'T':
			rna_strand = rna_strand + 'A'
		elif nucleotide == 'A':
			rna_strand = rna_strand + 'U'
		else:
			raise Exception('That\'s not a DNA strand!')
	return rna_strand

		
