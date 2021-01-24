# -*- coding: utf-8 -*-
# Submitted by Harsh Bhatia (2019AD04086), Alkesh Chaturvedi, Raza Abbas
# Bloxorz game ACI Assignment 1

import copy

#*****************************************************************************
#
#   givenMap, which is an input to this program contains:
#   
#   Bloxorx game Terrain which is represented using a Map of 0,1 such that
#   0: represents a Void
#   1: represents a Tile
#   9: represents a Goal position
#
#   getTerrain() will do the following:
#   
#   1) Read giveMap variable and prepares givenTerrain and remainingBoard
#   2) Display Map or Terrain (Level-1) according the Map limits 
#      input for this game  
#   3) Return givenTerrain and remainingBoard  
#    
#*****************************************************************************
def getTerrain(givenMap):
    
    givenTerrain   = []
    mapLength      = len(givenMap)
    mapLineCounter = 1
  
    for getTerrainCtr in range(0,mapLength):
        givenTerrain.append([int(x) for x in givenMap[getTerrainCtr]])
        mapLineCounter = mapLineCounter + 1
        if mapLineCounter > rowLimit: break
    
    remainingBoard = []
    
    getTerrainCtr = getTerrainCtr + 1
    
    for remainingBoardCtr in range(getTerrainCtr,mapLength): 
        remainingBoard.append([int(k) for k in givenMap[remainingBoardCtr]])

    print("PLEASE NOTE:: Board starts at Row, Col = (0,0) and not at (1,1)")
    print("All following references to Row & Col should be read accordingly")
    print("\nStart position of Agent or block is at (",xInitial, ",", yInitial,")")
    print("**************************************************")

    print("Input board displayed below where 0=void,1=tile & 9=goal")
    print("**************************************************")
    for val in givenTerrain:
        print(val)
    print("**************************************************")
    
    print("remainingBoard (can be blank):")
    for val in remainingBoard:
        print(val)
    print("**************************************************")
    
    return givenTerrain, remainingBoard

#*****************************************************************************
#
#   agentNode class declares different class variables and functions
#    
#*****************************************************************************

