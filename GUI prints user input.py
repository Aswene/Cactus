import tkinter

class GUI(tkinter.Tk):
    def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.GUI_widgets()

    def Mouse(self):
        self.labelVariable.set( self.entryVariable.get())
        self.entry.focus_set()
        self.entry.selection_range(0, tkinter.END)

    def Keyboard(self,event):
        self.labelVariable.set( self.entryVariable.get())
        self.entry.focus_set()
        self.entry.selection_range(0, tkinter.END)

    def GUI_widgets(self):
        self.grid()
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=10)
        label1 = tkinter.Label(self, text="Enter your expression here:")
        label1.grid(column=0,row=1)
        label2 = tkinter.Label(self, text="Solution displayed here:")
        label2.grid(column=0,row=2)
        label3 = tkinter.Label(self, text="MESSAGE FOR USER: Enter the values in RADIANS and answers are provided in RADIANS", foreground="black",background="red")
        label3.grid(column=0,row=0,columnspan=2,sticky='EW')
        self.entryVariable = tkinter.StringVar()
        self.entry = tkinter.Entry(self,textvariable=self.entryVariable)
        self.entry.grid(column=1,row=1,sticky='EW')
        self.entry.bind("<Return>", self.Keyboard)
        button = tkinter.Button(self,text="CLICK HERE OR PRESS ENTER ON KEYBOARD TO DISPLAY RESULT",
                                command=self.Mouse,foreground="black",background="cyan")
        button.grid(column=0,row=3,columnspan=2,sticky='EW')
        self.labelVariable = tkinter.StringVar()
        label = tkinter.Label(self,textvariable=self.labelVariable,
                              anchor="w",foreground="black",background="yellow")
        label.grid(column=1,row=2,sticky='EW')
        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,False)
        self.update()
        self.geometry(self.geometry())       
        self.entry.focus_set()
        self.entry.selection_range(0, tkinter.END)

if __name__ == "__main__":
    block = GUI(None)
    block.title('Expression Evaluator')
    block.mainloop()
