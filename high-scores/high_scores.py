def latest(scores):
	return scores[len(scores)-1]

def personal_best(scores):
	scoreSorted = scores.copy()
	scoreSorted.sort()
	return scoreSorted[len(scoreSorted)-1]

def personal_top_three(scores):
	scoreSorted = scores.copy()
	scoreSorted.sort(reverse = True)
	if len(scoreSorted) >= 3:
		return scoreSorted[0:3]
	else:
		return scoreSorted


