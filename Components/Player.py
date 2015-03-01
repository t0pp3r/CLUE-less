
class Player:
	def __init__(self, name, character):
		self.name = name
		self.character = character
		self.cards = None
		self.location = None
		self.notebook = None
	
	def __str__(self):
		return "{}\n\tCharacter = {}\n\tCards = {}\n\tLocation = {}\n\tNotebook = {}".format(self.name, self.character, self.cards, self.location, self.notebook)
		
	def __repr__(self):
		return self.__str__()
		