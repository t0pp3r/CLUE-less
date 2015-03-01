from Tkinter import *
import ttk

root = Tk()
Grid.rowconfigure(root,0,weight=1)
Grid.columnconfigure(root,0,weight=1)


##def __init__(self): 
##    names=('One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten')
##    self.button = []
##    for i,name in enumerate(names):
##        self.button.append(Button(root, text = "test"))
##        row,col = divmod(i,1)
##        self.button[i].grid(sticky=W+E+N+S, row=row, column=col, padx=1, pady=1)
##

root.grid()
root.mainloop()
