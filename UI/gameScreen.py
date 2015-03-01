from Tkinter import *
import ttk
import itertools
import tkMessageBox
import tkFont
import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from Constants import *
from twisted.internet import tksupport

class GameScreen:
    def __init__(self, controller):
        self.controller = controller
        self.gamescreen = None
        self.notiftextbox = None
        self.sugghistbox = None
        self.playerinfobox = None
        self.btn1 = None
        self.btn2 = None 
        self.btn3 = None 
        self.btn4 = None 
        self.btn5 = None 
        self.btn6 = None 
        self.btn7 = None 
        self.btn8 = None 
        self.btn9 = None 
        self.btn10 = None 
        self.btn11 = None
        self.btn12 = None
        self.btn13 = None
        self.btn14 = None
        self.btn15 = None
        self.btn16 = None
        self.btn17 = None
        self.btn18 = None
        self.btn19 = None
        self.btn20 = None
        self.btn21 = None
        self.btn22 = None
        self.btn23 = None
        self.btn24 = None
        self.btn25 = None
        self.btn26 = None
        self.btn27 = None


    def yourTurn(self):
        tkMessageBox.showinfo(title = "Clue-Less Message: Your Turn", message = "<<Player>>, it is now your turn")

    def connectionError(self):
        tkMessageBox.showerror(title = "Clue-Less Message:  Connection Error", message = "Sorry, Clue-Less could not connect to <<IP>>.  Please check the IP address port and try again")

    def hallwaysBlocked(self):
        tkMessageBox.showinfo(title = "Clue-Less Message:  Lose Turn", message = "<<Player>>, all hallways are blocked.  Your only option is to make an Accusation.")

    def disproveSuggestion(self):
        tkMessageBox.askyesno(title = "Clue-Less Message:  Disprove Suggestion", message = "<<Player>>, <<Player>> made a suggestion of:  <<Suspect>> in <<Room>> with a <<Weapon>>.  Can you disprove this?")

    def disproveSuggFalse(self):
        tkMessageBox.showinfo(title = "Clue-Less Message:  Disprove Suggestion", message = "<<Player>>, your card could not disprove <<Player>> suggestion.")

    def disproveSuggTrue(self):
        tkMessageBox.showinfo(title = "Clue-Less Message:  Suggestion Disproved", message = "<<Player>>, your suggestion has been disproved by <<Player>> with the <<card>>")

    def accusationFalse(self):
        tkMessageBox.showinfo(title = "Clue-Less Message:  Accusation", message = "<<Player>>, you accused <<Suspect>> in <<Room>> with a <<Weapon>>.  Your answer was incorrect.  Sorry this is the end of the game for you.")
        
    def gameover(self, name, suspect, room, weapon):
        tkMessageBox.showinfo(title = "Clue-Less Message:  Game Over", message = "%s has solved the mystery with a correct accusation!\nIt was %s in the %s with the %s!" % (name, suspect, room, weapon))    

    def wrongAccusation(self, player, suspect, room, weapon, murderChar, murderRoom, murderWeapon):
        tkMessageBox.showinfo(title = "Clue-Less Message: Wrong Accusation",
                              message = "You made the wrong accusation!\n\nYou accused:\n%s\n%s\n%s\n\nActual murder info is:\n%s\n%s\n%s" %
                              (suspect, room, weapon, murderChar, murderRoom, murderWeapon))

    def otherWrongAccusation(self, name, suspect, room, weapon):
        tkMessageBox.showinfo(title = "Clue-Less Message:  Wrong accusation made",
                              message = "%s made the wrong accusation of:\n %s in the %s with the %s\nThey are removed from the game." % (name, suspect, room, weapon))    
                                                    
    def startGame(self):
        pass
    
    def aboutGame(self):
        pass

    def updateNotificationBox(self, message):
        self.notiftextbox.delete(1.0, END)
        self.notiftextbox.insert(INSERT, message)

    def updateSuggestionBox(self, message):
        self.sugghistbox.delete(1.0, END)
        self.sugghistbox.insert(INSERT, message)

    def updatePlayerInfoBox(self):
        message = self.controller.getPlayerInfo()
        self.playerinfobox.delete(1.0, END)
        self.playerinfobox.insert(INSERT, message)
        

    def boardButtonPressed(self, name):
        if self.controller.gameStarted == False:
            tkMessageBox.showinfo(title = "Clue-Less Message:  Game not started yet", message = "Game not started by host yet.")
        elif self.controller.yourTurn == False:
            tkMessageBox.showinfo(title = "Clue-Less Message:  Please wait for you turn", message = "Please wait for your turn.")
        else:
            self.controller.canMove == False
            self.controller.gui.launchAccusationScreen()
            self.controller.gui.launchMovePlayerScreen()
            self.updateBoardPieces()
            if self.controller.getLocationType(self.controller.player) == ROOM:
                self.controller.gui.launchSuggestionScreen()        
                self.controller.sendSuggestionMessage()
            else:
                self.controller.endTurn()
            #self.controller.gui.launchAccusationScreen()
            
 
        #self.updateBoardPieces()
        #self.controller.gui.launchSuggestionScreen()
        #self.controller.gui.launchMovePlayerScreen()
        #self.controller.gui.launchAccusationScreen()
        print "We're back!"
        self.updateBoardPieces()
        print name

    def initClientButtonPressed(self):
        if self.controller.client == None:
            self.controller.initClient()

    def joinGameButtonPressed(self):
        self.controller.sendJoinGameMessage()

    def launchGameButtonPressed(self):
        self.controller.launchGame()

    def updateBoardPieces(self):
        print "Starting update!"
        self.btn1["text"] = self.controller.getBoardPieceText(PROFESSOR_PLUM)
        self.btn2["text"] = self.controller.getBoardPieceText(MRS_PEACOCK)
        self.btn3["text"] = self.controller.getBoardPieceText(STUDY)
        self.btn4["text"] = self.controller.getBoardPieceText(H1)
        self.btn5["text"] = self.controller.getBoardPieceText(LIBRARY)
        self.btn6["text"] = self.controller.getBoardPieceText(H2)
        self.btn7["text"] = self.controller.getBoardPieceText(CONSERVATORY)
        self.btn8["text"] = self.controller.getBoardPieceText(H3)
        self.btn9["text"] = self.controller.getBoardPieceText(H4)
        self.btn10["text"] = self.controller.getBoardPieceText(H5)
        self.btn11["text"] = self.controller.getBoardPieceText(MR_GREEN)
        self.btn12["text"] = self.controller.getBoardPieceText(HALL)
        self.btn13["text"] = self.controller.getBoardPieceText(H6)
        self.btn14["text"] = self.controller.getBoardPieceText(BILLIARD_ROOM)
        self.btn15["text"] = self.controller.getBoardPieceText(H7)
        self.btn16["text"] = self.controller.getBoardPieceText(BALLROOM)
        self.btn17["text"] = self.controller.getBoardPieceText(MISS_SCARLET)
        self.btn18["text"] = self.controller.getBoardPieceText(H8)
        self.btn19["text"] = self.controller.getBoardPieceText(H9)
        self.btn20["text"] = self.controller.getBoardPieceText(H10)
        self.btn21["text"] = self.controller.getBoardPieceText(MRS_WHITE)
        self.btn22["text"] = self.controller.getBoardPieceText(LOUNGE)
        self.btn23["text"] = self.controller.getBoardPieceText(H11)
        self.btn24["text"] = self.controller.getBoardPieceText(DINING_ROOM)
        self.btn25["text"] = self.controller.getBoardPieceText(H12)
        self.btn26["text"] = self.controller.getBoardPieceText(KITCHEN)
        self.btn27["text"] = self.controller.getBoardPieceText(COLONEL_MUSTARD)
        print "Finished update!"

        

    def initScreen(self):
        self.gamescreen = Tk()
        Grid.rowconfigure(self.gamescreen,0,weight=1)
        Grid.columnconfigure(self.gamescreen,0,weight=1)
        
        menubar = Menu(self.gamescreen)
        filemenu = Menu(menubar, tearoff = 0)
        filemenu.add_command(label = "Start New Game", command = self.startGame)
        filemenu.add_command(label = "Start Client", command = self.initClientButtonPressed)
        filemenu.add_command(label = "Join Game", command = self.joinGameButtonPressed)
        filemenu.add_command(label = "Launch Game", command = self.launchGameButtonPressed)

        filemenu.add_separator()

        filemenu.add_command(label = "Quit", command = self.gamescreen.quit)
        menubar.add_cascade(label = "File", menu = filemenu)

        helpmenu = Menu(menubar, tearoff = 0)
        helpmenu.add_cascade(label = "Help", command = self.aboutGame)
        helpmenu.add_cascade(label = "About Game", command = self.aboutGame)
        menubar.add_cascade(label = "Help", menu = helpmenu)

        self.gamescreen.config(menu = menubar)


        #Fonts
        customFont = tkFont.Font(family = "Helvetica", size=24, weight = 'bold', slant = 'italic', )
        customFont1 = tkFont.Font(family = "Helvetica", size=18, weight = 'bold')
        customFont2 = tkFont.Font(family = "Helvetica", size= 8, weight = 'bold')

        #Frames
        notification = ttk.Frame(self.gamescreen, padding = (5,5,5,5))
        notif_board = ttk.Labelframe(notification, text = "Notification Board", borderwidth = 5, relief = "sunken", width = 300, height = 120)
        sugg_board = ttk.Labelframe(notification, text = "Suggestion Board", borderwidth = 5, relief = "sunken", width = 400, height = 120)
        player_info = ttk.Labelframe(notification, text = "Player Info", borderwidth = 5, relief = "sunken", width = 400, height = 120)

        self.notiftextbox = Text(notif_board, height = 100, width = 50, wrap = "word")
        self.notiftextbox.insert(INSERT, "Please go to the menu bar and select\n the 'Start Client' button.")
        self.sugghistbox = Text(sugg_board, height = 100, width = 50, wrap = "word")
        self.sugghistbox.insert(INSERT, "This is where we display the \nsuggestion history.")
        self.playerinfobox = Text(player_info, height = 100, width = 50, wrap = "word")
        self.playerinfobox.insert(INSERT, self.controller.getPlayerInfo())#"This is where we display each players info.")

        self.notiftextbox.grid(column = 0, row = 0, sticky = (N,E,W),padx =5, pady = 5)
        self.sugghistbox.grid(column=1, row=0, sticky = (N,E,W), padx = 5, pady = 5)
        self.playerinfobox.grid(column=2, row=0, sticky = (N,E,W), padx = 5, pady = 5)

        notif_board.grid(column = 0, row = 0, sticky = (N,W),padx = 5, pady = 5)
        notif_board.grid_propagate(False)
        sugg_board.grid(column=1, row=0, sticky = (N), padx = 5, pady = 5)
        sugg_board.grid_propagate(False) 
        player_info.grid(column=2, row=0, sticky = (N,E,W,S), padx = 5, pady = 5)
        player_info.grid_propagate(False)

        gameboard = ttk.Labelframe(self.gamescreen, padding = (8,8,8,8), text = "Gameboard", relief = "sunken")

        ###these buttons will not be displayed on the gameboard b/c they do not have any labels (room, hallway, starting space)
        ##forgetButtons = [0,1,3,5,6,7,13,14,16,18,21,27,30,32,35,41,42,43,45,46,47,48]
        ##
        ###this list tracks all the buttons on the gameboard
        ##buttonNames = ["Prof. Plum", "Mrs. Peacock", "Study", "Hallway 1", "Library", "Hallway 2", "Conservatory", "Hallway 3", "Hallway 4", "Hallway 5", "Mr. Green", "Hall",
        ##               "Hallway 6", "Billiard", "Hallway 7", "Ballroom", "Miss Scarlet", "Hallway 8", "Hallway 9", "Hallway 10", "Mrs. White", "Lounge", "Hallway 11", "Dining Room",
        ##               "Hallway 12", "Kitchen", "Col. Mustard"]
        ##
        ##def printName(name):
        ##    print name
        ##
        ##
        ##myButtons = []
        ##count = 0
        ##for x, y in itertools.product(range(7), repeat=2):
        ##    if not x*7 + y in forgetButtons:
        ##            a = buttonNames[count]
        ##            btn = Button(gameboard, width=9, height=4, font = customFont2, text=buttonNames[count], command = lambda: printName("name"))
        ##            btn.grid(column=x, row=y, padx=3, pady=3)
        ##            myButtons.append(btn)
        ##            count = count + 1

        self.btn1 =  Button(gameboard, width = 13, height = 4, font = customFont2, text = PROFESSOR_PLUM, wraplength = 60, command = lambda: self.boardButtonPressed(PROFESSOR_PLUM))
        self.btn1.grid(column = 0, row = 2, padx = 3, pady = 3)
        self.btn2 =  Button(gameboard, width = 13, height = 4, font = customFont2, text = MRS_PEACOCK, wraplength = 60, command = lambda: self.boardButtonPressed(MRS_PEACOCK))
        self.btn2.grid(column = 0, row = 4, padx = 3, pady = 3)
        self.btn3 =  Button(gameboard, width = 13, height = 4, font = customFont2, text = STUDY, command = lambda: self.boardButtonPressed(STUDY))
        self.btn3.grid(column = 1, row = 1, padx = 3, pady = 3)
        self.btn4 =  Button(gameboard, width = 13, height = 4, font = customFont2, text = H1, command = lambda: self.boardButtonPressed(H1))
        self.btn4.grid(column = 1, row = 2, padx = 3, pady = 3)
        self.btn5 =  Button(gameboard, width = 13, height = 4, font = customFont2, text = LIBRARY, command = lambda: self.boardButtonPressed(LIBRARY))
        self.btn5.grid(column = 1, row = 3, padx = 3, pady = 3)
        self.btn6 =  Button(gameboard, width = 13, height = 4, font = customFont2, text = H2, command = lambda: self.boardButtonPressed(H2))
        self.btn6.grid(column = 1, row = 4, padx = 3, pady = 3)
        self.btn7 =  Button(gameboard, width = 13, height = 4, font = customFont2, text = CONSERVATORY, command = lambda: self.boardButtonPressed(CONSERVATORY))
        self.btn7.grid(column = 1, row = 5, padx = 3, pady = 3)
        self.btn8 =  Button(gameboard, width = 13, height = 4, font = customFont2, text = H3, command = lambda: self.boardButtonPressed(H3))
        self.btn8.grid(column = 2, row = 1, padx = 3, pady = 3)
        self.btn9 =  Button(gameboard, width = 13, height = 4, font = customFont2, text = H4, command = lambda: self.boardButtonPressed(H4))
        self.btn9.grid(column = 2, row = 3, padx = 3, pady = 3)
        self.btn10 = Button(gameboard, width = 13, height = 4, font = customFont2, text = H5, command = lambda: self.boardButtonPressed(H5))
        self.btn10.grid(column = 2, row = 5, padx = 3, pady = 3)
        self.btn11 = Button(gameboard, width = 13, height = 4, font = customFont2, text = MR_GREEN, command = lambda: self.boardButtonPressed(MR_GREEN))
        self.btn11.grid(column = 2, row = 6, padx = 3, pady = 3)
        self.btn12 = Button(gameboard, width = 13, height = 4, font = customFont2, text = HALL, command = lambda: self.boardButtonPressed(HALL))
        self.btn12.grid(column = 3, row = 1, padx = 3, pady = 3)
        self.btn13 = Button(gameboard, width = 13, height = 4, font = customFont2, text = H6, command = lambda: self.boardButtonPressed(H6))
        self.btn13.grid(column = 3, row = 2, padx = 3, pady = 3)
        self.btn14 = Button(gameboard, width = 13, height = 4, font = customFont2, text = BILLIARD_ROOM, wraplength = 60, command = lambda: self.boardButtonPressed(BILLIARD_ROOM))
        self.btn14.grid(column = 3, row = 3, padx = 3, pady = 3)
        self.btn15 = Button(gameboard, width = 13, height = 4, font = customFont2, text = H7, command = lambda: self.boardButtonPressed(H7))
        self.btn15.grid(column = 3, row = 4, padx = 3, pady = 3)
        self.btn16 = Button(gameboard, width = 13, height = 4, font = customFont2, text = BALLROOM, command = lambda: self.boardButtonPressed(BALLROOM))
        self.btn16.grid(column = 3, row = 5, padx = 3, pady = 3)
        self.btn17 = Button(gameboard, width = 13, height = 4, font = customFont2, text = MISS_SCARLET, wraplength = 60, command = lambda: self.boardButtonPressed(MISS_SCARLET))
        self.btn17.grid(column = 4, row = 0, padx = 3, pady = 3)
        self.btn18 = Button(gameboard, width = 13, height = 4, font = customFont2, text = H8, command = lambda: self.boardButtonPressed(H8))
        self.btn18.grid(column = 4, row = 1, padx = 3, pady = 3)
        self.btn19 = Button(gameboard, width = 13, height = 4, font = customFont2, text = H9, command = lambda: self.boardButtonPressed(H9))
        self.btn19.grid(column = 4, row = 3, padx = 3, pady = 3)
        self.btn20 = Button(gameboard, width = 13, height = 4, font = customFont2, text = H10, command = lambda: self.boardButtonPressed(H10))
        self.btn20.grid(column = 4, row = 5, padx = 3, pady = 3)
        self.btn21 = Button(gameboard, width = 13, height = 4, font = customFont2, text = MRS_WHITE, command = lambda: self.boardButtonPressed(MRS_WHITE))
        self.btn21.grid(column = 4, row = 6, padx = 3, pady = 3)
        self.btn22 = Button(gameboard, width = 13, height = 4, font = customFont2, text = LOUNGE, command = lambda: self.boardButtonPressed(LOUNGE))
        self.btn22.grid(column = 5, row = 1, padx = 3, pady = 3)
        self.btn23 = Button(gameboard, width = 13, height = 4, font = customFont2, text = H11, command = lambda: self.boardButtonPressed(H11))
        self.btn23.grid(column = 5, row = 2, padx = 3, pady = 3)
        self.btn24 = Button(gameboard, width = 13, height = 4, font = customFont2, text = DINING_ROOM, wraplength = 60, command = lambda: self.boardButtonPressed(DINING_ROOM))
        self.btn24.grid(column = 5, row = 3, padx = 3, pady = 3)
        self.btn25 = Button(gameboard, width = 13, height = 4, font = customFont2, text = H12, command = lambda: self.boardButtonPressed(H12))
        self.btn25.grid(column = 5, row = 4, padx = 3, pady = 3)
        self.btn26 = Button(gameboard, width = 13, height = 4, font = customFont2, text = KITCHEN, command = lambda: self.boardButtonPressed(KITCHEN))
        self.btn26.grid(column = 5, row = 5, padx = 3, pady = 3)
        self.btn27 = Button(gameboard, width = 13, height = 4, font = customFont2, text = COLONEL_MUSTARD, wraplength = 60, command = lambda: self.boardButtonPressed(COLONEL_MUSTARD))
        self.btn27.grid(column = 6, row = 2, padx = 3, pady = 3)


        cluesheet = ttk.Labelframe(self.gamescreen, text = "Player's Clue Sheet", relief = "sunken", padding = (5,5,5,5))
        whodidit = ttk.Labelframe(cluesheet, text = "Who Did It?", relief = "sunken",  width = 25, height = 25)
        withwhat = ttk.Labelframe(cluesheet, text = "With What Weapon?", relief = "sunken",  width = 25, height = 25)
        where = ttk.Labelframe(cluesheet, text = "Where Did They Do It?", relief = "sunken",  width = 25, height = 25)
        #action_buttons = ttk.Labelframe(cluesheet, text = "Action/Suggestion", relief = "sunken",  width = 25, height = 25)

        #Cluesheet Grid
        whodidit.grid(column = 0, row = 0, pady = 5, sticky = (W))
        #whodidit.grid_propagate(False)
        withwhat.grid(column = 0, row = 1, pady = 5, sticky = (W))
        #withwhat.grid_propagate(False)
        where.grid(column = 0, row = 2, pady = 5, sticky = (W))
        #where.grid_propagate(False)
        #action_buttons.grid(column = 0, row = 3, pady = 15, sticky = (W))

        #Checkbutton Initial Values
        onevar = BooleanVar()
        twovar = BooleanVar()
        threevar = BooleanVar()
        fourvar = BooleanVar()
        fivevar = BooleanVar()
        sixvar = BooleanVar()
        sevenvar = BooleanVar()
        eightvar = BooleanVar()
        ninevar = BooleanVar()
        tenvar = BooleanVar()
        elevenvar = BooleanVar()
        twelvevar = BooleanVar()
        thirteenvar = BooleanVar()
        fourteenvar = BooleanVar()
        fifteenvar = BooleanVar()
        sixteenvar = BooleanVar()
        seventeenvar = BooleanVar()
        eighteenvar = BooleanVar()
        nineteenvar = BooleanVar()
        twentyvar = BooleanVar()
        twentyonevar = BooleanVar()

        weapon = StringVar()
        place = StringVar()

        onevar.set(False)
        twovar.set(False)
        threevar.set(False)
        fourvar.set(False)
        fivevar.set(False)
        sixvar.set(False)
        sevenvar.set(False)
        eightvar.set(False)
        ninevar.set(False)
        tenvar.set(False)
        elevenvar.set(False)
        twelvevar.set(False)
        thirteenvar.set(False)
        fourteenvar.set(False)
        fifteenvar.set(False)
        sixteenvar.set(False)
        seventeenvar.set(False)
        eighteenvar.set(False)
        nineteenvar.set(False)
        twentyvar.set(False)
        twentyonevar.set(False)

        #Checkbuttons

        colmustard = Checkbutton(whodidit,  font = customFont2,text="Colonel Mustard", variable=onevar, onvalue=True)
        profplum = Checkbutton(whodidit,  font = customFont2, text="Professor Plum", variable=twovar, onvalue=True)
        peacock = Checkbutton(whodidit,  font = customFont2,text="Mrs. Peacock", variable=threevar, onvalue=True)
        scarlet = Checkbutton(whodidit,  font = customFont2,text="Miss Scarlet", variable=fourvar, onvalue=True)
        mrgreen = Checkbutton(whodidit,  font = customFont2,text="Mr. Green", variable=fivevar, onvalue=True)
        mrswhite = Checkbutton(whodidit,  font = customFont2,text="Mrs. White", variable=sixvar, onvalue=True)

        pipe = Checkbutton(withwhat,  font = customFont2,text="Lead Pipe", variable=sevenvar, onvalue=True)
        knife = Checkbutton(withwhat,  font = customFont2, text="Knife", variable=eightvar, onvalue=True)
        rope = Checkbutton(withwhat,  font = customFont2,text="Rope", variable=ninevar, onvalue=True)
        pistol = Checkbutton(withwhat, font = customFont2,text="Revolver", variable=tenvar, onvalue=True)
        hammer = Checkbutton(withwhat, font = customFont2, text="Wrench", variable=elevenvar, onvalue=True)
        weapon = Checkbutton(withwhat, font = customFont2, text="Candlestick", variable=twelvevar, onvalue=True)

        study_rb = Checkbutton(where, font = customFont2, text="Study", variable=thirteenvar, onvalue=True)
        hall_rb = Checkbutton(where,  font = customFont2, text="Hall", variable=fourteenvar, onvalue=True)
        lounge_rb = Checkbutton(where,  font = customFont2, text="Lounge", variable=fifteenvar, onvalue=True)
        library_rb = Checkbutton(where,  font = customFont2,text="Library", variable=sixteenvar, onvalue=True)
        billiardroom_rb = Checkbutton(where,  font = customFont2,text="Billiard Room", variable=seventeenvar, onvalue=True)
        diningroom_rb = Checkbutton(where, font = customFont2, text="Dining Room", variable=eighteenvar, onvalue=True)
        conservatory_rb = Checkbutton(where,  font = customFont2,text="Conservatory", variable=nineteenvar, onvalue=True)
        ballroom_rb = Checkbutton(where,  font = customFont2,text="Ballroom", variable=twentyvar, onvalue=True)
        kitchen_rb = Checkbutton(where,  font = customFont2, text="Kitchen", variable=twentyonevar, onvalue=True)

        ###Buttons (Action Buttons)
        ##suggestion = ttk.Button(action_buttons, text = "Make a Suggestion")
        ##accusation = ttk.Button(action_buttons, text = "Make a Accusation")


        #Whodidit Check Buttons Grid
        colmustard.grid(column=0, row=0,sticky=(N,E,W,S),padx = 3, pady = 3)
        profplum.grid(column=0, row=1,sticky=(N,E,W,S),padx = 3, pady = 3)
        peacock.grid(column=0, row=2,sticky=(N,E,W,S),padx = 3, pady = 3)
        scarlet.grid(column=1, row=0,sticky=(N,E,W,S),padx = 3, pady = 3)
        mrgreen.grid(column=1, row=1 ,sticky=(N,E,W,S),padx = 3, pady = 3)
        mrswhite.grid(column=1, row=2,sticky=(N,E,W,S),padx = 3, pady = 3)

        #Withwhat Check Buttons Grid
        pipe.grid(column=0, row=0,sticky=(N,E,W,S), padx = 3, pady = 3) 
        knife.grid(column=0, row=1,sticky=(N,E,W,S), padx = 3, pady = 3) 
        rope.grid(column=0, row=2,sticky=(N,E,W,S), padx = 3, pady = 3) 
        pistol.grid(column=1, row=0,sticky=(N,E,W,S), padx = 3, pady = 3) 
        hammer.grid(column=1, row=1 ,sticky = (N,E,W,S), padx = 3, pady = 3) 
        weapon.grid(column=1, row=2,sticky=(N,E,W,S), padx = 3, pady = 3)

        #Where Check Buttons Grid
        study_rb.grid(column=0, row=0,sticky=(N,E,W,S), padx = 5, pady = 5)
        hall_rb.grid(column=1, row=0, sticky=(N,E,W,S), padx = 5, pady = 5)
        lounge_rb.grid(column=2, row=0,sticky=(N,E,W,S), padx = 5, pady = 5) 
        library_rb.grid(column=0, row=1,sticky=(N,E,W,S), padx = 5, pady = 5)
        billiardroom_rb.grid(column=1, row=1,sticky=(N,E,W,S), padx = 5, pady = 5)
        diningroom_rb.grid(column=2, row=1,sticky=(N,E,W,S), padx = 5, pady = 5)
        conservatory_rb.grid(column=0, row=2,sticky=(N,E,W,S), padx = 5, pady = 5)
        ballroom_rb.grid(column=1, row=2,sticky=(N,E,W,S), padx = 5, pady = 5) 
        kitchen_rb.grid(column=2, row=2,sticky=(N,E,W,S), padx = 5, pady = 5)

        ###Actionbuttons Grid
        ##suggestion.grid(column = 0, row = 0, sticky = (N,E,W,S), padx = 15, pady = 15)
        ##accusation.grid(column = 0, row = 1, sticky = (N,E,W,S), padx = 15, pady = 15)

        notification.grid(row = 0, column = 0, sticky = (N,S,E,W))
        gameboard.grid(row = 2, column = 0, sticky = (N,S,E,W))
        cluesheet.grid(row = 1, column = 0, rowspan = 3, sticky = (E))

        # Initialize Client
        #self.controller.initServer(self.gamescreen)
        #self.controller.initClient(self.gamescreen)
        
        self.updateBoardPieces()
        tksupport.install(self.gamescreen)
        self.gamescreen.mainloop()
        

if __name__ == "__main__":
    gs = GameScreen(None)
    gs.initScreen()
    
                  
