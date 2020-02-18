import random
import math 

class Character:
	def __init__(self):
		self.strength = self.ability()
		self.dexterity = self.ability()
		self.constitution = self.ability()
		self.intelligence = self.ability()
		self.wisdom = self.ability()
		self.charisma = self.ability()
		self.hitpoints = self.hitPoints()

	def ability(self):
		dieList = []
		for num in range(4):
			dieList.append(random.randint(1,6))
		dieList.sort()
		return sum(dieList[1:])

	def hitPoints(self):
		return 10 + modifier(self.constitution)

	def __str__(self):
		return f'Strength: {self.strength}\nDexterity: {self.dexterity}\nConstitution: {self.constitution}\nIntelligence: {self.intelligence}\nWisdom: {self.wisdom}\nCharisma: {self.charisma}\nHitpoints: {self.hitpoints}'

def modifier(ability):
	return math.floor((ability - 10)/2)

