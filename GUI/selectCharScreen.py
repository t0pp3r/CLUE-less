from Tkinter import *
import ttk
import itertools
import tkMessageBox
import tkFont

#----------------------------------------------------------------------------
                            #Dialog Box Functions:

def connectionError():
    tkMessageBox.showerror(title = "Clue-Less Message:  Connection Error", message = "Sorry, Clue-Less could not connect to <<IP>>.  Please check the IP address port and try again")
    return
#---------------------------------------------------------------------------
selectcharscreen = Tk()
selectcharscreen.title("Select A Character")
Grid.rowconfigure(selectcharscreen, 0, weight = 1)
Grid.columnconfigure(selectcharscreen, 0, weight = 1)

#---------------------------------------------------------------------------
                                #Font
customFont = tkFont.Font(family = "Helvetica", size=24, weight = 'bold', slant = 'italic', )
customFont1 = tkFont.Font(family = "Helvetica", size=18, weight = 'bold')
customFont2 = tkFont.Font(family = "Helvetica", size=12, weight = 'bold')
#---------------------------------------------------------------------------
                                #MenuBar

def startGame():
    pass
def aboutGame():
    pass
menubar = Menu(selectcharscreen)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = "Start New Game", command = startGame)

filemenu.add_separator()

filemenu.add_command(label = "Quit", command = selectcharscreen.quit)
menubar.add_cascade(label = "File", menu = filemenu)

helpmenu = Menu(menubar, tearoff = 0)
helpmenu.add_cascade(label = "Help", command = aboutGame)
helpmenu.add_cascade(label = "About Game", command = aboutGame)
menubar.add_cascade(label = "Help", menu = helpmenu)

selectcharscreen.config(menu = menubar)
#------------------------------------------------------------------------------
                                #Frames
welcome = ttk.Frame(selectcharscreen, borderwidth = 5, relief = "flat")
enterName = ttk.Frame(selectcharscreen, borderwidth = 5)
selChar = ttk.Frame(selectcharscreen, borderwidth = 5, relief = "sunken")
#------------------------------------------------------------------------------
                                #Labels
welcomeText = ttk.Label(welcome, text = "Welcome To Clue-Less!", foreground = 'red', font = customFont)
enterNameLabel = ttk.Label(enterName, text = "Enter Your Name:", font = customFont1, foreground = 'red')
selCharLabel = ttk.Label(selChar, text = "Select A Character:", font = customFont1, foreground = 'red')
#------------------------------------------------------------------------------
                                #Entry
playerName = StringVar()                     
enterNameEntry = ttk.Entry(enterName, width = 40, textvariable = playerName)                     
#------------------------------------------------------------------------------
#Instantiation and Grid Layout for widgets in selChar Frame (Labels/Buttons)
#------------------------------------------------------------------------------
#this list contains the image files that will sit on each button 
charImage = ["RED_Scarlet.gif", "WHITE_White.gif", "YELLOW_Mustard.gif", "PINK_Peacock.gif", "GREEN_Green.gif", "BLUE_Plum.gif"]
#this list contains the labels that will sit above each player's button icon
charLabels = ["Miss Scarlet", "Mrs. White", "Col. Mustard", "Mrs. Peacock", "Mr. Green", "Prof. Plum"]
myCharIconList = []
myCharLabelList = []
myCharBtnList = []

for x in range(6):
    selLabel = ttk.Label(selChar, text = charLabels[x], font = customFont1)
    selLabel.grid(column = x, row = 4, padx = 5, pady = 5)
    myCharLabelList.append(selLabel)
    charIcon = PhotoImage(file = charImage[x])
    myCharIconList.append(charIcon)
    charBtn = Button(selChar, image = myCharIconList[x])
    charBtn.grid(column = x, row = 5, sticky = (N,E,W,S), rowspan = 2, padx = 5, pady = 5)
    myCharBtnList.append(charBtn)
    

#------------------------------------------------------------------------------
                                #IIG Icon
iigIcon = PhotoImage(file = 'IGG_Icon.gif')
iigIconLabel = ttk.Label(selectcharscreen, image = iigIcon)

#------------------------------------------------------------------------------
#Geometry Layout Manager
#------------------------------------------------------------------------------
welcome.grid(column = 0, row = 0, columnspan = 3, rowspan = 2, sticky = (N,S,W,E), padx = 10, pady = 10)
enterName.grid(column = 0, row = 3, rowspan = 2, sticky = (N,S,E,W), padx = 10, pady = 10)
selChar.grid(column = 0, row = 6, rowspan = 4, columnspan = 5, sticky = (N,S,E,W), padx = 10, pady = 10)
#------------------------------------------------------------------------------
#Labels
welcomeText.grid(column = 2, row = 0, sticky = (W))
enterNameLabel.grid(column = 2, row = 1, columnspan = 2, sticky = (N,S,E,W), padx = 10, pady = 10)
selCharLabel.grid(column = 2, row = 3, columnspan = 3, sticky = (N,S,E,W), padx = 10, pady = 10)
#------------------------------------------------------------------------------
#Entry
enterNameEntry.grid(column = 5, row = 1, columnspan = 1, sticky = (E), padx = 5, pady = 5)
#------------------------------------------------------------------------------
                                #IIG Image
iigIconLabel.grid(column = 5, row = 0, sticky = (E), padx = 5, pady = 5)
#------------------------------------------------------------------------------

selectcharscreen.mainloop()

