from typing import *
from Constants import *
from Components.Card import *
from Components.BoardPiece import *
from Components.Player import *
from Server import *
from UI.GUI import *
from twisted.internet import reactor, tksupport
from twisted.internet.task import LoopingCall
from multiprocessing import Process
from Listener import *
import XMLManager as XML
import random
import sys, os

class GameController:
        def __init__(self, cards, pieces, players):
                self.cards = cards
                self.pieces = pieces
                self.players = players
                self.availableChars = NAMES.keys()
                self.player = None
                self.character = None
                self.yourTurn = False
                self.canMove = False
                self.host = False
                self.connectionIP = None
                self.suggestedPlayer = None
                self.suggestedWeapon = None
                self.suggestedRoom = None
        def startGame(self):
                self.gui = GUI(self)
                self.gui.launchWelcomeScreen()
                self.gui.launchSelectCharScreen()
                self.gui.launchGameScreen()

        def launchGame(self):   
                cards = self.cards

                # Choose murder weapon, room, and character
                while self.murderWeapon == None:
                        c = cards[random.randint(0,len(cards)-1)]
                        if c.type == WEAPON:
                                self.murderWeapon = c.label
                                cards.remove(c)
                while self.murderChar == None:
                        c = cards[random.randint(0,len(cards)-1)]
                        if c.type == PERSON:
                                self.murderChar = c.label
                                cards.remove(c)
                while self.murderRoom == None:
                        c = cards[random.randint(0,len(cards)-1)]
                        if c.type == ROOM:
                                self.murderRoom = c.label
                                cards.remove(c)
                self.sendMurderCardsMessage()

                # Deal Cards to players
                for player in self.players:
                        s = ""
                        c = cards[random.randint(0,len(cards)-1)]
                        s += c.label + ","
                        cards.remove(c)
                        c = cards[random.randint(0,len(cards)-1)]
                        s += c.label + ","
                        cards.remove(c)
                        c = cards[random.randint(0,len(cards)-1)]
                        s += c.label
                        cards.remove(c)
                        if player.name == self.player:
                                self.getPlayer(self.player).cards = s.split(",")
                        else:
                                self.sendCardsMessage(player.name, s)

                # Determine player order
                order = ""
                for player in self.players:
                        order += player.name + ","
                order = order[0:len(order)-1]
                self.sendPlayerOrderMessage(order)

                # Send start game message
                self.playerRotation = order.split(",")
                self.sendStartGameMessage()
                self.gameStarted = True
                if self.playerRotation[0] == self.player:
                        self.yourTurn = True
                        self.canMove = True
                self.gui.updatePlayerInfoBox()

