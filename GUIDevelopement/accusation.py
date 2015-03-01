from Tkinter import *
import ttk
import itertools
import tkMessageBox
import tkFont

#---------------------------------------------------------------------------
                            #Root Window
accusation = Tk()
accusation.title("Clue-Less Message: Accusation")
#---------------------------------------------------------------------------
                                #Font
customFont = tkFont.Font(family = "Helvetica", size=24, weight = 'bold', slant = 'italic')
customFont1 = tkFont.Font(family = "Helvetica", size=12, weight = 'bold')
#---------------------------------------------------------------------------
                               #Parent Frame
accLabel = ttk.Frame(accusation, borderwidth = 5)
accComboAndBtn = ttk.Frame(accusation, borderwidth = 5)
#---------------------------------------------------------------------------
                                #Label
accusationLabel = Label(accLabel, text = "<<Player>>, please choose the suspect, room, and murder weapon you would like to include in your accusation.",
                        font = customFont1, foreground = 'red', wraplength = 400, justify = CENTER)

suspectLabel = Label(accComboAndBtn, text = "Suspect:", font = customFont1, foreground = 'red')
roomLabel    = Label(accComboAndBtn, text = "Room:", font = customFont1, foreground = 'red')
weaponLabel  = Label(accComboAndBtn, text = "Weapon:", font = customFont1, foreground = 'red')
#---------------------------------------------------------------------------                        
                                #Buttons
accOkBtn = Button(accComboAndBtn, text = "OK", font = customFont1)
#---------------------------------------------------------------------------
                                #ComboBoxes
playervar = StringVar()
suspect = ('Mr. Green', 'Miss Scarlet', 'Prof. Plum', 'Mrs. White', 'Col. Mustard', 'Mrs. Peacock')
weapons = ('Lead Pipe', 'Knife', 'Rope', 'Revolver', 'Wrench', 'Candlestick')
rooms = ('Study', 'Library', 'Conservatory', 'Hall', 'Billiard', 'Ballroom', 'Lounge', 'Dining Room', 'Kitchen')
suspectComboBox = ttk.Combobox(accComboAndBtn, values = suspect, state = 'readonly', font = customFont1)
weaponComboBox = ttk.Combobox(accComboAndBtn, values = weapons, state = 'readonly', font = customFont1)
roomsComboBox = ttk.Combobox(accComboAndBtn, values = rooms, state = 'readonly', font = customFont1)
#---------------------------------------------------------------------------
                                #IIG Icon
iigIcon = PhotoImage(file = 'IGG_Icon.gif')
iigIconLabel = ttk.Label(accusation, image = iigIcon)
#---------------------------------------------------------------------------
                            #Grid Layout Manager
#---------------------------------------------------------------------------
                                #Frames
accLabel.grid(column = 0, row = 0, sticky = (E,W))
accComboAndBtn.grid(column = 0, row = 1, sticky = (N,W))
                                #Icons
iigIconLabel.grid(row = 0, sticky = (E), padx = 5, pady = 5)
                                #Labels
accusationLabel.grid(column = 1, row = 0, sticky = (E))
suspectLabel.grid(column = 0, row = 0, sticky = (E,W), padx = 5, pady = 5)
roomLabel.grid(column = 1, row = 0, sticky = (E,W), padx = 5, pady = 5)
weaponLabel.grid(column = 2, row = 0, sticky = (E,W),padx = 5, pady = 5)
                                #Buttons
accOkBtn.grid(column = 4, row = 1, sticky = (E),padx = 25, pady =5)
                                #ComboBoxes
suspectComboBox.grid(column = 0, row = 1, sticky = (N,S,E,W),padx = 5, pady = 5)
weaponComboBox.grid(column = 2, row = 1, sticky = (N,S,E,W),padx = 5, pady = 5)
roomsComboBox.grid(column = 1, row = 1, sticky = (N,S,E,W),padx = 5, pady = 5)

accusation.mainloop()
