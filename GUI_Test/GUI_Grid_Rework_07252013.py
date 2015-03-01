from Tkinter import *
import ttk
import itertools


root = Tk()
Grid.rowconfigure(root,0,weight=1)
Grid.columnconfigure(root,0,weight=1)

#------------------------------------------------------------------------------
#Menu Bar
def startGame():
    pass
def aboutGame():
    pass
menubar = Menu(root)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = "Start New Game", command = startGame)

filemenu.add_separator()

filemenu.add_command(label = "Quit", command = root.quit)
menubar.add_cascade(label = "File", menu = filemenu)

helpmenu = Menu(menubar, tearoff = 0)
helpmenu.add_cascade(label = "Help", command = aboutGame)
helpmenu.add_cascade(label = "About Game", command = aboutGame)
menubar.add_cascade(label = "Help", menu = helpmenu)

root.config(menu = menubar)

#------------------------------------------------------------------------------

notification = ttk.Frame(root, padding = (5,5,5,5))
notif_board = ttk.Labelframe(notification, text = "Notification Board", borderwidth = 5, relief = "sunken", width = 300, height = 150)
sugg_board = ttk.Labelframe(notification, text = "Suggestion Board", borderwidth = 5, relief = "sunken", width = 300, height = 150)
player_info = ttk.Labelframe(notification, text = "Player Info", borderwidth = 5, relief = "sunken", width = 300, height = 150)

notiftextbox = Text(notif_board, height = 100, width = 40, wrap = "word")
notiftextbox.insert(INSERT, "This is where we display each players moves.")
sugghistbox = Text(sugg_board, height = 100, width = 40, wrap = "word")
sugghistbox.insert(INSERT, "This is where we display the suggestion history.")
playerinfobox = Text(player_info, height = 100, width = 40, wrap = "word")
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
gameboard = ttk.Labelframe(root, padding = (8,8,8,8), text = "Gameboard", relief = "sunken")
#these buttons will not be displayed on the gameboard b/c they do not have any labels (room, hallway, starting space)
forgetButtons = [0,1,3,5,6,7,13,14,16,18,21,27,30,32,35,41,42,43,45,46,47,48]
#this list tracks all the buttons on the gameboard
myButtons = []
count = 0
for x, y in itertools.product(range(7), repeat=2):
    if not x*7 + y in forgetButtons:
        btn = Button(gameboard, width=7, height=4, text="Room%d\none\ntwo\nfour\nfive" % x)
        btn.grid(column=x, row=y, padx=3, pady=3)
        myButtons.append(btn)
          
        btn.config(text="Room%d\none\ntwo\nfour\nfive" % x)
        
##for x in range(5):
##  Grid.columnconfigure(gameboard,x,weight=1)  
##for y in range(5):
##  Grid.rowconfigure(gameboard,y,weight=1)

#----------------------------------------------------------------------------------------------------------
cluesheet = ttk.Frame(root, padding = (5,5,5,5))
whodidit = ttk.Labelframe(cluesheet, text = "Who Did It?", relief = "sunken",  width = 25, height = 25)
withwhat = ttk.Labelframe(cluesheet, text = "With What Weapon?", relief = "sunken",  width = 25, height = 25)
where = ttk.Labelframe(cluesheet, text = "Where Did They Do It?", relief = "sunken",  width = 25, height = 25)
action_buttons = ttk.Labelframe(cluesheet, text = "Action/Suggestion", relief = "sunken",  width = 25, height = 25)

#Cluesheet Grid
whodidit.grid(column = 0, row = 0, pady = 5, sticky = (W))
#whodidit.grid_propagate(False)
withwhat.grid(column = 0, row = 1, pady = 5, sticky = (W))
#withwhat.grid_propagate(False)
where.grid(column = 0, row = 2, pady = 5, sticky = (W)  )
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
colmustard = ttk.Checkbutton(whodidit, text="Colonel Mustard", variable=onevar, onvalue=True)
profplum = ttk.Checkbutton(whodidit, text="Professor Plum", variable=twovar, onvalue=True)
peacock = ttk.Checkbutton(whodidit, text="Mrs. Peacock", variable=threevar, onvalue=True)
scarlet = ttk.Checkbutton(whodidit, text="Miss Scarlet", variable=fourvar, onvalue=True)
mrgreen = ttk.Checkbutton(whodidit, text="Mr. Green", variable=fivevar, onvalue=True)
mrswhite = ttk.Checkbutton(whodidit, text="Mrs. White", variable=sixvar, onvalue=True)

#RadioButtons
pipe = ttk.Radiobutton(withwhat, text="Pipe", variable=weapon)
knife = ttk.Radiobutton(withwhat, text="Knife", variable=weapon)
rope = ttk.Radiobutton(withwhat, text="Rope", variable=weapon)
pistol = ttk.Radiobutton(withwhat, text="Pistol", variable=weapon)
hammer = ttk.Radiobutton(withwhat, text="Hammer", variable=weapon)
weapon = ttk.Radiobutton(withwhat, text="Weapon", variable=weapon)

study_rb = ttk.Radiobutton(where, text="Study", variable=place)
hall_rb = ttk.Radiobutton(where, text="Hall", variable=place)
lounge_rb = ttk.Radiobutton(where, text="Lounge", variable=place)
library_rb = ttk.Radiobutton(where, text="Library", variable=place)
billiardroom_rb = ttk.Radiobutton(where, text="Billiard Room", variable=place)
diningroom_rb = ttk.Radiobutton(where, text="Dining Room", variable=place)
conservatory_rb = ttk.Radiobutton(where, text="Conservatory", variable=place)
ballroom_rb = ttk.Radiobutton(where, text="Ballroom", variable=place)
kitchen_rb = ttk.Radiobutton(where, text="Kitchen", variable=place)

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

#Withwhat Radio Buttons Grid
pipe.grid(column=0, row=0,sticky=(N,E,W,S), padx = 3, pady = 3) 
knife.grid(column=0, row=1,sticky=(N,E,W,S),padx = 3, pady = 3) 
rope.grid(column=0, row=2,sticky=(N,E,W,S),padx = 3, pady = 3) 
pistol.grid(column=1, row=0,sticky=(N,E,W,S),padx = 3, pady = 3) 
hammer.grid(column=1, row=1 ,sticky = (N,E,W,S),padx = 3, pady = 3) 
weapon.grid(column=1, row=2,sticky=(N,E,W,S),padx = 3, pady = 3)

#Where Radio Buttons Grid
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
gameboard.grid(row = 2, column = 0, sticky = (E,W))
cluesheet.grid(row = 1, column = 1, rowspan = 3, sticky = (N,S,E,W))

root.mainloop()


                  
