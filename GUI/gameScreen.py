from Tkinter import *
import ttk
import itertools
import tkMessageBox
import tkFont
#-------------------------------------------------------------------------------
                                        #Dialog Box Functions:
def yourTurn():
    tkMessageBox.showinfo(title = "Clue-Less Message: Your Turn", message = "<<Player>>, it is now your turn")

def connectionError():
    tkMessageBox.showerror(title = "Clue-Less Message:  Connection Error", message = "Sorry, Clue-Less could not connect to <<IP>>.  Please check the IP address port and try again")

def hallwaysBlocked():
    tkMessageBox.showinfo(title = "Clue-Less Message:  Lose Turn", message = "<<Player>>, all hallways are blocked.  Your only option is to make an Accusation.")

def disproveSuggestion():
    tkMessageBox.askyesno(title = "Clue-Less Message:  Disprove Suggestion", message = "<<Player>>, <<Player>> made a suggestion of:  <<Suspect>> in <<Room>> with a <<Weapon>>.  Can you disprove this?")

def disproveSuggFalse():
    tkMessageBox.showinfo(title = "Clue-Less Message:  Disprove Suggestion", message = "<<Player>>, your card could not disprove <<Player>> suggestion.")

def disproveSuggTrue():
    tkMessageBox.showinfo(title = "Clue-Less Message:  Suggestion Disproved", message = "<<Player>>, your suggestion has been disproved by <<Player>> with the <<card>>")

def accusationFalse():
    tkMessageBox.showinfo(title = "Clue-Less Message:  Accusation", message = "<<Player>>, you accused <<Suspect>> in <<Room>> with a <<Weapon>>.  Your answer was incorrect.  Sorry this is the end of the game for you.")
    
def gameover():
    tkMessageBox.showinfo(title = "Clue-Less Message:  Game Over", message = "<<Player>> has solved the mystery with a correct accusation!  It was <<Suspect>> in the <<Room>> with a <<Weapon>>.  Better luck next time!")
    
#------------------------------------------------------------------------------

gamescreen = Tk()
Grid.rowconfigure(gamescreen,0,weight=1)
Grid.columnconfigure(gamescreen,0,weight=1)

#------------------------------------------------------------------------------
                                                #Menu Bar
def startGame():
    pass
def aboutGame():
    pass
menubar = Menu(gamescreen)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = "Start New Game", command = startGame)

filemenu.add_separator()

filemenu.add_command(label = "Quit", command = gamescreen.quit)
menubar.add_cascade(label = "File", menu = filemenu)

helpmenu = Menu(menubar, tearoff = 0)
helpmenu.add_cascade(label = "Help", command = aboutGame)
helpmenu.add_cascade(label = "About Game", command = aboutGame)
menubar.add_cascade(label = "Help", menu = helpmenu)

gamescreen.config(menu = menubar)

#------------------------------------------------------------------------------
                                                    #Fonts
customFont = tkFont.Font(family = "Helvetica", size=24, weight = 'bold', slant = 'italic', )
customFont1 = tkFont.Font(family = "Helvetica", size=18, weight = 'bold')
customFont2 = tkFont.Font(family = "Helvetica", size= 8, weight = 'bold')
#------------------------------------------------------------------------------
                                                    #Frames
notification = ttk.Frame(gamescreen, padding = (5,5,5,5))
notif_board = ttk.Labelframe(notification, text = "Notification Board", borderwidth = 5, relief = "sunken", width = 300, height = 150)
sugg_board = ttk.Labelframe(notification, text = "Suggestion Board", borderwidth = 5, relief = "sunken", width = 300, height = 150)
player_info = ttk.Labelframe(notification, text = "Player Info", borderwidth = 5, relief = "sunken", width = 300, height = 150)

notiftextbox = Text(notif_board, height = 100, width = 50, wrap = "word")
notiftextbox.insert(INSERT, "This is where we display each players moves.")
sugghistbox = Text(sugg_board, height = 100, width = 50, wrap = "word")
sugghistbox.insert(INSERT, "This is where we display the suggestion history.")
playerinfobox = Text(player_info, height = 100, width = 50, wrap = "word")
playerinfobox.insert(INSERT, "This is where we display each players info.")

notiftextbox.grid(column = 0, row = 0, sticky = (N,E,W),padx =5, pady = 5)
sugghistbox.grid(column=1, row=0, sticky = (N,E,W), padx = 5, pady = 5)
playerinfobox.grid(column=2, row=0, sticky = (N,E,W), padx = 5, pady = 5)

notif_board.grid(column = 0, row = 0, sticky = (N,W),padx = 5, pady = 5)
notif_board.grid_propagate(False)
sugg_board.grid(column=1, row=0, sticky = (N), padx = 5, pady = 5)
sugg_board.grid_propagate(False) 
player_info.grid(column=2, row=0, sticky = (N,E,W,S), padx = 5, pady = 5)
player_info.grid_propagate(False)
#------------------------------------------------------------------------------
gameboard = ttk.Labelframe(gamescreen, padding = (8,8,8,8), text = "Gameboard", relief = "sunken")

#these buttons will not be displayed on the gameboard b/c they do not have any labels (room, hallway, starting space)
forgetButtons = [0,1,3,5,6,7,13,14,16,18,21,27,30,32,35,41,42,43,45,46,47,48]

