from Tkinter import *
import ttk
import itertools
import tkMessageBox
import tkFont
import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from Constants import *

class SelectCharScreen:
    def __init__(self, controller):
        self.controller = controller
        self.selectcharscreen = None
        self.name = None
        self.char = None
        self.enterNameEntry = None

    def connectionError(self):
        tkMessageBox.showerror(title = "Clue-Less Message:  Connection Error", message = "Sorry, Clue-Less could not connect to <<IP>>.  Please check the IP address port and try again")
        return

    def startGame(self):
        pass
    
    def aboutGame(self):
        pass

    def selectCharacterButton(self, char):
        if self.controller.isCharAvailable(char) and self.enterNameEntry.get() != "":
            self.controller.character = char
            self.controller.player = self.enterNameEntry.get()
            self.controller.addPlayer(self.enterNameEntry.get(), char)
            self.selectcharscreen.destroy()
        elif self.enterNameEntry.get() == "":
            tkMessageBox.showerror(title = "Clue-Less Message:  Error", message = "Please enter your name in the text box.")
        else:
            tkMessageBox.showerror(title = "Clue-Less Message:  Error", message = "Sorry, %s has already been selected. Please choose again." % char)
        print "button"
        

    def initScreen(self):
        #Parent Frame
        self.selectcharscreen = Tk()
        self.selectcharscreen.title("Select A Character")
        Grid.rowconfigure(self.selectcharscreen, 0, weight = 1)
        Grid.columnconfigure(self.selectcharscreen, 0, weight = 1)

        #Font
        customFont = tkFont.Font(family = "Helvetica", size=24, weight = 'bold', slant = 'italic', )
        customFont1 = tkFont.Font(family = "Helvetica", size=18, weight = 'bold')
        customFont2 = tkFont.Font(family = "Helvetica", size=12, weight = 'bold')

        #MenuBar
        menubar = Menu(self.selectcharscreen)
        filemenu = Menu(menubar, tearoff = 0)
        filemenu.add_command(label = "Start New Game", command = self.startGame)

        filemenu.add_separator()

        filemenu.add_command(label = "Quit", command = self.selectcharscreen.quit)
        menubar.add_cascade(label = "File", menu = filemenu)

        helpmenu = Menu(menubar, tearoff = 0)
        helpmenu.add_cascade(label = "Help", command = self.aboutGame)
        helpmenu.add_cascade(label = "About Game", command = self.aboutGame)
        menubar.add_cascade(label = "Help", menu = helpmenu)

        self.selectcharscreen.config(menu = menubar)

        #Frames
        welcome = ttk.Frame(self.selectcharscreen, borderwidth = 5, relief = "flat")
        enterName = ttk.Frame(self.selectcharscreen, borderwidth = 5)
        selChar = ttk.Frame(self.selectcharscreen, borderwidth = 5, relief = "sunken")

        #Labels
        welcomeText = ttk.Label(welcome, text = "Welcome To Clue-Less!", foreground = 'red', font = customFont)
        enterNameLabel = ttk.Label(enterName, text = "Enter Your Name:", font = customFont1, foreground = 'red')
        selCharLabel = ttk.Label(selChar, text = "Select A Character:", font = customFont1, foreground = 'red')

        #Entry
        playerName = StringVar()                     
        self.enterNameEntry = ttk.Entry(enterName, width = 40, textvariable = playerName)                     

        #Instantiation and Grid Layout for widgets in selChar Frame (Labels/Buttons)

        #this list contains the image files that will sit on each button 
        charImage = ["GUI\RED_Scarlet.gif", "GUI\WHITE_White.gif", "GUI\YELLOW_Mustard.gif", "GUI\PINK_Peacock.gif", "GUI\GREEN_Green.gif", "GUI\BLUE_Plum.gif"]
        #this list contains the labels that will sit above each player's button icon
        charLabels = ["Miss Scarlet", "Mrs. White", "Col. Mustard", "Mrs. Peacock", "Mr. Green", "Prof. Plum"]
        myCharIconList = []
        myCharLabelList = []
        myCharBtnList = []

        #for x in range(6):

        # Miss Scarlet Button
        selLabel = ttk.Label(selChar, text = MISS_SCARLET, font = customFont1)
        selLabel.grid(column = 0, row = 4, padx = 5, pady = 5)
        myCharLabelList.append(selLabel)
        charIcon = PhotoImage(file = charImage[0])
        myCharIconList.append(charIcon)
        charBtn = Button(selChar, image = myCharIconList[0], command= lambda:self.selectCharacterButton(MISS_SCARLET))
        charBtn.grid(column = 0, row = 5, sticky = (N,E,W,S), rowspan = 2, padx = 5, pady = 5)
        myCharBtnList.append(charBtn)

        # Mrs White Button
        selLabel = ttk.Label(selChar, text = MRS_WHITE, font = customFont1)
        selLabel.grid(column = 1, row = 4, padx = 5, pady = 5)
        myCharLabelList.append(selLabel)
        charIcon = PhotoImage(file = charImage[1])
        myCharIconList.append(charIcon)
        charBtn = Button(selChar, image = myCharIconList[1], command= lambda:self.selectCharacterButton(MRS_WHITE))
        charBtn.grid(column = 1, row = 5, sticky = (N,E,W,S), rowspan = 2, padx = 5, pady = 5)
        myCharBtnList.append(charBtn)

        # Colonel Mustard Button
        selLabel = ttk.Label(selChar, text = COLONEL_MUSTARD, font = customFont1)
        selLabel.grid(column = 2, row = 4, padx = 5, pady = 5)
        myCharLabelList.append(selLabel)
        charIcon = PhotoImage(file = charImage[2])
        myCharIconList.append(charIcon)
        charBtn = Button(selChar, image = myCharIconList[2], command= lambda:self.selectCharacterButton(COLONEL_MUSTARD))
        charBtn.grid(column = 2, row = 5, sticky = (N,E,W,S), rowspan = 2, padx = 5, pady = 5)
        myCharBtnList.append(charBtn)

        # Mrs. Peacock Button
        selLabel = ttk.Label(selChar, text = MRS_PEACOCK, font = customFont1)
        selLabel.grid(column = 3, row = 4, padx = 5, pady = 5)
        myCharLabelList.append(selLabel)
        charIcon = PhotoImage(file = charImage[3])
        myCharIconList.append(charIcon)
        charBtn = Button(selChar, image = myCharIconList[3], command= lambda:self.selectCharacterButton(MRS_PEACOCK))
        charBtn.grid(column = 3, row = 5, sticky = (N,E,W,S), rowspan = 2, padx = 5, pady = 5)
        myCharBtnList.append(charBtn)

        # Mr. Green Button
        selLabel = ttk.Label(selChar, text = MR_GREEN, font = customFont1)
        selLabel.grid(column = 4, row = 4, padx = 5, pady = 5)
        myCharLabelList.append(selLabel)
        charIcon = PhotoImage(file = charImage[4])
        myCharIconList.append(charIcon)
        charBtn = Button(selChar, image = myCharIconList[4], command= lambda:self.selectCharacterButton(MR_GREEN))
        charBtn.grid(column = 4, row = 5, sticky = (N,E,W,S), rowspan = 2, padx = 5, pady = 5)
        myCharBtnList.append(charBtn)

        # Professor Plum Button
        selLabel = ttk.Label(selChar, text = PROFESSOR_PLUM, font = customFont1)
        selLabel.grid(column = 5, row = 4, padx = 5, pady = 5)
        myCharLabelList.append(selLabel)
        charIcon = PhotoImage(file = charImage[5])
        myCharIconList.append(charIcon)
        charBtn = Button(selChar, image = myCharIconList[5], command= lambda:self.selectCharacterButton(PROFESSOR_PLUM))
        charBtn.grid(column = 5, row = 5, sticky = (N,E,W,S), rowspan = 2, padx = 5, pady = 5)
        myCharBtnList.append(charBtn)

        #IIG Icon
        iigIcon = PhotoImage(file = 'GUI\IGG_Icon.gif')
        iigIconLabel = ttk.Label(self.selectcharscreen, image = iigIcon)

        #Geometry Layout Manager
        welcome.grid(column = 0, row = 0, columnspan = 3, rowspan = 2, sticky = (N,S,W,E), padx = 10, pady = 10)
        enterName.grid(column = 0, row = 3, rowspan = 2, sticky = (N,S,E,W), padx = 10, pady = 10)
        selChar.grid(column = 0, row = 6, rowspan = 4, columnspan = 5, sticky = (N,S,E,W), padx = 10, pady = 10)

        #Labels
        welcomeText.grid(column = 2, row = 0, sticky = (W))
        enterNameLabel.grid(column = 2, row = 1, columnspan = 2, sticky = (N,S,E,W), padx = 10, pady = 10)
        selCharLabel.grid(column = 2, row = 3, columnspan = 3, sticky = (N,S,E,W), padx = 10, pady = 10)

        #Entry
        self.enterNameEntry.grid(column = 5, row = 1, columnspan = 1, sticky = (E), padx = 5, pady = 5)

                                        #IIG Image
        iigIconLabel.grid(column = 5, row = 0, sticky = (E), padx = 5, pady = 5)

        self.selectcharscreen.mainloop()

if __name__ == "__main__":
    scs = SelectCharScreen(None)
    scs.initScreen()
