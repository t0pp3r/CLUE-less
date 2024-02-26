from Tkinter import *
import ttk
import itertools
import tkMessageBox
import tkFont

#---------------------------------------------------------------------------
                            #Root Window
suggestion = Tk()
suggestion.title("Clue-Less Message: Suggestion")
#---------------------------------------------------------------------------
                                #Font
customFont = tkFont.Font(family = "Helvetica", size=24, weight = 'bold', slant = 'italic')
customFont1 = tkFont.Font(family = "Helvetica", size=12, weight = 'bold')
#---------------------------------------------------------------------------
                               #Parent Frame
suggLabel = ttk.Frame(suggestion, borderwidth = 5)
suggComboAndBtn = ttk.Frame(suggestion, borderwidth = 5)
#---------------------------------------------------------------------------
                                #Label
suggestionLabel = Label(suggLabel, text = "<<Player>>, please choose the suspect and murder weapon you would like to suggest.",
                        font = customFont1, foreground = 'red', wraplength = 400, justify = CENTER)

suspectLabel = Label(suggComboAndBtn, text = "Suspect:", font = customFont1, foreground = 'red')
weaponLabel = Label(suggComboAndBtn, text = "Weapon:", font = customFont1, foreground = 'red')
#---------------------------------------------------------------------------                        
                                #Buttons
suggOkBtn = Button(suggComboAndBtn, text = "OK", font = customFont1)
#---------------------------------------------------------------------------
                                #ComboBoxes
playervar = StringVar()
suspect = ('Mr. Green', 'Miss Scarlet', 'Prof. Plum', 'Mrs. White', 'Col. Mustard', 'Mrs. Peacock')
weapons = ('Lead Pipe', 'Knife', 'Rope', 'Revolver', 'Wrench', 'Candlestick')
suspectComboBox = ttk.Combobox(suggComboAndBtn, values = suspect, state = 'readonly', font = customFont1)
weaponComboBox = ttk.Combobox(suggComboAndBtn, values = weapons, state = 'readonly', font = customFont1)

#---------------------------------------------------------------------------
                                #IIG Icon
iigIcon = PhotoImage(file = 'IGG_Icon.gif')
iigIconLabel = ttk.Label(suggestion, image = iigIcon)
#---------------------------------------------------------------------------
                            #Grid Layout Manager
#---------------------------------------------------------------------------
#Frames
suggLabel.grid(column = 0, row = 0, columnspan = 3, sticky = (E,W))
suggComboAndBtn.grid(column = 0, row = 2, sticky = (N,W))

#Icons
iigIconLabel.grid(column = 4, row = 0, sticky = (E), padx = 5, pady = 5)
#Labels
suggestionLabel.grid(column = 1, row = 0, sticky = (N))
suspectLabel.grid(column = 0, row = 0, sticky = (S,E,W), padx = 5, pady = 5)
weaponLabel.grid(column = 1, row = 0, sticky = (S,E,W),padx = 5, pady = 5 )
#Buttons
suggOkBtn.grid(column = 4, row = 1, sticky = (E),padx = 25, pady =5)
#ComboBoxes
suspectComboBox.grid(column = 0, row = 1, sticky = (N,S,E,W),padx = 5, pady = 5)
weaponComboBox.grid(column = 1, row = 1, sticky = (N,S,E,W),padx = 5, pady = 5)


suggestion.mainloop()
