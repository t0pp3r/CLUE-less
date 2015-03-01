from Tkinter import *
import ttk
import itertools
import tkMessageBox
import tkFont

class DisproveSuggestionScreen:
    def __init__(self, controller):
        self.controller = controller
        self.cydSugg = None
        self.cardComboBox = None

    def noButtonPressed(self):
        self.controller.sendNotDisprovedSuggestion()
        self.cydSugg.destroy()

    def yesButtonPressed(self):
        s = self.cardComboBox.get()
        if s == "":
            tkMessageBox.showerror(title = "Clue-Less Message:  Input Error", message = "Please select an option for all drop down boxes.")
        elif s != self.controller.suggestedPlayer and s != self.controller.suggestedWeapon and s != self.controller.suggestedRoom:
            tkMessageBox.showerror(title = "Clue-Less Message:  Input Error", message = "Your choice does not disprove any of the suggested cards.")
        else:
            self.controller.sendDisprovedSuggestion(s)
            self.cydSugg.destroy()
    
    def initScreen(self):
        #---------------------------------------------------------------------------
                                #Root Window
        self.cydSugg = Tk()
        self.cydSugg.title("Clue-Less Message: Can You Disprove The Suggestion")
        #---------------------------------------------------------------------------
                                    #Font
        customFont = tkFont.Font(family = "Helvetica", size=24, weight = 'bold', slant = 'italic')
        customFont1 = tkFont.Font(family = "Helvetica", size=12, weight = 'bold')
        #---------------------------------------------------------------------------
                                   #Parent Frames
        self.cydSuggText = ttk.Frame(self.cydSugg, borderwidth = 5)
        self.cydSuggCombBtn = ttk.Frame(self.cydSugg, borderwidth = 5)
        #---------------------------------------------------------------------------
                                    #Label
        self.cydSuggLabel = Label(self.cydSuggText, text = "Can you disprove the suggestion made? If yes, select your card below. Otherwise, select no." +
                                  "\n\nSuggested Cards:\n\nRoom: %s\nCharacter: %s\nWeapon: %s\n" % (self.controller.suggestedRoom, self.controller.suggestedPlayer, self.controller.suggestedWeapon),
                            font = customFont1, foreground = 'black', wraplength = 400, justify = CENTER)

        self.cydSuggcardLabel = Label(self.cydSuggText, text = "Select Card:", font = customFont1, foreground = 'red')
        #---------------------------------------------------------------------------                        
                                    #Buttons
        yes = Button(self.cydSuggCombBtn, text = "Yes", font = customFont1, command = self.yesButtonPressed)
        no = Button(self.cydSuggCombBtn, text = "No", font = customFont1, command = self.noButtonPressed)
        #---------------------------------------------------------------------------
                                    #ComboBoxes
        playervar = StringVar()
        cards = self.controller.getYourCards()#('card a', 'card b', 'card c', 'card d')

        self.cardComboBox = ttk.Combobox(self.cydSuggCombBtn, values = cards, state = 'readonly', font = customFont1)

        #---------------------------------------------------------------------------
                                    #IIG Icon
        #iigIcon = PhotoImage(file = 'IGG_Icon.gif')
        #iigIconLabel = ttk.Label(self.cydSugg, image = iigIcon)
        #---------------------------------------------------------------------------
                                #Grid Layout Manager
        #---------------------------------------------------------------------------
        #Frames
        self.cydSuggText.grid(column = 0, row = 0, sticky = (E,W))
        self.cydSuggCombBtn.grid(column = 0, row = 1, sticky = (N,W))

        #Icons
        #iigIconLabel.grid(column = 4, row = 0, sticky = (E), padx = 5, pady = 5)
        #Labels
        self.cydSuggLabel.grid(column = 1, row = 0, sticky = (N))
        self.cydSuggcardLabel.grid(column = 1, row = 1, sticky = (W), padx = 5, pady = 5)
        #Buttons
        yes.grid(column = 4, row = 0, sticky = (E),padx = 5, pady =5)
        no.grid(column = 5, row = 0, sticky = (E),padx = 5, pady =5)
        #ComboBoxes
        self.cardComboBox.grid(column = 1, row = 0, sticky = (N,S,E,W),padx = 5, pady = 5)

        self.cydSugg.wait_window(self.cydSugg)

if __name__ == "__main__":
    cyd = DisproveSuggestionScreen(None)
    cyd.initScreen()