def handleListenerInput(self, message):
        print ("Message: %s") % message
        message_dict = XML.parseData(message)
        description = message_dict[DESCRIPTION_TAG]
        if description == MAKE_SUGGESTION:
                name = message_dict[PLAYER_TAG]
                self.suggestedRoom = message_dict[ROOM_TAG]
                self.suggestedPlayer = message_dict[CHARACTER_TAG]
                self.suggestedWeapon = message_dict[WEAPON_TAG]
                up = "%s suggested:\n%s\n%s\n%s" % (name,self.suggestedRoom,self.suggestedPlayer,self.suggestedWeapon)
                self.gui.updateNotificationBox(up)
                now = self.getNextPlayer(name)
                self.currSuggester = now
                if now == self.player:
                        self.gui.launchDisproveSuggestionScreen()
        elif description == MOVE_PLAYER:
                name = message_dict[PLAYER_TAG]
                loc = message_dict[ROOM_TAG]
                self.movePlayer(name, loc)
                self.gui.updateGameBoard()
                up = "%s moved to:\n  %s" % (name,loc)
                self.gui.updateNotificationBox(up)
        elif description == MAKE_CORRECT_ACCUSATION:
                player = message_dict[PLAYER_TAG]
                weapon = message_dict[WEAPON_TAG]
                room = message_dict[ROOM_TAG]
                char = message_dict[CHARACTER_TAG]
                self.gui.launchGameOverScreen(player, char, room, weapon)
                sys.exit()
                os._exit(1)
        elif description == MAKE_WRONG_ACCUSATION:
                player = message_dict[PLAYER_TAG]
                weapon = message_dict[WEAPON_TAG]
                room = message_dict[ROOM_TAG]
                char = message_dict[CHARACTER_TAG]
                self.gui.launchOtherWrongAccusationScreen(player, char, room, weapon)               
                self.currPlayerTurn = self.getNextPlayer(player)
                self.removePlayerFromGame(player)
                self.gui.updatePlayerInfoBox()
                self.gui.updateGameBoard()
                up = "%s is out of the game" % (player)
                self.gui.updateNotificationBox(up)
                if self.currPlayerTurn == self.player:
                        self.yourTurn = True
                        self.canMove = True
                        self.gui.updatePlayerInfoBox()
                        self.gui.launchAccusationScreen()
                        self.gui.launchMovePlayerScreen()
                        if self.getLocationType(self.player) == ROOM:
                                self.gui.launchSuggestionScreen()        
                                self.sendSuggestionMessage()
                        else:
                                self.endTurn()
                print ("Need to remove player from game")
        elif description == SUGGESTION_DISPROVED:
                if self.yourTurn:
                        name = message_dict[PLAYER_TAG]
                        c = message_dict[CHOICE_TAG]
                        mess = "%s disproved your suggestion\nwith: %s" % (name, c)
                        self.gui.updateSuggestionBox(mess)
                        self.gui.launchAccusationScreen()
                        if self.gameOver:
                                print ("Manage game over")
                        else:
                                self.gui.updatePlayerInfoBox()
                                self.endTurn()
        elif description == SUGGESTION_NOT_DISPROVED:
                name = message_dict[PLAYER_TAG]
                now = self.getNextPlayer(name)
                self.currSuggester = now
                up = "%s did not disprove\nthe suggestion" % (name)
                self.gui.updateNotificationBox(up)
                if now == self.player and self.yourTurn:
                        self.endTurn()
                elif now == self.player:
                        self.gui.launchDisproveSuggestionScreen()
        elif description == END_TURN:
                name = message_dict[PLAYER_TAG]
                self.currPlayerTurn = self.getNextPlayer(name)
                self.gui.updatePlayerInfoBox()
                self.gui.updateGameBoard()
                up = "%s ended their turn" % (name)
                self.gui.updateNotificationBox(up)
                if self.currPlayerTurn == self.player:
                        self.yourTurn = True
                        self.canMove = True
                        self.gui.updatePlayerInfoBox()
                        self.gui.launchAccusationScreen()
                        if self.gameOver:
                                print ("Game Over!!!!")
                        else:
                                self.gui.launchMovePlayerScreen()
                                if self.getLocationType(self.player) == ROOM:
                                        self.gui.launchSuggestionScreen()        
                                        self.sendSuggestionMessage()
                                else:
                                        self.endTurn()
        elif description == SEND_PLAYER_ORDER:
                l = message_dict[CHOICE_TAG]
                order = l.split(',')
                self.playerRotation = order
        elif description == SEND_PLAYER_CARDS:
                name = message_dict[PLAYER_TAG]
                if self.player == name:
                        cards = message_dict[CHOICE_TAG]
                        cardList = cards.split(',')
                        self.getPlayer(self.player).cards = cardList
        elif description == START_GAME:
                self.gameStarted = True
                self.gui.updatePlayerInfoBox()
                up = "Game started!"
                self.gui.updateNotificationBox(up)
                if self.player == self.playerRotation[0]:
                        self.yourTurn = True
                        self.canMove = True
                        self.gui.updatePlayerInfoBox()
                        self.gui.launchAccusationScreen()
                        self.gui.launchMovePlayerScreen()
        elif description == SEND_MURDER_CARDS:
                self.murderChar = message_dict[CHARACTER_TAG]
                self.murderRoom = message_dict[ROOM_TAG]
                self.murderWeapon = message_dict[WEAPON_TAG]
        elif description == JOIN_GAME:
                name = message_dict[PLAYER_TAG]
                char = message_dict[CHARACTER_TAG]
                up = "%s joined game\nas %s" % (name,char)
                self.gui.updateNotificationBox(up)
                if self.getPlayer(name) == None:
                        self.addPlayer(name, char)
                        self.sendJoinGameMessage()
                self.gui.updateGameBoard()
        else:
                print ("WHY input not correct?!?!")                        
                
        #print "handleListenerInput"
        #print message
        #self.client.protocol.sendMessage("From %s" % self.player)
        # Update

        def endTurn(self):
                self.currPlayerTurn = self.getNextPlayer(self.player)
                self.yourTurn = False
                self.canMove = False
                self.gui.updatePlayerInfoBox()
                self.gui.updateGameBoard()
                self.sendEndTurnMessage()

        def getNextPlayer(self, name):
                i = self.playerRotation.index(name)
                if i == len(self.playerRotation) - 1:
                        return self.playerRotation[0]
                else:
                        return self.playerRotation[i + 1]

        def getCardType(self, name):
                weapons = CARDS[WEAPON]
                for w in weapons:
                        if w == name:
                                return WEAPON
                characters = CARDS[PERSON]
                for c in characters:
                        if c == name:
                                return PERSON
                rooms = CARDS[ROOM]
                for r in rooms:
                        if r == name:
                                return ROOM
                # Shouldn't get here
                return None

        def sendMurderCardsMessage(self):
                message = XML.formatData(SEND_MURDER_CARDS, room = self.murderRoom,
                                         character = self.murderChar, weapon = self.murderWeapon)
                self.sendUpdate(message)

        def sendJoinGameMessage(self):
                message = XML.formatData(JOIN_GAME, player = self.player, character = self.getPlayer(self.player).character)
                self.sendUpdate(message)

        def sendPlayerOrderMessage(self, message):
                message = XML.formatData(SEND_PLAYER_ORDER, choice = message)
                self.sendUpdate(message)

        def sendStartGameMessage(self):
                message = XML.formatData(START_GAME)
                self.sendUpdate(message)

        def sendCardsMessage(self, player, cardString):
                message = XML.formatData(SEND_PLAYER_CARDS, player = player, choice = cardString)
                self.sendUpdate(message)

        def sendEndTurnMessage(self):
                message = XML.formatData(END_TURN, player = self.player)
                self.sendUpdate(message)

        def sendSuggestionMessage(self):
                message = XML.formatData(MAKE_SUGGESTION, player = self.player, room = self.suggestedRoom,
                                         character = self.suggestedPlayer, weapon = self.suggestedWeapon)
                self.sendUpdate(message)

        def sendPlayerMoveMessage(self):
                message = XML.formatData(MOVE_PLAYER, player = self.player, room = self.getPlayerLocation(self.player))
                self.sendUpdate(message)

        def sendDisprovedSuggestion(self, card):
                message = XML.formatData(SUGGESTION_DISPROVED, player = self.player, choice = card)
                self.sendUpdate(message)

        def sendNotDisprovedSuggestion(self):
                message = XML.formatData(SUGGESTION_NOT_DISPROVED, player = self.player)
                self.sendUpdate(message)

        def sendMakeCorrectAccusation(self):
                message = XML.formatData(MAKE_CORRECT_ACCUSATION, player = self.player, room = self.murderRoom,
                                         weapon = self.murderWeapon, character = self.murderChar)
                self.sendUpdate(message)

        def sendMakeWrongAccusation(self):
                message = XML.formatData(MAKE_WRONG_ACCUSATION, player = self.player, character = self.accusedPlayer,
                                         weapon = self.accusedWeapon, room = self.accusedRoom)
                self.sendUpdate(message)
                