class agentNode:

    def __init__(self, x, y, agentAlignment, parentNode, playingCourt, x1=None,y1=None):
        self.x                  = x
        self.y                  = y
        self.agentAlignment     = agentAlignment  
        self.parentNode         = parentNode
        self.playingCourt       = copy.deepcopy(playingCourt)
        self.x1                 = x1
        self.y1                 = y1

    def goRight(self):
        childNode = agentNode(self.x, self.y, self.agentAlignment, self, self.playingCourt)
    
        if childNode.agentAlignment == "STAND_STRAIGHT":
           childNode.agentAlignment = "LAY_HORIZONTALLY"
           childNode.x = childNode.x + 1
        elif childNode.agentAlignment == "LAY_HORIZONTALLY":
           childNode.agentAlignment = "STAND_STRAIGHT"
           childNode.x = childNode.x + 2
        elif childNode.agentAlignment == "LAY_VERTICALLY":
           childNode.x = childNode.x + 1
           
        return childNode

    def goLeft(self):
        childNode = agentNode(self.x, self.y, self.agentAlignment, self, self.playingCourt)

        if childNode.agentAlignment == "STAND_STRAIGHT":
           childNode.agentAlignment = "LAY_HORIZONTALLY"
           childNode.x = childNode.x - 2
        elif childNode.agentAlignment == "LAY_HORIZONTALLY":
           childNode.agentAlignment = "STAND_STRAIGHT"
           childNode.x = childNode.x - 1
        elif childNode.agentAlignment == "LAY_VERTICALLY":
           childNode.x = childNode.x - 1

        return childNode 
    
    def goUp(self):
        childNode = agentNode(self.x, self.y, self.agentAlignment, self, self.playingCourt)

        if childNode.agentAlignment == "STAND_STRAIGHT":
           childNode.agentAlignment = "LAY_VERTICALLY"
           childNode.y = childNode.y - 2
        elif childNode.agentAlignment == "LAY_HORIZONTALLY":
           childNode.y = childNode.y - 1
        
        elif childNode.agentAlignment == "LAY_VERTICALLY":
           childNode.agentAlignment = "STAND_STRAIGHT"
           childNode.y = childNode.y - 1
        
        return childNode 

    def goDown(self):
        childNode = agentNode(self.x, self.y, self.agentAlignment, self, self.playingCourt)

        if childNode.agentAlignment == "STAND_STRAIGHT":
           childNode.agentAlignment = "LAY_VERTICALLY"
           childNode.y = childNode.y + 1
        elif childNode.agentAlignment == "LAY_HORIZONTALLY":
           childNode.y = childNode.y + 1

        elif childNode.agentAlignment == "LAY_VERTICALLY":
           childNode.agentAlignment = "STAND_STRAIGHT"
           childNode.y = childNode.y + 2
           
        return childNode 

    def split_goUp(self):
        childNode = agentNode(self.x, self.y, self.agentAlignment, self, self.playingCourt, self.x1, self.y1)
        childNode.y -= 1
        return childNode 

    def split_goDown(self):
        childNode = agentNode(self.x, self.y, self.agentAlignment, self, self.playingCourt, self.x1, self.y1)
        childNode.y += 1
        return childNode 


    def split_goLeft(self):
        childNode = agentNode(self.x, self.y, self.agentAlignment, self, self.playingCourt, self.x1, self.y1)
        childNode.x -= 1
        return childNode 


    def split_goRight(self):
        childNode = agentNode(self.x, self.y, self.agentAlignment, self, self.playingCourt, self.x1, self.y1)
        childNode.x += 1
        return childNode 

    def split1_goUp(self):
        childNode = agentNode(self.x, self.y, self.agentAlignment, self, self.playingCourt, self.x1, self.y1)
        childNode.y1 -= 1
        return childNode 

    def split1_goDown(self):
        childNode = agentNode(self.x, self.y, self.agentAlignment, self, self.playingCourt, self.x1, self.y1)
        childNode.y1 += 1
        return childNode 

    def split1_goLeft(self):
        childNode = agentNode(self.x, self.y, self.agentAlignment, self, self.playingCourt, self.x1, self.y1)
        childNode.x1 -= 1
        return childNode 

    def split1_goRight(self):
        childNode = agentNode(self.x, self.y, self.agentAlignment, self, self.playingCourt, self.x1, self.y1)
        childNode.x1 += 1
        return childNode 

    def showAgentLocation(self):
        if self.agentAlignment != "SPLIT":
            print("Agent position on board: ", self.agentAlignment, " at column = ", self.x, "and row = ", self.y)
        else:
            print("Agent position on board: ", self.agentAlignment, " at column(s) = ", self.x, self.x1, "and row(s) = ", self.y, self.y1)
    
    def showBoard(self):
        
        # local definition
        x   = self.x
        y   = self.y
        x1  = self.x1
        y1  = self.y1
        agentAlignment = self.agentAlignment
        playingCourt = self.playingCourt

        # let's go

        if agentAlignment != "SPLIT":
            
            for i in range(len(playingCourt)): # for ROW
                print("",end='  ')
                for j in range(len(playingCourt[i])): # for COL in a ROW

                    if (i==y and j==x and agentAlignment=="STAND_STRAIGHT") or \
                            ((i==y and j==x) or (i==y and j==x+1) and agentAlignment=="LAY_HORIZONTALLY") or \
                            ((i==y and j==x) or (i==y+1 and j==x) and agentAlignment=="LAY_VERTICALLY"):

                        print("x",end=' ')

                    elif(playingCourt[i][j]==0):
                        print(" ",end=' ')
                    else:
                        print(playingCourt[i][j], end=' ')
                print("")
        else: # CASE SPLIT
            for i in range(len(playingCourt)): # for ROW
                print("",end='  ')
                for j in range(len(playingCourt[i])): # for COL

                    if (i==y and j==x) or (i==y1 and j==x1):
                        print("x",end=' ')

                    elif(playingCourt[i][j]==0):
                        print(" ",end=' ')
                    else:
                        print(playingCourt[i][j], end=' ')
                print("")
            
    
