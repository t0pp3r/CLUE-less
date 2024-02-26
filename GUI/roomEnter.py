from Tkinter import *
import ttk
import itertools
import tkMessageBox
import tkFont


#---------------------------------------------------------------------------
#Root Window
rEnter = Tk()
rEnter.title("Clue-Less Message: Room Enter")
#---------------------------------------------------------------------------
                                #Font
customFont = tkFont.Font(family = "Helvetica", size=24, weight = 'bold', slant = 'italic')
customFont1 = tkFont.Font(family = "Helvetica", size=12, weight = 'bold')
customFont2 = tkFont.Font(family = "Helvetica", size=12, weight = 'bold')
#---------------------------------------------------------------------------
#Parent Frame
roomEnterLabel = ttk.Frame(rEnter, borderwidth = 5, relief = "flat")
roomEnterBtn = ttk.Frame(rEnter, borderwidth = 5, relief = "flat")
#Label
rEnterLabel = Label(roomEnterLabel, text = "<<Player>>, you have entered the <<Room>>.  You may now make a suggestion or accusation.",
                        font = customFont1, foreground = 'red', wraplength = 400, justify = CENTER)

                        
#Buttons
mSuggestion = Button(roomEnterBtn, text = "Make Suggestion",font = customFont1)
mAccusation = Button(roomEnterBtn, text = "Make Accusation",font = customFont1)

#IIG Icon
iigIcon = PhotoImage(file = 'IGG_Icon.gif')
iigIconLabel = ttk.Label(rEnter, image = iigIcon)


#Grid Layout Manager
roomEnterLabel.grid(column = 0, row = 0, sticky = (N,S,E,W),padx = 15, pady = 15)
roomEnterBtn.grid(column = 0, row = 2, sticky = (E,W))
rEnterLabel.grid(column = 1, row = 0, sticky = (E,W))
iigIconLabel.grid(column = 4, row = 0, sticky = (E), padx = 5, pady = 5)

mSuggestion.grid(column = 1, row = 2, sticky = (E),padx = 15, pady = 15)
mAccusation.grid(column = 2, row = 2, sticky = (E),padx = 15, pady = 15)




rEnter.mainloop()


