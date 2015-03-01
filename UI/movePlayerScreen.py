from Tkinter import *
import ttk
import itertools
import tkMessageBox
import tkFont

class MovePlayerScreen:
    def __init__(self, controller):
        self.controller = controller
        self.movePlayer = None
        self.locationComboBox = None

    def okButtonPressed(self):
        if self.locationComboBox.get() == "":
            tkMessageBox.showerror(title = "Clue-Less Message:  Input Error", message = "Please select an option for all drop down boxes.")
        else:
            self.controller.movePlayer(self.controller.player, self.locationComboBox.get())
            self.controller.sendPlayerMoveMessage()
            self.controller.gui.updateGameBoard()
            self.movePlayer.destroy()
            

    def initScreen(self):
        self.movePlayer = Tk()
        self.movePlayer.title("Clue-Less Message: Move Player")
        #---------------------------------------------------------------------------
                                        #Font
        customFont = tkFont.Font(family = "Helvetica", size=24, weight = 'bold', slant = 'italic')
        customFont1 = tkFont.Font(family = "Helvetica", size=12, weight = 'bold')
        #---------------------------------------------------------------------------
                                       #Parent Frame
        moveLabel = ttk.Frame(self.movePlayer, borderwidth = 5)
        moveComboAndBtn = ttk.Frame(self.movePlayer, borderwidth = 5)
        #---------------------------------------------------------------------------
                                        #Label
        movePlayerLabel = Label(moveLabel, text = "Please select the location you would like to move to.\n\nYour location: %s" % self.controller.getMyLocation(),
                                font = customFont1, foreground = 'black', wraplength = 400, justify = CENTER)

        locationLabel = Label(moveComboAndBtn, text = "Location:", font = customFont1, foreground = 'red')
        #---------------------------------------------------------------------------                        
                                        #Buttons
        moveOkBtn = Button(moveComboAndBtn, text = "OK", font = customFont1, command = self.okButtonPressed)
        #---------------------------------------------------------------------------
                                        #ComboBoxes
        playervar = StringVar()
        locations = self.controller.getValidLocationsToMoveTo(self.controller.player)
        self.locationComboBox = ttk.Combobox(moveComboAndBtn, values = locations, state = 'readonly', font = customFont1)

        #---------------------------------------------------------------------------
                                        #IIG Icon
        #iigIcon = PhotoImage(file = 'GUI\IGG_Icon.gif')
        #iigIconLabel = ttk.Label(self.movePlayer, image = iigIcon)
        #---------------------------------------------------------------------------
                                    #Grid Layout Manager
        #---------------------------------------------------------------------------
        #Frames
        moveLabel.grid(column = 0, row = 0, columnspan = 3, sticky = (E,W))
        moveComboAndBtn.grid(column = 0, row = 2, sticky = (N,W))

        #Icons
        #iigIconLabel.grid(column = 4, row = 0, sticky = (E), padx = 5, pady = 5)
        #Labels
        movePlayerLabel.grid(column = 1, row = 0, sticky = (N))
        locationLabel.grid(column = 0, row = 0, sticky = (S,E,W), padx = 5, pady = 5)
        #Buttons
        moveOkBtn.grid(column = 4, row = 1, sticky = (E),padx = 25, pady =5)
        #ComboBoxes
        self.locationComboBox.grid(column = 0, row = 1, sticky = (N,S,E,W),padx = 5, pady = 5)

        #self.movePlayer.mainloop()
        self.movePlayer.wait_window(self.movePlayer)

if __name__ == "__main__":
    sc = MovePlayerScreen(None)
    sc.initScreen()