def isNumberThree(agent,x,y):
    playingCourt = agent.playingCourt

    for item in restOfBoard:

        if (x,y) ==  (item[0], item[1]):


            numToggle = item[2]   # num toggle
            index = 2   # index to check more element

            for i in range(numToggle):    # traverse toggle array
                bX = item[2*i+3]
                bY = item[2*i+4]
                if playingCourt[bX][bY] == 0:
                    playingCourt[bX][bY] = 1
                else:
                    playingCourt[bX][bY] = 0
        
            index = index + 1 + 2 * numToggle


            # check if "item" has more element
            if index < len(item):   # case has more

                # read num close
                numClose = item[index]

                # traverse list close if num > 0
                for i in range(numClose):
                    bX = item[index+2*i+1]
                    bY = item[index+2*i+2]
                    playingCourt[bX][bY]=0

                index = index + 1 + 2 * numClose
            


            # check if "item" has more element
            if index < len(item):   # case also has more item
                # get num open
                numOpen = item[index]

                # traverse list open if num > 0
                for i in range(numOpen):
                    bX = item[index+2*i+1]
                    bY = item[index+2*i+2]
                    playingCourt[bX][bY]=1



def isNumberFour(agent,x,y):

    playingCourt = agent.playingCourt
    
    for item in restOfBoard:
        if (x,y) ==  (item[0], item[1]):
            num = item[2]
            for i in range(num):
                bX = item[2*i+3]
                bY = item[2*i+4]
                playingCourt[bX][bY] = 0

def isNumberFive(agent,x,y):

    playingCourt = agent.playingCourt

    for item in restOfBoard:
        if (x,y) ==  (item[0], item[1]):


            numToggle = item[2]     # numtoggle
            index = 2   # index to check more element

            for i in range(numToggle):
                bX = item[2*i+3]
                bY = item[2*i+4]
                if playingCourt[bX][bY] == 0:
                    playingCourt[bX][bY] = 1
                else:
                    playingCourt[bX][bY] = 0
            
            index = index + 1 + 2 * numToggle

            # check if "item" has more element
            if index < len(item):   # case has more

                # read num close
                numClose = item[index]
                    
                # traverse list close if num > 0
                for i in range(numClose):
                    bX = item[index+2*i+1]
                    bY = item[index+2*i+2]
                    playingCourt[bX][bY]=0

                index = index + 1 + 2 * numClose
            
            # check if "item" has more element
            if index < len(item):   # case also has more item
                # get num open
                numOpen = item[index]

                # traverse list open if num > 0
                for i in range(numOpen):
                    bX = item[index+2*i+1]
                    bY = item[index+2*i+2]
                    playingCourt[bX][bY]=1


def isNumberSix(agent,x,y):

    playingCourt = agent.playingCourt

    for item in restOfBoard:
        if (x,y) ==  (item[0], item[1]):
            num = item[2]
            for i in range(num):
                bX = item[2*i+3]
                bY = item[2*i+4]
                playingCourt[bX][bY] = 1

def isNumberSeven(agent,x,y):  

    array = []    

    for item in restOfBoard:
        if (x,y) ==  (item[0], item[1]):
            num = item[2]
            # format x7 y7 2 x y x1 y1
            for i in range(num):
                bX = item[2*i+3]
                bY = item[2*i+4]
                array.append([bX,bY])

    (agent.y,agent.x,agent.y1,agent.x1) = \
            (array[0][0],array[0][1],array[1][0], array[1][1])

    agent.agentAlignment = "SPLIT"

def isNumberEight(agent,x,y):

    playingCourt = agent.playingCourt

    for item in restOfBoard:
        if (x,y) ==  (item[0], item[1]):

            num = item[2]
            for i in range(num):
                bX = item[2*i+3]
                bY = item[2*i+4]
                playingCourt[bX][bY] = 1

#*****************************************************************************
#
#
#*****************************************************************************

