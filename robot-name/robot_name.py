import random
import string

class Robot:
	uniqueNames = []

	def __init__(self):
		possibleName = self.randomName()
		while possibleName in Robot.uniqueNames:
			possibleName = self.randomName()

		self.name = possibleName
		Robot.uniqueNames.append(self.name)

	def randomName(self):
		letters = ''.join([random.choice(string.ascii_uppercase) for i in range(2)])
		numbers = ''.join([random.choice(string.digits) for i in range(3)])
		return letters + numbers
	
	def reset(self):
		self.__init__()
