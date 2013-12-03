from tkinter import *
from tkinter import ttk

class Test(Frame):
    def __init__(self,master=None):
        
        self.carpet_grid = {}
        self.cellWidth = 40
        self.cellHeight = 40
        
        #Call Frame constructor
        Frame.__init__(self,master)
        
        #Draw frame on grid
        self.grid()
        #Construct a label and add it to grid
        self.label = ttk.Label( self,text="Starting......")
        self.label.grid()
        #Key event
        self.label.bind("<1>", lambda e: self.label.configure(text="Moved inside"))

        #Generate Canvas
        self.canvas = Canvas(self, width=400, height=400, borderwidth=0, highlightthickness=0, bg = 'white')
        self.canvas.grid(column=0,row=2)
        #Generate Text
        self.text = Text(self, width=56, height = 5)
        self.text.grid(column=0,row=3,pady = 5)
        

        #Create Start Button
        self.Start = ttk.Button(text = 'Start Fishing')
        self.Start.grid(column=1,row=0)
        self.Debug = ttk.Button(text = 'Debug')
        self.Debug.grid(column=2,row=0)
        
        for column in range(10):
            for row in range(10):
                x1 = column * self.cellWidth
                y1 = row * self.cellHeight
                x2 = x1 + self.cellWidth 
                y2 = y1 + self.cellHeight
                self.carpet_grid[column,row] = self.canvas.create_rectangle(x1,y1,x2,y2, tags ="Rect")
                

   

    
#test = Test()