def isValidBlock(agent):
    
    if checkFloor(agent):
        
        x     = agent.x
        y     = agent.y
        x1    = agent.x1
        y1    = agent.y1
        agentAlignment   = agent.agentAlignment
        playingCourt = agent.playingCourt
        
        
        if agentAlignment == "STAND_STRAIGHT" and playingCourt[y][x] == 2:
            return False 

        if agentAlignment == "STAND_STRAIGHT" and playingCourt[y][x] == 3:
            isNumberThree(agent,x,y)
        
        if playingCourt[y][x] == 4:
            isNumberFour(agent,x,y)
        if agentAlignment == "LAY_HORIZONTALLY" and playingCourt[y][x+1] == 4:
            isNumberFour(agent,x+1,y)
        if agentAlignment == "LAY_VERTICALLY" and playingCourt[y+1][x] == 4:
            isNumberFour(agent,x,y+1)
        if agentAlignment == "SPLIT" and playingCourt[y1][x1] == 4:
            isNumberFour(agent,x1,y1)


        if playingCourt[y][x] == 5:
            isNumberFive(agent,x,y)
        if agentAlignment == "LAY_HORIZONTALLY" and playingCourt[y][x+1] == 5:
            isNumberFive(agent,x+1,y)
        if agentAlignment == "LAY_VERTICALLY" and playingCourt[y+1][x] == 5:
            isNumberFive(agent,x,y+1)
        if agentAlignment == "SPLIT" and playingCourt[y1][x1] == 5:
            isNumberFive(agent,x1,y1)

        if playingCourt[y][x] == 6:
            isNumberSix(agent,x,y)
        if agentAlignment == "LAY_HORIZONTALLY" and playingCourt[y][x+1] == 6:
            isNumberSix(agent,x+1,y)
        if agentAlignment == "LAY_VERTICALLY" and playingCourt[y+1][x] == 6:
            isNumberSix(agent,x,y+1)
        if agentAlignment == "SPLIT" and playingCourt[y1][x1] == 6:
            isNumberSix(agent,x1,y1)

        if agentAlignment == "STAND_STRAIGHT" and playingCourt[y][x] == 7:
            isNumberSeven(agent,x,y)
        if agentAlignment == "SPLIT": # check IS_MERGE
            # case LAY_HORIZONTALLY: x first
            if y == y1 and x == x1 -1:
                agent.agentAlignment = "LAY_HORIZONTALLY"

            # case LAY_HORIZONTALLY: x1 first
            if y == y1 and x == x1 + 1:
                agent.agentAlignment = "LAY_HORIZONTALLY"
                agent.x   = x1

            # case LAY_VERTICALLY: y first
            if x == x1 and y == y1 - 1:
                agent.agentAlignment = "LAY_VERTICALLY"
            
            # case LAY_VERTICALLY: y1 first
            if x == x1 and y == y1 + 1:
                agent.agentAlignment = "LAY_VERTICALLY"
                agent.y   = y1

        if agentAlignment == "STAND_STRAIGHT" and playingCourt[y][x] == 8:
            isNumberEight(agent,x,y)
            
        return True
    else:
        return False

#*****************************************************************************
#
#   checkFloor() used to check if agent is fully positioned on playing court  
#   if yes, return True otherwise False
#
#*****************************************************************************

def checkFloor(agent):

    playingCourt = agent.playingCourt
    agentAlignment = agent.agentAlignment
    x = agent.x
    y = agent.y
    
    if x >= 0 and y >= 0 and x < colLimit and y < rowLimit and playingCourt[y][x] != 0:

        if agentAlignment   == "STAND_STRAIGHT":
           return True
        elif agentAlignment == "LAY_HORIZONTALLY":
           if x+1 < colLimit and playingCourt[y][x+1] != 0 :
              return True
        elif agentAlignment == "LAY_VERTICALLY":
           if y+1 < rowLimit and playingCourt[y+1][x] != 0 :
              return True
        else:
            x1 = agent.x1
            y1 = agent.y1

            if x1 >= 0 and y1 >= 0 and x1 < colLimit and y1 < rowLimit and playingCourt[y1][x1] != 0:
               return True
    else:
        return False

#*****************************************************************************
#   
#   alreadyExplored() checks if neighbor position or child node is already
#   explored by checking in tempState list aka explored list.    
#
#*****************************************************************************

def alreadyExplored(agent):

    if agent.agentAlignment != "SPLIT":

        for node in tempState:
            if node.x == agent.x and node.y == agent.y and node.agentAlignment == agent.agentAlignment and node.playingCourt == agent.playingCourt:
               return True
    else:
        for node in tempState:
            if node.x  == agent.x and node.y  == agent.y and node.x1 == agent.x1 and node.y1 == agent.y1 and node.agentAlignment == agent.agentAlignment and node.playingCourt == agent.playingCourt:
               return True

    return False