def sendUpdate(self, message):
        self.client.protocol.sendMessage(message)

def initClient(self):
        #host = "127.0.0.1"
        #lc = LoopingCall(self.updateBoard)
        #lc.start(1)
        #tksupport.install(widget)
        print ("Init Client!")
        self.client = Client_Factory(self)
        print ("Client: ") + str(self.client)
        reactor.connectTCP(self.connectionIP, PORT_SERVER, self.client)
        reactor.run()
        #self.runServer()
        print ("initialized client")

        def updateBoard(self):
                print ("Update Board")

        def initServer(self):
                #tksupport.install(widget)
                reactor.listenTCP(8123, ServerFactory(self))
                reactor.run()

        # Add a player to the game
        def addPlayer(self, name, charName):
                player = Player(name, charName)
                player.location = charName
                self.players.append(player)
                #for p in self.pieces:
                        #print "Name: %s, Players: %s" % (p.name, str(p.players))
                for piece in self.pieces:
                        #print piece
                        if piece.name == charName:
                                #print "adding player to: %s" % piece.name
                                piece.addPlayer(name)
                #print "-------------------"
                #for p in self.pieces:
                #        print "Name: %s, Players: %s" % (p.name, str(p.players))
	
	# Move a player to a specified location
	# Params:
	#	name -> String of player's name
	#	location -> String of location name
def movePlayer(self, name, location):
        # Update location of player within player object
        for player in self.players:
                if player.name == name:
                        old_location = player.location
                        player.location = location
                        #print "New player location: %s" % player.location
        # Update players at specific locations after move
        for piece in self.pieces:
                if piece.name == location:
                        piece.addPlayer(name)
                elif piece.name == old_location:
                        piece.removePlayer(name)
				
	# Get piece associated with piece name passed in
def getPiece(self, name):
        for piece in self.pieces:
                if piece.name == name:
                        #print "getPiece: %s" % piece.name
                        return piece

