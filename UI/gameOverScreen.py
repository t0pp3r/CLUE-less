from Tkinter import *
import ttk
import itertools
import tkMessageBox
import tkFont

class GameoverScreen:
    def __init__(self, controller):
        self.controller = controller
        self.ipAddress1 = None
        self.ipAddress2 = None
        self.gameoverscreen = None

    def connectionError(self):
        tkMessageBox.showerror(title = "Clue-Less Message:  Connection Error", message = "Sorry, Clue-Less could not connect to <<IP>>.  Please check the IP address port and try again")
        return

    def startGame(self):
            pass

    def aboutGame(self):
            pass

    def initScreen(self): 
        
#---------------------------------------------------------------------------
        self.gameoverscreen = Tk()
        Grid.rowconfigure(self.gameoverscreen, 0, weight = 1)
        Grid.columnconfigure(self.gameoverscreen, 0, weight = 1)
#---------------------------------------------------------------------------
                                                                                #Font
        customFont = tkFont.Font(family = "Helvetica", size=20, weight = 'bold', slant = 'italic')
        customFont1 = tkFont.Font(family = "Helvetica", size=14, weight = 'bold')
        customFont2 = tkFont.Font(family = "Helvetica", size=12, weight = 'bold')
#---------------------------------------------------------------------------
                                                                                #MenuBar
        menubar = Menu(self.gameoverscreen)
        filemenu = Menu(menubar, tearoff = 0)
        filemenu.add_command(label = "Start New Game", command = startGame)

        filemenu.add_separator()

        filemenu.add_command(label = "Quit", command = self.gameoverscreen.quit)
        menubar.add_cascade(label = "File", menu = filemenu)
        helpmenu = Menu(menubar, tearoff = 0)
        helpmenu.add_cascade(label = "Help", command = aboutGame)
        helpmenu.add_cascade(label = "About Game", command = aboutGame)
        menubar.add_cascade(label = "Help", menu = helpmenu)

        self.gameoverscreen.config(menu = menubar)
#------------------------------------------------------------------------------
                                                                                #Frames
        welcome = ttk.Frame(self.gameoverscreen, borderwidth = 5, relief = "flat")
        host = ttk.Frame(self.gameoverscreen, borderwidth = 5, relief = "sunken", width = 500, height = 500)
        join = ttk.Frame(self.gameoverscreen, borderwidth = 5, relief = "sunken", width = 500, height = 500)
        iigLogo = ttk.Frame(self.gameoverscreen)
#------------------------------------------------------------------------------
                                                                                #Labels

        welcomeText = ttk.Label(welcome, text = "Thank You For Playing Clue-Less!", foreground = 'red', font = customFont)
        hostGame = ttk.Label(host, text = "Host A Game", font = customFont1, foreground = 'red')
        joinGame = ttk.Label(join, text = "Join A Game", font = customFont1, foreground = 'red')
        ipLabel1 = ttk.Label(host, font = customFont2, text = "IP Address:")
        portLabel1 = ttk.Label(host, font = customFont2,text = "Port:")
        ipLabel2 = ttk.Label(join, font = customFont2,text = "IP Address:")
        portLabel2 = ttk.Label(join, font = customFont2,text = "Port:")
#------------------------------------------------------------------------------
                                                                                #Entry
        ip = StringVar()
        port = StringVar()

        ipAddress1 = ttk.Entry(host, textvariable = ip)
        portAddress1 = ttk.Entry(host, textvariable = port)

        ipAddress2 = ttk.Entry(join, textvariable = ip)
        portAddress2 = ttk.Entry(join, textvariable = port)
#------------------------------------------------------------------------------
                                                                                #Buttons
        hostButton = Button(host, font = customFont2, text = "Start Game")
        joinButton = Button(join, font = customFont2, text = "Join Game")
#------------------------------------------------------------------------------
                                                                                #IIG Icon
        iigIcon = PhotoImage(file = 'IGG_Icon.gif')
        iigIconLabel = ttk.Label(iigLogo, image = iigIcon)
#------------------------------------------------------------------------------
                                                                                #Geometry Layout Manager
#------------------------------------------------------------------------------
        host.grid(column = 0, row = 1, columnspan = 1, rowspan = 4, sticky = (N,S,E,W), padx = 15, pady = 15)
        join.grid(column = 3, row = 1, columnspan = 1, rowspan = 4, sticky = (N,S,E,W) , padx = 15, pady = 15)
        welcome.grid(column = 0, row = 0, columnspan = 3, rowspan = 1, sticky = (W), padx = 35, pady = 35)
        #welcome.place(relx=0.5, rely=0.5, anchor=NW)
        iigLogo.grid(column = 1, row = 6, rowspan = 1, sticky = (S,W), padx = 5, pady = 5)

        #Labels
        hostGame.grid(column = 0, columnspan = 1, row = 1, sticky = (N,S,E,W), padx = 5, pady = 5)
        joinGame.grid(column = 0, columnspan = 1, row = 1, sticky = (N,S,E,W), padx = 5, pady = 5)
        #welcomeText.place(relx=0.5, rely=0.5, anchor=CENTER)
        welcomeText.grid(column = 0, row = 1, sticky = (N,S,E,W))
#------------------------------------------------------------------------------
                                                                                #Host Frame
        #Labels
        ipLabel1.grid(column = 0, row = 2, sticky = (N,W), padx = 5, pady = 5)
        portLabel1.grid(column = 0, row = 4, sticky = (N,W), padx = 5, pady = 5)
        #Entry Boxes
        ipAddress1.grid(column = 2, row = 2, sticky = (N,W), padx = 5, pady = 5)
        portAddress1.grid(column = 2, row = 4, sticky = (N,W), padx = 5, pady = 5)
#------------------------------------------------------------------------------
                                                                                #Join Game
        #Labels
        ipLabel2.grid(column = 0, row = 2, sticky = (N,W), padx = 5, pady = 5)
        portLabel2.grid(column = 0, row = 4, sticky = (N,W), padx = 5, pady = 5)
        #Entry Boxes
        ipAddress2.grid(column = 2, row = 2, sticky = (N,W), padx = 5, pady = 5)
        portAddress2.grid(column = 2, row = 4, sticky = (N,W), padx = 5, pady = 5)
#------------------------------------------------------------------------------
                                                                                #IIG Image
        iigIconLabel.grid(column = 0, row = 6, sticky = (W))
#------------------------------------------------------------------------------
        #Buttons
        hostButton.grid(column = 2, row = 5, sticky = (W,S), padx = 5, pady = 5)
        joinButton.grid(column = 2, row = 5, sticky = (W,S), padx = 5, pady = 5)

        self.gameoverscreen.mainloop()

if __name__ == "__main__":
    go = GameoverScreen(None)
