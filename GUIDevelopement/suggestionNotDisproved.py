from Tkinter import *
import ttk
import itertools
import tkMessageBox
import tkFont


#---------------------------------------------------------------------------
                            #Root Window
suggNotDisp = Tk()
suggNotDisp.title("Clue-Less Message: Suggestion Not Disproved")
#---------------------------------------------------------------------------
                                #Font
customFont = tkFont.Font(family = "Helvetica", size=24, weight = 'bold', slant = 'italic')
customFont1 = tkFont.Font(family = "Helvetica", size=12, weight = 'bold')
#---------------------------------------------------------------------------
                            #Parent Frame
suggNotDispLabel = ttk.Frame(suggNotDisp, borderwidth = 5, relief = "flat")
suggNotDispBtn = ttk.Frame(suggNotDisp, borderwidth = 5, relief = "flat")
#---------------------------------------------------------------------------
                                #Label
suggNotDisprovedLabel = Label(suggNotDispLabel, text = "<<Player>>, no one was able to prove your suggestion false.  You may end your turn or make an accusation now.",
                        font = customFont1, foreground = 'red', wraplength = 400, justify = CENTER)
#---------------------------------------------------------------------------                        
                                #Buttons
endTurn = Button(suggNotDispBtn, text = "End Turn",font = customFont1)
mAccusation = Button(suggNotDispBtn, text = "Make Accusation",font = customFont1)
#---------------------------------------------------------------------------
                                #IIG Icon
iigIcon = PhotoImage(file = 'IGG_Icon.gif')
iigIconLabel = ttk.Label(suggNotDisp, image = iigIcon)
#---------------------------------------------------------------------------
                        #Grid Layout Manager
suggNotDispLabel.grid(column = 0, row = 0, sticky = (N,S,E,W),padx = 15, pady = 15)
suggNotDispBtn.grid(column = 0, row = 2, sticky = (E,W))
suggNotDisprovedLabel.grid(column = 1, row = 0, sticky = (E,W))
iigIconLabel.grid(column = 4, row = 0, sticky = (E), padx = 5, pady = 5)

endTurn.grid(column = 2, row = 2, sticky = (E),padx = 15, pady = 15)
mAccusation.grid(column = 4, row = 2, sticky = (E),padx = 15, pady = 15)




suggNotDisp.mainloop()