#this list tracks all the buttons on the gameboard
buttonNames = ["Prof. Plum", "Mrs. Peacock", "Study", "Hallway 1", "Library", "Hallway 2", "Conservatory", "Hallway 3", "Hallway 4", "Hallway 5", "Mr. Green", "Hall",
               "Hallway 6", "Billiard", "Hallway 7", "Ballroom", "Miss Scarlet", "Hallway 8", "Hallway 9", "Hallway 10", "Mrs. White", "Lounge", "Hallway 11", "Dining Room",
               "Hallway 12", "Kitchen", "Col. Mustard"]

myButtons = []
count = 0
for x, y in itertools.product(range(7), repeat=2):
    if not x*7 + y in forgetButtons:
            btn = Button(gameboard, width=9, height=4, font = customFont2, text=buttonNames[count])
            btn.grid(column=x, row=y, padx=3, pady=3)
            myButtons.append(btn)
            count = count + 1
               
#----------------------------------------------------------------------------------------------------------
cluesheet = ttk.Labelframe(gamescreen, text = "Player's Clue Sheet", relief = "sunken", padding = (5,5,5,5))
whodidit = ttk.Labelframe(cluesheet, text = "Who Did It?", relief = "sunken",  width = 25, height = 25)
withwhat = ttk.Labelframe(cluesheet, text = "With What Weapon?", relief = "sunken",  width = 25, height = 25)
where = ttk.Labelframe(cluesheet, text = "Where Did They Do It?", relief = "sunken",  width = 25, height = 25)
action_buttons = ttk.Labelframe(cluesheet, text = "Action/Suggestion", relief = "sunken",  width = 25, height = 25)

#Cluesheet Grid
whodidit.grid(column = 0, row = 0, pady = 5, sticky = (W))
#whodidit.grid_propagate(False)
withwhat.grid(column = 0, row = 1, pady = 5, sticky = (W))
#withwhat.grid_propagate(False)
where.grid(column = 0, row = 2, pady = 5, sticky = (W))
#where.grid_propagate(False)
action_buttons.grid(column = 0, row = 3, pady = 15, sticky = (W))

#Checkbutton Initial Values
onevar = BooleanVar()
twovar = BooleanVar()
threevar = BooleanVar()
fourvar = BooleanVar()
fivevar = BooleanVar()
sixvar = BooleanVar()

weapon = StringVar()
place = StringVar()

onevar.set(True)
twovar.set(False)
threevar.set(True)
fourvar.set(True)
fivevar.set(False)
sixvar.set(True)

                                            #Checkbuttons
colmustard = Checkbutton(whodidit,  font = customFont2,text="Colonel Mustard", variable=onevar, onvalue=True)
profplum = Checkbutton(whodidit,  font = customFont2, text="Professor Plum", variable=twovar, onvalue=True)
peacock = Checkbutton(whodidit,  font = customFont2,text="Mrs. Peacock", variable=threevar, onvalue=True)
scarlet = Checkbutton(whodidit,  font = customFont2,text="Miss Scarlet", variable=fourvar, onvalue=True)
mrgreen = Checkbutton(whodidit,  font = customFont2,text="Mr. Green", variable=fivevar, onvalue=True)
mrswhite = Checkbutton(whodidit,  font = customFont2,text="Mrs. White", variable=sixvar, onvalue=True)


pipe = Checkbutton(withwhat,  font = customFont2,text="Lead Pipe", variable=onevar, onvalue=True)
knife = Checkbutton(withwhat,  font = customFont2, text="Knife", variable=onevar, onvalue=True)
rope = Checkbutton(withwhat,  font = customFont2,text="Rope", variable=onevar, onvalue=True)
pistol = Checkbutton(withwhat, font = customFont2,text="Revolver", variable=onevar, onvalue=True)
hammer = Checkbutton(withwhat, font = customFont2, text="Wrench", variable=onevar, onvalue=True)
weapon = Checkbutton(withwhat, font = customFont2, text="Candlestick", variable=onevar, onvalue=True)

study_rb = Checkbutton(where, font = customFont2, text="Study", variable=onevar, onvalue=True)
hall_rb = Checkbutton(where,  font = customFont2, text="Hall", variable=onevar, onvalue=True)
lounge_rb = Checkbutton(where,  font = customFont2, text="Lounge", variable=onevar, onvalue=True)
library_rb = Checkbutton(where,  font = customFont2,text="Library", variable=onevar, onvalue=True)
billiardroom_rb = Checkbutton(where,  font = customFont2,text="Billiard Room", variable=onevar, onvalue=True)
diningroom_rb = Checkbutton(where, font = customFont2, text="Dining Room", variable=onevar, onvalue=True)
conservatory_rb = Checkbutton(where,  font = customFont2,text="Conservatory", variable=onevar, onvalue=True)
ballroom_rb = Checkbutton(where,  font = customFont2,text="Ballroom", variable=onevar, onvalue=True)
kitchen_rb = Checkbutton(where,  font = customFont2, text="Kitchen", variable=onevar, onvalue=True)

#Buttons (Action Buttons)
suggestion = ttk.Button(action_buttons, text = "Make a Suggestion")
accusation = ttk.Button(action_buttons, text = "Make a Accusation")

#-----------------------------------------------------------------------------------------------------------
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

#Actionbuttons Grid
suggestion.grid(column = 0, row = 0, sticky = (N,E,W,S), padx = 15, pady = 15)
accusation.grid(column = 0, row = 1, sticky = (N,E,W,S), padx = 15, pady = 15)




#-----------------------------------------------------------------------------------------------------------

notification.grid(row = 0, column = 0, sticky = (N,S,E,W))
gameboard.grid(row = 2, column = 0, sticky = (N,S,E,W))
cluesheet.grid(row = 1, column = 0, rowspan = 3, sticky = (E))

gamescreen.mainloop()


                  
