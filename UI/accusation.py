from Tkinter import *
import ttk
import itertools
import tkMessageBox
import tkFont

class AccusationScreen:
    def __init__(self, controller):
        self.controller = controller
        self.accusation = None

    def okButtonPressed(self):
        if self.suspectComboBox.get() == "" or self.weaponComboBox.get() == "" or self.roomsComboBox.get() == "":
            tkMessageBox.showerror(title = "Clue-Less Message:  Input Error", message = "Please select an option for all drop down boxes.")
        else:
            self.controller.handleAccusation(self.suspectComboBox.get(), self.weaponComboBox.get(), self.roomsComboBox.get())
            self.accusation.destroy()

    def noButtonPressed(self):
        self.accusation.destroy()

    def initScreen(self):
        #---------------------------------------------------------------------------                        
        #Root Window
        self.accusation = Tk()
        self.accusation.title("Clue-Less Message: Accusation")
        #---------------------------------------------------------------------------                        
        #Font
        customFont = tkFont.Font(family = "Helvetica", size=24, weight = 'bold', slant = 'italic')
        customFont1 = tkFont.Font(family = "Helvetica", size=12, weight = 'bold')
        #---------------------------------------------------------------------------                        
        #Parent Frame
        accLabel = ttk.Frame(self.accusation, borderwidth = 5)
        accComboAndBtn = ttk.Frame(self.accusation, borderwidth = 5)
        #---------------------------------------------------------------------------                        
        #Label
        accusationLabel = Label(accLabel, text = "Do you want to make an accusation?  If not, click no.",
                                font = customFont1, foreground = 'black', wraplength = 400, justify = CENTER)

        suspectLabel = Label(accComboAndBtn, text = "Suspect:", font = customFont1, foreground = 'red')
        roomLabel    = Label(accComboAndBtn, text = "Room:", font = customFont1, foreground = 'red')
        weaponLabel  = Label(accComboAndBtn, text = "Weapon:", font = customFont1, foreground = 'red')
        #---------------------------------------------------------------------------                        
        #Buttons
        makeaccBtn = Button(accComboAndBtn, text = "Make Accusation", font = customFont1, command = self.okButtonPressed)
        cancelBtn = Button(accComboAndBtn, text = "Don't Make Accusation", font = customFont1, command = self.noButtonPressed)
        #---------------------------------------------------------------------------
        #ComboBoxes
        playervar = StringVar()
        suspects = self.controller.getAllCharacterNames()
        weapons = self.controller.getAllWeaponNames()
        rooms = self.controller.getAllRoomNames()
        self.suspectComboBox = ttk.Combobox(accComboAndBtn, values = suspects, state = 'readonly', font = customFont1)
        self.weaponComboBox = ttk.Combobox(accComboAndBtn, values = weapons, state = 'readonly', font = customFont1)
        self.roomsComboBox = ttk.Combobox(accComboAndBtn, values = rooms, state = 'readonly', font = customFont1)
        #---------------------------------------------------------------------------
        #IIG Icon
        #iigIcon = PhotoImage(file = 'IGG_Icon.gif')
        #iigIconLabel = ttk.Label(self.accusation, image = iigIcon)
        #---------------------------------------------------------------------------
        #Grid Layout Manager
        #---------------------------------------------------------------------------
        #Frames
        accLabel.grid(column = 0, row = 0, sticky = (E,W))
        accComboAndBtn.grid(column = 0, row = 1, sticky = (N,W))
        #Icons
        #iigIconLabel.grid(row = 0, sticky = (E), padx = 5, pady = 5)
        #Labels
        accusationLabel.grid(column = 1, row = 0, sticky = (E))
        suspectLabel.grid(column = 0, row = 0, sticky = (E,W), padx = 5, pady = 5)
        roomLabel.grid(column = 1, row = 0, sticky = (E,W), padx = 5, pady = 5)
        weaponLabel.grid(column = 2, row = 0, sticky = (E,W),padx = 5, pady = 5)
        #Buttons
        makeaccBtn.grid(column = 4, row = 1, sticky = (E),padx = 25, pady =5)
        cancelBtn.grid(column = 4, row = 2, sticky = (E), padx = 25, pady = 5)
        #ComboBoxes
        self.suspectComboBox.grid(column = 0, row = 1, sticky = (N,S,E,W),padx = 5, pady = 5)
        self.weaponComboBox.grid(column = 2, row = 1, sticky = (N,S,E,W),padx = 5, pady = 5)
        self.roomsComboBox.grid(column = 1, row = 1, sticky = (N,S,E,W),padx = 5, pady = 5)

        #self.accusation.mainloop()
        self.accusation.wait_window(self.accusation)

if __name__ == "__main__":
    ac = AccusationScreen(None)
    ac.initScreen()
