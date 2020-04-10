class Allergies:

	def __init__(self, score):
		self.allergy_score = score
		self.allergy_dict = {'eggs':1, 'peanuts':2, 'shellfish':4, 'strawberries':8, 'tomatoes':16, 'chocolate':32, 'pollen':64, 'cats': 128}
		self.allergies_set = set()
		
	def allergic_to(self, item = None):
		score = self.allergy_score
		for key, value in sorted(self.allergy_dict.items(),reverse=True,key=lambda p:p[1]):
			while score >= value:
				score -= value
				self.allergies_set.add(key)
		return item in self.allergies_set
	
	@property
	def lst(self):
		self.allergic_to()
		return list(self.allergies_set)