#*****************************************************************************
#
#   crawl() adds legal neighbor positions or child nodes of agent to
#   Frontier or Queue. Only child nodes which are not explored earlier
#   will be added in Frontier. As soon as a node is added in Frontier or
#   Queue, it is added in explored (tempState) list as well. This will 
#   reduce the search space by removing the loopy paths   
#
#*****************************************************************************

def crawl(Queue, agent):

    if isValidBlock(agent):
        if alreadyExplored(agent):
            return None

        Queue.append(agent)
        tempState.append(agent)
        return True 

    return False   

#*****************************************************************************
#
#   printFinalPath() shows step-by-step moves of agent on the given board
#
#*****************************************************************************

def printFinalPath(agent):
    
    print("**************************************************")
    
    holdNode = agent.parentNode
    finalPath = [agent]
    
    while holdNode != None:
        
        if holdNode.agentAlignment != "SPLIT":
            childNode = agentNode(holdNode.x, holdNode.y,holdNode.agentAlignment,holdNode.parentNode,holdNode.playingCourt)
        else:
            childNode = agentNode(holdNode.x, holdNode.y,holdNode.agentAlignment,holdNode.parentNode,holdNode.playingCourt,holdNode.x1,holdNode.y1)

        holdNode = holdNode.parentNode
        finalPath = [childNode] + finalPath

    ctr = 0
    
    for val in finalPath:
        ctr = ctr + 1
        print("\nStep (",ctr,")")
        val.showAgentLocation()
        print("**************************************************")
        val.showBoard()

    print("\nAgent took",ctr,"step(s) to solve this problem using BFS")

#*****************************************************************************
#
#   goalTest() checks & return True if agent is standing straight    
#   & its location on specified terrain is same as goal location
#
#*****************************************************************************

def goalTest(agent):
   
    if agent.agentAlignment == "STAND_STRAIGHT" and agent.playingCourt[agent.y][agent.x] == 9:
        return True
    else:
        return False

#*****************************************************************************
#
#   breadthFirstSearch() is using Frontier as a queue data structure
#   to scan all shallowest neighbor (aka childNodes) positions of agent 
#   and does to goalTest 
#
#*****************************************************************************

def breadthFirstSearch(agent):

    frontier = []
    frontier.append(agent)
    tempState.append(agent)

    while frontier:
        current = frontier.pop(0)

        if goalTest(current):
           printFinalPath(current)
           return True

        if current.agentAlignment != "SPLIT":

           crawl(frontier,current.goRight())
           crawl(frontier,current.goLeft())
           crawl(frontier,current.goUp())
           crawl(frontier,current.goDown())

        else: 

           crawl(frontier,current.split_goRight())
           crawl(frontier,current.split_goLeft())
           crawl(frontier,current.split_goUp())
           crawl(frontier,current.split_goDown())
            
           crawl(frontier,current.split1_goRight())
           crawl(frontier,current.split1_goLeft())
           crawl(frontier,current.split1_goUp())
           crawl(frontier,current.split1_goDown())

    return False

#*****************************************************************************
#
#   Main Program starts here
#
#   1) Input board for agent as a Map. Also input start position of agent  
#   2) Invoke getTerrain() & obtain playing Court or board for agent to crawl
#   3) Get agent or block node created  
#   4) Invoke breadFirstSearch() uninformed search
#                
#*****************************************************************************

# Input the terrain here
givenMap = [[1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 1, 1, 9, 1, 1],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 0]] 

# Input the Agent or Block start position
startAt = [2,2]

# Input the terrain or Map limits here according to the above provided Map
# Note: mapLimits[0] = total terrain rows; mapLimits[1] = total terrain cols
# mapLimits can be reduced to exclude some of the terrain portion

mapLimits = [6,10] 

xInitial  = int(startAt[0])
yInitial  = int(startAt[1])
    
rowLimit = int(mapLimits[0])
colLimit = int(mapLimits[1])

givenTerrain, restOfBoard = getTerrain(givenMap)

tempState = []

agent = agentNode(xInitial, yInitial, "STAND_STRAIGHT", None, givenTerrain)

print("Agent solves Bloxorz game problem using Breadth First Search strategy as below")
breadthFirstSearch(agent)