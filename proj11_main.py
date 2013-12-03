import random as r
from proj11_gui_test import *
import time as t

class CarpetFish(Test):
    def __init__(self):
        #global variables
        self.selectedBlock = None
        self.selectedFish = None
        self.position_Fish = None
        self.caughtFish = False

        #Start Gui
        Test.__init__(self,master=None)
        #List of fish
        self.fish_list = ("Bass","Marlin","Steelhead")
        #Event for left-click on canvas
        self.canvas.bind("<1>", self.closestBlock)
        #Event for left-click on start button
        self.Start.bind("<1>", self.startRound)
        #Event for debug
        self.Debug.bind("<1>",self.Debugger)
        
            
    """
    Selects a fish to be sent to the board.
    """
    def selectFishType(self):
        temp = r.randint(0,(len(self.fish_list)-1))
        self.selectedFish = self.fish_list[temp]

    """
    Selects at random where the fish will be placed on the board.
    """
    def selectFishBlock(self, debug = False):
        if debug == True:
            self.position_Fish = 1
            return
        randx = r.randint(0,9)
        randy = r.randint(0,9)
        self.position_Fish = self.carpet_grid[(randx,randy)]
        
    """
    Checks if user's 'line' is in the same line as the fish.
    """
    def checkForFish(self):
        if self.selectedBlock == self.position_Fish:
            self.caughtFish = True
            #I need to implement timestamps and make the else statement insert into text.
            self.text.insert(END, "You caught a {}!\n".format(self.selectedFish))
            print("You caught a {}!".format(self.selectedFish))
        else:
            print("No fish were caught")
    
    """
    Debug.
    """
    def Debug(self, set_block = None, set_fish = None, print_carpet = False):
        print("Debug")
        if set_block != None:
            self.position_Fish = set_block
        if set_fish != None:
            self.selectedFish = set_fish
        if print_carpet == True:
            print(self.carpet_grid)
        
            
    """
    Mouse-Event, finds closest rectangle when left_mouse button is clicked
    """
    def closestBlock(self,e):
        block = self.canvas.find_closest(e.x,e.y)
        self.canvas.itemconfigure(self.selectedBlock, fill = 'white')
        self.canvas.itemconfigure(block, fill = 'red')
        self.selectedBlock=block[0]
        print(block)

    """
    Start round of fishing
    """
    def startRound(self,event):
        #Time to wait (in seconds)
        timer = r.randint(1,5)
        self.selectFishType()
        self.selectFishBlock()
        print(timer)
        t.sleep(timer)
        self.checkForFish()

    def Debugger(self,event):
        self.selectedBlock = 1 
        self.selectFishBlock(debug = True)
        #Time to wait (in seconds)
        timer = r.randint(1,5)
        self.selectFishType()
        print(timer)
        t.sleep(timer)
        self.checkForFish()
    """
    Refresh grid and check for caught fish.
    """
    def refresh(self):
        pass
        
        
    
new_game = CarpetFish()
