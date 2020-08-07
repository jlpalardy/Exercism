'''
This solution is heavily inspired by caddycarine's on Exercism's Python track.

The reason why this solution is quick is because it imposes as narrow a range as possible on a and b
in each triplet. 

Remember: a < b < c; a + b + c = x; a, b, and c are positive integers; and a + b <= c by triangle inequality.

Given this, we can derive from a < b that the max value of a is x//2 (again, needs to be an integer).
The min value of a is, of course, 1. 

The min value of b can be set in two places, depending on how large a is. The absolute minimum of b is a + 1, but if a is larger, you can narrow the interval we're searching for b in if you consider the minimum of b as x//2 - a. This is derived by setting c as its max (x//2 by triangle inequality and considering we need an integer) and using a + b + c = x. The most useful min is the maximum of these two possibilities. The max value of b is (x-a)//2, which is derived from b < c.  
'''

def triplets_with_sum(number):
	triplets_sum_list = []
	triplets_list = triplets_in_range(1, number)
	for triplet in triplets_list:
		if is_triplet(triplet) is True:
			triplets_sum_list.append(triplet)
	print(triplets_sum_list)
	return triplets_sum_list


def triplets_in_range(start, end):
	triplets = []
	for a in range(1, end // 2):
		b_max = (end - a) // 2
		b_min = max(a + 1, (end // 2) - a)
		for b in range(b_min, b_max + 1):
			triplets.append([a, b, end - a - b])
	return triplets 

def is_triplet(triplet):
	return triplet[0]**2 + triplet[1]**2 == triplet[2]**2

