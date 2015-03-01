class Card:
	def __init__(self, type, label):
		self.type = type
		self.label = label
		
	def __str__(self):
		return "%s -> %s" % (self.type, self.label)
		
	def __repr__(self):
		return self.__str__()
		
		