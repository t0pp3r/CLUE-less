from Tkinter import *
import ttk
import itertools
import tkMessageBox
import tkFont

class SuggestionScreen:
    def __init__(self, controller):
        self.controller = controller
        self.suggestion = None
        self.suspectComboBox = None
        self.weaponComboBox = None
        self.roomComboBox = None

    def okButtonPressed(self):
        if self.suspectComboBox.get() == "" or self.weaponComboBox.get() == "":
            tkMessageBox.showerror(title = "Clue-Less Message:  Input Error", message = "Please select an option for all drop down boxes.")
        else:
            self.controller.registerSuggestion(self.suspectComboBox.get(), self.weaponComboBox.get(), self.controller.getMyLocation())
            self.suggestion.destroy()
            

    def initScreen(self):
        self.suggestion = Tk()
        self.suggestion.title("Clue-Less Message: Suggestion")
        #---------------------------------------------------------------------------
                                        #Font
        customFont = tkFont.Font(family = "Helvetica", size=24, weight = 'bold', slant = 'italic')
        customFont1 = tkFont.Font(family = "Helvetica", size=12, weight = 'bold')
        #---------------------------------------------------------------------------
                                       #Parent Frame
        suggLabel = ttk.Frame(self.suggestion, borderwidth = 5)
        suggComboAndBtn = ttk.Frame(self.suggestion, borderwidth = 5)
        #---------------------------------------------------------------------------
                                        #Label
        suggestionLabel = Label(suggLabel, text = "Please choose the suspect, murder weapon, and room you would like to suggest.\n\nYour location: %s" % self.controller.getMyLocation(),
                                font = customFont1, foreground = 'black', wraplength = 400, justify = CENTER)

        suspectLabel = Label(suggComboAndBtn, text = "Suspect:", font = customFont1, foreground = 'red')
        weaponLabel = Label(suggComboAndBtn, text = "Weapon:", font = customFont1, foreground = 'red')
        #---------------------------------------------------------------------------                        
                                        #Buttons
        suggOkBtn = Button(suggComboAndBtn, text = "OK", font = customFont1, command = self.okButtonPressed)
        #---------------------------------------------------------------------------
                                        #ComboBoxes
        playervar = StringVar()
        suspects = self.controller.getAllCharacterNames()
        weapons = self.controller.getAllWeaponNames()
        self.suspectComboBox = ttk.Combobox(suggComboAndBtn, values = suspects, state = 'readonly', font = customFont1)
        self.weaponComboBox = ttk.Combobox(suggComboAndBtn, values = weapons, state = 'readonly', font = customFont1)

        #---------------------------------------------------------------------------
                                        #IIG Icon
        #iigIcon = PhotoImage(file = 'GUI\IGG_Icon.gif')
        #iigIconLabel = ttk.Label(self.suggestion, image = iigIcon)
        #---------------------------------------------------------------------------
                                    #Grid Layout Manager
        #---------------------------------------------------------------------------
        #Frames
        suggLabel.grid(column = 0, row = 0, columnspan = 3, sticky = (E,W))
        suggComboAndBtn.grid(column = 0, row = 2, sticky = (N,W))

        #Icons
        #iigIconLabel.grid(column = 4, row = 0, sticky = (E), padx = 5, pady = 5)
        #Labels
        suggestionLabel.grid(column = 1, row = 0, sticky = (N))
        suspectLabel.grid(column = 0, row = 0, sticky = (S,E,W), padx = 5, pady = 5)
        weaponLabel.grid(column = 1, row = 0, sticky = (S,E,W),padx = 5, pady = 5 )
        #Buttons
        suggOkBtn.grid(column = 4, row = 1, sticky = (E),padx = 25, pady =5)
        #ComboBoxes
        self.suspectComboBox.grid(column = 0, row = 1, sticky = (N,S,E,W),padx = 5, pady = 5)
        self.weaponComboBox.grid(column = 1, row = 1, sticky = (N,S,E,W),padx = 5, pady = 5)

        #self.suggestion.mainloop()
        self.suggestion.wait_window(self.suggestion)

if __name__ == "__main__":
    sc = SuggestionScreen(None)
    sc.initScreen()
