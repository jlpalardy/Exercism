from itertools import combinations

def triplets_with_sum(number):
	triplets_sum_list = []
	triplets_list = triplets_in_range(1, number - 2)
	for triplet in triplets_list:
		if triplet[0] + triplet[1] + triplet[2] == number:
			triplets_sum_list.append(triplet)
	print(triplets_sum_list)
	return triplets_sum_list


def triplets_in_range(start, end):
	triplets = []
	for a in range(start, end - 1):
		for b in range(a + 1, end):
			for c in range(b + 1, end + 1):
				if is_triplet([a,b,c]) == True:
					triplets.append([a,b,c])
	return triplets 
				

def is_triplet(triplet):
	return triplet[0]**2 + triplet[1]**2 == triplet[2]**2 
	
#triplets_with_sum(12)
#triplets_with_sum(30)
#triplets_with_sum(462)
#triplets_with_sum(5)
#triplets_with_sum(30000)
