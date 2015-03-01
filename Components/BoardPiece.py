class BoardPiece:
	def __init__(self, name, type, players=[], left=None, right=None, above=None, below=None, secret=None):
		self.name = name
		self.type = type
		self.players = players
		self.left = left
		self.right = right
		self.above = above
		self.below = below
		self.secret = secret
	
	def getAdjacentSpots(self):
		adj = []
		if self.left != None:
			adj.append(self.left)
		if self.right != None:
			adj.append(self.right)
		if self.above != None:
			adj.append(self.above)
		if self.below != None:
			adj.append(self.below)
		if self.secret != None:
			adj.append(self.secret)
		
		return adj
		
	def removePlayer(self, name):
		for player in self.players:
			if player == name:
				self.players.remove(player)
				return
				
	def addPlayer(self,name):
		self.players.append(name)
		
	def __str__(self):
		return "%s -> %s" % (self.type, self.name)
		
	def __repr__(self):
		return self.__str__()
