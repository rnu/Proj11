import random as r
from proj_GUI_Exp import *
import time as t

class CarpetFish(GUI):
    def __init__(self):
        #Seed for randomizer
        r.seed(2)
        #global variables
        self.isDebug = False
        self.isEvalMode= False
        self.selectedBlock = None
        self.selectedFish = None
        self.position_Fish = None

        #Start Gui
        GUI.__init__(self,master=None)
        #List of fish
        self.fish_list = ("Bass","Marlin","Steelhead", "Pike", "Muskellunge",\
                          "Perch", "Pariot Fish", "Trigger Fish", "Sun Fish",\
                          "Mahi-mahi", "Chillean Sea Bass", "Stripped Sea Bass",\
                          "Blue-Fin Tuna", "Barracuda")
        
        #Event for left-click on canvas
        self.canvas.bind("<1>", self.closestBlock)
        #Event for left-click on start button
        self.Start.bind("<1>", self.startRound)
      
    """
    Selects a fish to be sent to the board.
    """
    def selectFishType(self):
        temp = r.randint(0,(len(self.fish_list)-1))
        self.selectedFish = self.fish_list[temp]

    """
    Selects at random where the fish will be placed on the board.
    """
    def selectFishBlock(self):
        randx = r.randint(0,9)
        randy = r.randint(0,9)
        self.position_Fish = self.carpet_grid[(randx,randy)]
        
    """
    Checks if user's 'line' is in the same line as the fish.
    """
    def checkForFish(self):
        #Report back to user if a fish was caught.
        if self.selectedBlock == self.position_Fish:
            #Insert string into text box.
            self.text.insert(END, "--> {} - You caught a {}!\n".format(t.strftime("%H:%M:%S"),self.selectedFish))
            print("--> {} - You caught a {}!".format(t.strftime("%H:%M:%S"),self.selectedFish))
        else:
            #Insert string into text box.
            self.text.insert(END, "-->{} - Nothing was caught\n".format(t.strftime("%H:%M:%S")))
            print("--> No fish were caught")
            
    """
    Mouse-Event, finds closest rectangle when left_mouse button is clicked
    """
    def closestBlock(self,e):
        block = self.canvas.find_closest(e.x,e.y)
        self.canvas.itemconfigure(self.selectedBlock, fill = 'blue')
        self.canvas.itemconfigure(block, fill = 'red')
        self.selectedBlock=block[0]
        print(block)

    """
    Start round of fishing
    """
    def startRound(self,event):
        #Time to wait (in seconds)
        timer = r.randint(60,300)
        self.selectFishType()
        self.selectFishBlock()
        #For Debug/'Instant Result Mode'
        if self.isDebug == True:
            timer = r.randint(1,5)
            self.selectedBlock = 1
            self.position_Fish = 1
            self.selectFishType()
        print(timer)
        t.sleep(timer)
        self.checkForFish()

    
new_game = CarpetFish()
