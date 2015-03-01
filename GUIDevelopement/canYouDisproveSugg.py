from Tkinter import *
import ttk
import itertools
import tkMessageBox
import tkFont

#---------------------------------------------------------------------------
                            #Root Window
cydSugg = Tk()
cydSugg.title("Clue-Less Message: Can You Disprove The Suggestion")
#---------------------------------------------------------------------------
                                #Font
customFont = tkFont.Font(family = "Helvetica", size=24, weight = 'bold', slant = 'italic')
customFont1 = tkFont.Font(family = "Helvetica", size=12, weight = 'bold')
#---------------------------------------------------------------------------
                               #Parent Frames
cydSuggText = ttk.Frame(cydSugg, borderwidth = 5)
cydSuggCombBtn = ttk.Frame(cydSugg, borderwidth = 5)
#---------------------------------------------------------------------------
                                #Label
cydSuggLabel = Label(cydSuggText, text = "Can you disprove the suggestion made? If yes, select your card below. Otherwise, select no.",
                        font = customFont1, foreground = 'red', wraplength = 400, justify = CENTER)

cydSuggcardLabel = Label(cydSuggText, text = "Select Card:", font = customFont1, foreground = 'red')
#---------------------------------------------------------------------------                        
                                #Buttons
yes = Button(cydSuggCombBtn, text = "Yes", font = customFont1)
no = Button(cydSuggCombBtn, text = "No", font = customFont1)
#---------------------------------------------------------------------------
                                #ComboBoxes
playervar = StringVar()
cards = ('card a', 'card b', 'card c', 'card d')

cardComboBox = ttk.Combobox(cydSuggCombBtn, values = cards, state = 'readonly', font = customFont1)

#---------------------------------------------------------------------------
                                #IIG Icon
iigIcon = PhotoImage(file = 'IGG_Icon.gif')
iigIconLabel = ttk.Label(cydSugg, image = iigIcon)
#---------------------------------------------------------------------------
                            #Grid Layout Manager
#---------------------------------------------------------------------------
#Frames
cydSuggText.grid(column = 0, row = 0, sticky = (E,W))
cydSuggCombBtn.grid(column = 0, row = 1, sticky = (N,W))

#Icons
iigIconLabel.grid(column = 4, row = 0, sticky = (E), padx = 5, pady = 5)
#Labels
cydSuggLabel.grid(column = 1, row = 0, sticky = (N))
cydSuggcardLabel.grid(column = 1, row = 1, sticky = (W), padx = 5, pady = 5)
#Buttons
yes.grid(column = 4, row = 0, sticky = (E),padx = 5, pady =5)
no.grid(column = 5, row = 0, sticky = (E),padx = 5, pady =5)
#ComboBoxes
cardComboBox.grid(column = 1, row = 0, sticky = (N,S,E,W),padx = 5, pady = 5)


cydSugg.mainloop()
