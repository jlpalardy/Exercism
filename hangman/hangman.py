# Game status categories
# Change the values as you see fit

STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"

class Hangman:
	def __init__(self, word):
		self.remaining_guesses = 9
		self.status = STATUS_ONGOING
		for char in word:
			if not char.isalpha():
				raise ValueError('No punctuation or numbers, please!')
		self.word = word.lower()
		self.unguessed = set(self.word)
		self.guessed = []

	def guess(self, char):
		#Handling bad guesses
		if self.status != STATUS_ONGOING:
			raise ValueError('Game over!')
		elif len(char) != 1 or char.isalpha() == False:
			print('Guess only letters, and only one at a time!')
			self.remaining_guesses -= 1
		elif char in self.guessed:
			print('You already guessed that!')
			self.remaining_guesses -= 1
		else:
			c = char.lower()
			if c in self.unguessed:
				self.unguessed.remove(c)
				print(f'Good guess! You have {self.remaining_guesses} left.')
				print(self.get_masked_word())
			else:
				self.remaining_guesses -= 1
				print(f'Nope! You have {self.remaining_guesses} guesses left.') 
		self.update_status() 		

	def update_status(self):
		if len(self.unguessed) == 0:
			self.status = STATUS_WIN
			print('You win!')
		if self.remaining_guesses < 0:
			self.status = STATUS_LOSE
			print(f'You lose! The word was \'{self.word}\'.')
		
	def get_masked_word(self):
		return ''.join('_' if l.lower() in self.unguessed else l for l in self.word)

	def get_status(self):
		return self.status
		
