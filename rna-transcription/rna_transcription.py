def to_rna(dna_strand = ''):
	rna_strand = ''
	nucleo_dict = { 'G':'C', 'C':'G', 'T':'A', 'A':'U'}
	
	for nucleotide in dna_strand:
		if nucleotide not in nucleo_dict:
			raise ValueError('Not a nucleotide!')
		rna_strand += dna_to_rna[nucleotide]

	return rna_strand