# Get card associated with card name passed in
def getCard(self, name):
        for card in self.cards:
                if card.label == name:
                        return card

        # Get player associated with player name passed in
        def getPlayer(self, name):
                for player in self.players:
                        if player.name == name:
                                return player
                return None

        def getAdjacentPieces(self, location):
                piece = self.getPiece(location)
                print("Loc: %s, Piece: %s") % (location, piece.name)
                return piece.getAdjacentSpots()

        def getPlayersAtLocation(self, location):
                piece = self.getPiece(location)
                return piece.players

        # Pass in the name of a location
        def getPlayerNamesAtLocation(self, location):
                players = self.getPlayersAtLocation(location)
                names = []
                for player in players:
                        names.append(player.name)

        # Get location of player given name
        def getPlayerLocation(self, name):
                player = self.getPlayer(name)
                return player.location

        # Get location for player playing on the local client
        def getMyLocation(self):
                return self.getPlayerLocation(self.player)
			
	# Pass in the name of a player
	# Return list of piece names (strings) that are valid
def getValidLocationsToMoveTo(self, name):
        player = self.getPlayer(name)
        location = self.getPlayerLocation(self.player)
        print ("Player location: %s") % location
        pieces = self.getAdjacentPieces(location)
        print ("Valid pieces: %s") % str(pieces)
        valid_spots = []
        for p in pieces:
                piece = self.getPiece(p)
                print("Adj: %s") % piece.name
                players = piece.players
                if len(players) == 0:
                        valid_spots.append(piece.name)
                elif piece.type == ROOM:
                        valid_spots.append(piece.name)
        return valid_spots

        # Check off any cards on the player notecard passed in here
def updateNotecard(self, character=None, location=None, card=None):
                if character != None:
                        self.player.notebook.append(getCard(character))
                if location != None:
        
                        self.player.notebook.append(getCard(location))
                if card != None:
                        self.player.notebook.append(getCard(card))

        # Check if a character is available to play with
def isCharAvailable(self, name):
                for i in self.availableChars:
                        if name == i:
                                return True
                return False

	# Get a formatted string containing the player's name and character
def getPlayerInfo(self):
        info = "Your Name: %s\n" % self.player
        info += "Character: %s\n" % self.character
        info += "Location: %s\n" % self.getPlayerLocation(self.player)
        info += "Cards: "
        if self.getPlayer(self.player).cards != None:
                for card in self.getPlayer(self.player).cards:
                        info += card + " "
        info += "\nYour Turn = %s" % str(self.yourTurn)
        return info

        # Get formatted text for a board piece
def getBoardPieceText(self, name):
                text = ""
                piece = self.getPiece(name)
                if piece.secret == None:
                        text += "%s:\n" % piece.name
                else:
                        text += "%s(S):\n" % piece.name
                #print "Get: Piece: %s, Players: %s" % (name, str(piece.players))
                for player in piece.players:
                        text += "%s\n" % player
                return text

        # Register a suggestion from the user
def registerSuggestion(self, suspect, weapon, room):
                self.suggestedPlayer = suspect
                self.suggestedWeapon = weapon






                self.suggestedRoom = room

        # Register a accusation from the user
def handleAccusation(self, suspect, weapon, room):
                self.accusedPlayer = suspect
                self.accusedWeapon = weapon
                self.accusedRoom = room
                self.gameOver = True
                if self.murderWeapon == weapon and self.murderChar == suspect and self.murderRoom == room:
                        self.sendMakeCorrectAccusation()
                        self.gui.launchGameOverScreen(self.player, suspect, room, weapon)
                else:
                        self.sendMakeWrongAccusation()
                        self.gui.launchWrongAccusationScreen(self.player, suspect, room, weapon,
                                                             self.murderChar, self.murderRoom, self.murderWeapon)
                #print "Destroy!"
                #self.gui.gameScreen.gamescreen.destroy()
                print ("System exit!")
                sys.exit()
                #os._exit(1)
                #print "Raise"
                #raise SystemExit

        # Helper function to get all character names
def getAllCharacterNames(self):
                return NAMES.keys()

        # Helper function to get all weapon names
def getAllWeaponNames(self):
                return CARDS[WEAPON]

        # Helper function to get all room names








def getAllRoomNames(self):
                return CARDS[ROOM]

        # Get cards in client players hand
def getYourCards(self):
                player = self.getPlayer(self.player)
                return player.cards

        # Get board piece type
def getLocationType(self, player):
                loc = self.getPlayerLocation(player)
                if "Hallway" in loc:
                        return HALLWAY
                else:
                        return ROOM

        # Remove player from game
def removePlayerFromGame(self, name):
                player = self.getPlayer(name)
                loc = player.location
                piece = self.getPiece(loc)
                piece.removePlayer(name)
                for p in self.playerRotation:
                        if p == name:
                                self.playerRotation.remove(p)
                self.players.remove(player)
				

