from tkinter import *
from tkinter import ttk
from UI.welcomeScreen import *
from UI.selectCharScreen import *
from UI.gameScreen import *
from UI.suggestion import *
from UI.accusation import *
from UI.movePlayerScreen import *
from UI.canYouDisproveSugg import *


class GUI:
    def __init__(self, controller):
        self.controller = controller
        self.gameScreen = None

    def launchWelcomeScreen(self):
        welcome = WelcomeScreen(self.controller)
        welcome.initScreen()

    def launchSelectCharScreen(self):
        selectChar = SelectCharScreen(self.controller)
        selectChar.initScreen()

    def launchGameScreen(self):
        self.gameScreen = GameScreen(self.controller)
        self.gameScreen.initScreen()

    def launchSuggestionScreen(self):
        suggestionScreen = SuggestionScreen(self.controller)
        suggestionScreen.initScreen()

    def launchAccusationScreen(self):
        accusationScreen = AccusationScreen(self.controller)
        accusationScreen.initScreen()

    def launchMovePlayerScreen(self):
        movePlayerScreen = MovePlayerScreen(self.controller)
        movePlayerScreen.initScreen()

    def launchDisproveSuggestionScreen(self):
        disproveSuggestionScreen = DisproveSuggestionScreen(self.controller)
        disproveSuggestionScreen.initScreen()

    def updateGameBoard(self):
        self.gameScreen.updateBoardPieces()

    def updateSuggestionBox(self, message):
        self.gameScreen.updateSuggestionBox(message)

    def updateNotificationBox(self, message):
        self.gameScreen.updateNotificationBox(message)

    def updatePlayerInfoBox(self):
        self.gameScreen.updatePlayerInfoBox()

    def launchGameOverScreen(self, name, suspect, room, weapon):
        self.gameScreen.gameover(name, suspect, room, weapon)

    def launchWrongAccusationScreen(self, player, suspect, room, weapon,
                                    murderChar, murderRoom, murderWeapon):
        self.gameScreen.wrongAccusation(player, suspect, room, weapon,
                                        murderChar, murderRoom, murderWeapon)

    def launchOtherWrongAccusationScreen(self, player, suspect, room, weapon):
        self.gameScreen.otherWrongAccusation(player, suspect, room, weapon)


if __name__ == "__main__":
    gui = GUI(None)
    gui.launchWelcomeScreen()
        
