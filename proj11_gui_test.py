from tkinter import *
from tkinter import ttk

class GUI(Frame):
    def __init__(self,master=None):
        #Title of Frame
        self.carpet_grid = {}
        self.cellWidth =40
        self.cellHeight=40
        
        #Call Frame init
        Frame.__init__(self,master)
        self.grid()
        
        self.makeMenu()
        self.makeCanvas()
        self.makeText()
        self.makeButtons()

    def makeButtons(self):
        self.Start = ttk.Button(text='Start Fishing')
        self.Start.grid(column=0,row=1)
        #Now in Game Modes
        #self.Debug = ttk.Button(text='Debug')
        #self.Debug.grid(column=0, row=2)
        
    def makeMenu(self):
        #Generate Menu
        self.mb = Menu(self)
        self.master.config(menu=self.mb)
        #File Menu
        self.fileMenu = Menu(self.mb, tearoff = False)
        self.mb.add_cascade(label="File", menu = self.fileMenu)
        self.fileMenu.add_command(label="Print Report", command=lambda:self.printReport())
        #Options Menu
        self.modesMenu = Menu(self.mb, tearoff=False)
        self.mb.add_cascade(label="Game Modes", menu=self.modesMenu)
        self.modesMenu.add_command(label="Normal Mode", command = lambda:self.setDebug(False))
        self.modesMenu.add_command(label="Evaluation Mode", )
        self.modesMenu.add_command(label="Instant Results", command = lambda:self.setDebug(True))
        

    def makeCanvas(self):
        #Make canvas on frame
        self.canvas = Canvas(self, width=401, height=401, borderwidth=0, highlightthickness=0, bg = 'white')
        self.canvas.grid(columnspan=4, rowspan=4)

        for column in range(10):
            for row in range(10):
                x1 = column * self.cellWidth
                y1 = row * self.cellHeight
                x2 = x1 + self.cellWidth 
                y2 = y1 + self.cellHeight
                self.carpet_grid[column,row] = self.canvas.create_rectangle(x1,y1,x2,y2, tags ="Rect", fill='blue')
                
    def makeText(self):
        #Label for the frame around text
        self.labelframe = LabelFrame(self, text="Fishing Report")
        self.labelframe.grid(column=1,row=5,rowspan=5, pady=5)
        #Text in the labelframe
        self.text = Text(self.labelframe, width=56, height = 5, bg = "#A9A9A9")
        self.text.grid()
        

    def printReport(self):
        try:
            file = open("Fishing_Report.txt",'w')
            file.write("{}".format(self.text.get(1.0,END)))
            file.close()
        except IOError:
            messagebox.showinfo(message="Error writting to file")
            return
        
    def setDebug(self, TorF=False):
            self.isDebug = TorF
            
#test = GUI()

