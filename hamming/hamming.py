def distance(strand_a, strand_b):
	if len(strand_a) != len(strand_b):
		raise ValueError('DNA strands must be the same length!')
	else:
		hamming_distance = 0
		for index in range(len(strand_a)):
			if strand_a[index] != strand_b[index]:
				hamming_distance += 1
		return hamming_distance
