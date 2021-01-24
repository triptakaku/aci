# -*- coding: utf-8 -*-
# Submitted by Harsh Bhatia (2019AD04086), Alkesh Chaturvedi, Raza Abbas
# Bloxorz game ACI Assignment 1

# Some clarify
# 0: None
# 1: Normal
# 2: Đo đỏ
# 3: Chữ X  (T C O)
# 4: Cục tròn đặc (only đóng).
# 5: Cục tròn đặc (T C O)
# 6: Cục tròn đặc (only mở)
# 7: Cục phân thân
# 8: Chữ X  (only mở)
# 9: Lỗ chiến thắng

import copy

#*****************************************************************************
#
#   Map file, which is an input file to this program contains:
#   
#   (A) 
#   Bloxorx game Terrain which is represented using a Map of 0,1 such that
#   0: represents a Void
#   1: represents a Tile
#   9: represents a Goal position
#
#   (B)
#   Initial position of the Agent or Block
#   Initial position can be changed in Map file to any valid position(tile) 
# 
#   getTerrain() will read the mapFile as below:
#   
#   1) Read first line to determine the size of the map and starting
#      position of the agent or block
#   
#   2) Display Map or Terrain (Level-1) used for this game  
#
#   3) Return Map size, Map & Starting co-ordinates  
#    
#*****************************************************************************
def getTerrain(mapFile):
    
    fileHandler = open(mapFile,"r")
    firstLine = fileHandler.readline()

    MAP_ROW = int(firstLine.split()[0])
    MAP_COL = int(firstLine.split()[1])
    xStart  = int(firstLine.split()[2])
    yStart  = int(firstLine.split()[3])
    
    mapLineCounter = 1
    givenTerrain = []
  
    for nextLine in fileHandler:
        givenTerrain.append([int(k) for k in nextLine.split()])
        mapLineCounter = mapLineCounter + 1
        if mapLineCounter > MAP_ROW: break

    manaBoa = []
    
    for nextLine in fileHandler: 
        manaBoa.append([int(k) for k in nextLine.split()])

    print("\nStart position of Agent or block is at (",xStart, ",", yStart,")")
    print("**************************************************")

    print("Input Terrain displayed below using a MAP where 0=void,1=tile & 9=goal")
    print("**************************************************")
    for val in givenTerrain:
        print(val)
    print("**************************************************")
    
    print("ManaBoa (can be blank):")
    for val in manaBoa:
        print(val)
    print("**************************************************")
    
    return MAP_ROW, MAP_COL, xStart, yStart, givenTerrain, manaBoa


class agentNode:

    def __init__(self, x, y, agentAlignment, parentNode, board, x1=None,y1=None):
        self.x                  = x
        self.y                  = y
        self.agentAlignment     = agentAlignment  
        self.parentNode         = parentNode
        self.board              = copy.deepcopy(board)
        self.x1                 = x1
        self.y1                 = y1
    
    def move_up(self):
        childNode = agentNode(self.x, self.y, self.agentAlignment, self, self.board)

        if self.agentAlignment == "STAND_STRAIGHT":
            childNode.y -= 2 
            childNode.agentAlignment = "LAY_VERTICALLY"

        elif childNode.agentAlignment == "LAY_HORIZONTALLY":
            childNode.y -= 1
        
        elif childNode.agentAlignment == "LAY_VERTICALLY":
            childNode.y -= 1
            childNode.agentAlignment = "STAND_STRAIGHT"
        
        return childNode 

    def move_down(self):
        childNode = agentNode(self.x, self.y, self.agentAlignment, self, self.board)

        if childNode.agentAlignment == "STAND_STRAIGHT":
            childNode.y += 1
            childNode.agentAlignment = "LAY_VERTICALLY"

        elif childNode.agentAlignment == "LAY_HORIZONTALLY":
            childNode.y += 1

        elif childNode.agentAlignment == "LAY_VERTICALLY":
            childNode.y += 2
            childNode.agentAlignment = "STAND_STRAIGHT"
        return childNode 

    def move_right(self):
        childNode = agentNode(self.x, self.y, self.agentAlignment, self, self.board)
    
        if childNode.agentAlignment == "STAND_STRAIGHT":
            childNode.x += 1
            childNode.agentAlignment = "LAY_HORIZONTALLY"

        elif childNode.agentAlignment == "LAY_HORIZONTALLY":
            childNode.x += 2
            childNode.agentAlignment = "STAND_STRAIGHT"

        elif childNode.agentAlignment == "LAY_VERTICALLY":
             childNode.x += 1
        return childNode

    def move_left(self):
        childNode = agentNode(self.x, self.y, self.agentAlignment, self, self.board)

        if childNode.agentAlignment == "STAND_STRAIGHT":
            childNode.agentAlignment = "LAY_HORIZONTALLY"
            childNode.x -= 2

        elif childNode.agentAlignment == "LAY_HORIZONTALLY":
            childNode.x -= 1
            childNode.agentAlignment = "STAND_STRAIGHT"

        elif childNode.agentAlignment == "LAY_VERTICALLY":
            childNode.x -= 1

        return childNode 

    # FOR CASE SPLIT
    def split_move_up(self):
        childNode = agentNode(self.x, self.y, self.agentAlignment, self, self.board, self.x1, self.y1)
        childNode.y -= 1
        return childNode 

    def split_move_down(self):
        childNode = agentNode(self.x, self.y, self.agentAlignment, self, self.board, self.x1, self.y1)
        childNode.y += 1
        return childNode 


    def split_move_left(self):
        childNode = agentNode(self.x, self.y, self.agentAlignment, self, self.board, self.x1, self.y1)
        childNode.x -= 1
        return childNode 


    def split_move_right(self):
        childNode = agentNode(self.x, self.y, self.agentAlignment, self, self.board, self.x1, self.y1)
        childNode.x += 1
        return childNode 

    def split1_move_up(self):
        childNode = agentNode(self.x, self.y, self.agentAlignment, self, self.board, self.x1, self.y1)
        childNode.y1 -= 1
        return childNode 

    def split1_move_down(self):
        childNode = agentNode(self.x, self.y, self.agentAlignment, self, self.board, self.x1, self.y1)
        childNode.y1 += 1
        return childNode 

    def split1_move_left(self):
        childNode = agentNode(self.x, self.y, self.agentAlignment, self, self.board, self.x1, self.y1)
        childNode.x1 -= 1
        return childNode 

    def split1_move_right(self):
        childNode = agentNode(self.x, self.y, self.agentAlignment, self, self.board, self.x1, self.y1)
        childNode.x1 += 1
        return childNode 

    def disPlayPosition(self):
        if self.agentAlignment != "SPLIT":
            print(self.agentAlignment, self.x, self.y)
        else:
            print(self.agentAlignment, self.x, self.y, self.x1, self.y1)
    
    def disPlayBoard(self):
        
        # local definition
        x   = self.x
        y   = self.y
        x1  = self.x1
        y1  = self.y1
        agentAlignment = self.agentAlignment
        board = self.board

        # let's go

        if agentAlignment != "SPLIT":
            
            for i in range(len(board)): # for ROW
                print("",end='  ')
                for j in range(len(board[i])): # for COL in a ROW

                    if (i==y and j==x and agentAlignment=="STAND_STRAIGHT") or \
                            ((i==y and j==x) or (i==y and j==x+1) and agentAlignment=="LAY_HORIZONTALLY") or \
                            ((i==y and j==x) or (i==y+1 and j==x) and agentAlignment=="LAY_VERTICALLY"):

                        print("x",end=' ')

                    elif(board[i][j]==0):
                        print(" ",end=' ')
                    else:
                        print(board[i][j], end=' ')
                print("")
        else: # CASE SPLIT
            for i in range(len(board)): # for ROW
                print("",end='  ')
                for j in range(len(board[i])): # for COL

                    if (i==y and j==x) or (i==y1 and j==x1):
                        print("x",end=' ')

                    elif(board[i][j]==0):
                        print(" ",end=' ')
                    else:
                        print(board[i][j], end=' ')
                print("")
            
    
# Case 3: Chữ X
def isNumberThree(agent,x,y):
    board = agent.board

    for item in ManaBoa:

        if (x,y) ==  (item[0], item[1]):

            # TOGGLEEEE

            numToggle = item[2]   # num toggle
            index = 2   # index to check more element

            for i in range(numToggle):    # traverse toggle array
                bX = item[2*i+3]
                bY = item[2*i+4]
                if board[bX][bY] == 0:
                    board[bX][bY] = 1
                else:
                    board[bX][bY] = 0
        
            index = index + 1 + 2 * numToggle

            # CLOSEEEE

            # check if "item" has more element
            if index < len(item):   # case has more

                # read num close
                numClose = item[index]

                # traverse list close if num > 0
                for i in range(numClose):
                    bX = item[index+2*i+1]
                    bY = item[index+2*i+2]
                    board[bX][bY]=0

                index = index + 1 + 2 * numClose
            

            # OPEENNNN

            # check if "item" has more element
            if index < len(item):   # case also has more item
                # get num open
                numOpen = item[index]

                # traverse list open if num > 0
                for i in range(numOpen):
                    bX = item[index+2*i+1]
                    bY = item[index+2*i+2]
                    board[bX][bY]=1



# Case 4: Cục tròn đặc (only đóng).
def isNumberFour(agent,x,y):
    board = agent.board
    
    #print("(x-y) = (", x,"-", y,")")

    for item in ManaBoa:
        if (x,y) ==  (item[0], item[1]):
            num = item[2]
            for i in range(num):
                bX = item[2*i+3]
                bY = item[2*i+4]
                board[bX][bY] = 0

# Case 5: Cục tròn đặc (toggle)
def isNumberFive(agent,x,y):
    board = agent.board

    for item in ManaBoa:
        if (x,y) ==  (item[0], item[1]):


            numToggle = item[2]     # numtoggle
            index = 2   # index to check more element

            for i in range(numToggle):
                bX = item[2*i+3]
                bY = item[2*i+4]
                if board[bX][bY] == 0:
                    board[bX][bY] = 1
                else:
                    board[bX][bY] = 0
            
            index = index + 1 + 2 * numToggle

            # CLOSEEEE

            # check if "item" has more element
            if index < len(item):   # case has more

                # read num close
                numClose = item[index]
                    
                # traverse list close if num > 0
                for i in range(numClose):
                    bX = item[index+2*i+1]
                    bY = item[index+2*i+2]
                    board[bX][bY]=0

                index = index + 1 + 2 * numClose
            

            # OPEENNNN

            # check if "item" has more element
            if index < len(item):   # case also has more item
                # get num open
                numOpen = item[index]

                # traverse list open if num > 0
                for i in range(numOpen):
                    bX = item[index+2*i+1]
                    bY = item[index+2*i+2]
                    board[bX][bY]=1


# Case 6: Cục tròn đặc (only mở)
def isNumberSix(agent,x,y):
    board = agent.board

    for item in ManaBoa:
        if (x,y) ==  (item[0], item[1]):
            num = item[2]
            for i in range(num):
                bX = item[2*i+3]
                bY = item[2*i+4]
                board[bX][bY] = 1

# Case 7: Cục phân thân
def isNumberSeven(agent,x,y):  
    array = []    
    for item in ManaBoa:
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

# Case 8: Chữ X (only mở)
def isNumberEight(agent,x,y):
    board = agent.board

    for item in ManaBoa:
        if (x,y) ==  (item[0], item[1]):

            num = item[2]
            for i in range(num):
                bX = item[2*i+3]
                bY = item[2*i+4]
                board[bX][bY] = 1




# isValidBLock
def isValidBlock(agent):
    
    if isFloor(agent):
        
        # local definition
        x     = agent.x
        y     = agent.y
        x1    = agent.x1
        y1    = agent.y1
        agentAlignment   = agent.agentAlignment
        board = agent.board
        
        
        # Case 2: Đo đỏ
        if agentAlignment == "STAND_STRAIGHT" and board[y][x] == 2:
            return False 

        # Case 3: Chữ X
        if agentAlignment == "STAND_STRAIGHT" and board[y][x] == 3:
            isNumberThree(agent,x,y)
        
        # Case 4: Cục tròn đặc (only đóng).
        if board[y][x] == 4:
            isNumberFour(agent,x,y)
        if agentAlignment == "LAY_HORIZONTALLY" and board[y][x+1] == 4:
            isNumberFour(agent,x+1,y)
        if agentAlignment == "LAY_VERTICALLY" and board[y+1][x] == 4:
            isNumberFour(agent,x,y+1)
        if agentAlignment == "SPLIT" and board[y1][x1] == 4:
            isNumberFour(agent,x1,y1)


        # Case 5: Cục tròn đặc (toggle)
        if board[y][x] == 5:
            isNumberFive(agent,x,y)
        if agentAlignment == "LAY_HORIZONTALLY" and board[y][x+1] == 5:
            isNumberFive(agent,x+1,y)
        if agentAlignment == "LAY_VERTICALLY" and board[y+1][x] == 5:
            isNumberFive(agent,x,y+1)
        if agentAlignment == "SPLIT" and board[y1][x1] == 5:
            isNumberFive(agent,x1,y1)

        # Case 6: Cục tròn đặc (only mở)
        if board[y][x] == 6:
            isNumberSix(agent,x,y)
        if agentAlignment == "LAY_HORIZONTALLY" and board[y][x+1] == 6:
            isNumberSix(agent,x+1,y)
        if agentAlignment == "LAY_VERTICALLY" and board[y+1][x] == 6:
            isNumberSix(agent,x,y+1)
        if agentAlignment == "SPLIT" and board[y1][x1] == 6:
            isNumberSix(agent,x1,y1)

        # Case 7: Phân thân 
        if agentAlignment == "STAND_STRAIGHT" and board[y][x] == 7:
            isNumberSeven(agent,x,y)
        # Case7_1: MERGE BLOCK
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

        # Case 8: Chữ X (only mở)
        if agentAlignment == "STAND_STRAIGHT" and board[y][x] == 8:
            isNumberEight(agent,x,y)
            
        return True
    else:
        return False


def isFloor(agent):
    x = agent.x
    y = agent.y
    agentAlignment = agent.agentAlignment
    board = agent.board
    
    if x >= 0 and y >= 0 and \
            y < MAP_ROW and x < MAP_COL and \
            board[y][x] != 0:

        if agentAlignment == "STAND_STRAIGHT":
            return True
        elif agentAlignment == "LAY_VERTICALLY":
            if y+1 < MAP_ROW and board[y+1][x] != 0 :
                return True
        elif agentAlignment == "LAY_HORIZONTALLY":
            if x+1 < MAP_COL and board[y][x+1] != 0 :
                return True
        else: # case SPLIT
            x1 = agent.x1
            y1 = agent.y1

            if x1 >= 0 and y1 >= 0 and \
                y1 < MAP_ROW and x1 < MAP_COL and \
                board[y1][x1] != 0:
                    return True

    else:
        return False


def isVisited(agent):
    if agent.agentAlignment != "SPLIT":

        for item in passState:
            if item.x == agent.x     and item.y == agent.y and \
                item.agentAlignment == agent.agentAlignment and item.board == agent.board:
                return True

    else: # case SPLIT
        for item in passState:
            if item.x  == agent.x     and item.y  == agent.y and \
               item.x1 == agent.x1    and item.y1 == agent.y1 and \
                item.agentAlignment == agent.agentAlignment and item.board == agent.board:
                return True

    return False

def move(Stack, agent, flag):

    if isValidBlock(agent):
        if isVisited(agent):
            return None

        Stack.append(agent)
        passState.append(agent)
        #print(flag)
        return True 

    return False   

def printSuccessRoad(agent):
    
    print("================================")
    
    successRoad = [agent]
    temp = agent.parentNode
    
    while temp != None:
        
        if temp.agentAlignment != "SPLIT":
            childNode = agentNode(temp.x, temp.y, \
                    temp.agentAlignment, temp.parentNode, temp.board)
        else: # case SPLIT
            childNode = agentNode(temp.x, temp.y, \
                    temp.agentAlignment, temp.parentNode, temp.board, temp.x1, temp.y1)

        successRoad = [childNode] + successRoad
        
        temp = temp.parentNode
    
    step = 0
    for item in successRoad:
        step += 1
        print("\nStep:", step, end=' >>>   ')
        item.disPlayPosition()
        print("=============================")
        item.disPlayBoard()

    print("COMSUME",step,"STEP!!!!")


#*****************************************************************************
#
#   goalMet() checks & return True if agent is standing straight    
#   & its location on specified terrain is same as goal location
#
#*****************************************************************************

def goalMet(agent):
   
    if agent.agentAlignment == "STAND_STRAIGHT" and agent.board[agent.y][agent.x] == 9:
        return True
    else:
        return False

#*****************************************************************************
#
#
#
#
#
#
#
#
#*****************************************************************************

def breadthFirstSearch(agent):

    frontier = []
    frontier.append(agent)
    passState.append(agent)

    virtualStep = 0

    while frontier:
        current = frontier.pop(0)

        if goalMet(current):
            printSuccessRoad(current)
            print("SUCCESS")
            print("COMSUME", virtualStep, "VIRTUAL STEP")
            return True

        if current.agentAlignment != "SPLIT":
            virtualStep += 4

            move(frontier,current.move_up(), "up")
            move(frontier,current.move_right(), "right")
            move(frontier,current.move_down(), "down")
            move(frontier,current.move_left(), "left")
        else: 
            virtualStep += 8

            move(frontier,current.split_move_left(), "left0")
            move(frontier,current.split_move_right(), "right0")
            move(frontier,current.split_move_up(), "up0")
            move(frontier,current.split_move_down(), "down0")
            
            move(frontier,current.split1_move_left(), "left1")
            move(frontier,current.split1_move_right(), "right1")
            move(frontier,current.split1_move_up(), "up1")
            move(frontier,current.split1_move_down(), "down1")
    return False


#*****************************************************************************
#
#   Main Program starts here
#
#   1) Invoke getTerrain() & obtain terrain alongwith initial position of agent
#   2) Get agent or block node created  
#   3) Invoke breadFirstSearch() uninformed search
#   4) breadthFirstSearch() invokes step-by-step execution once goal is met
#                
#*****************************************************************************

passState = []

MAP_ROW, MAP_COL, xStart, yStart, givenTerrain, ManaBoa = getTerrain('Map/Map.txt')

agent = agentNode(xStart, yStart, "STAND_STRAIGHT", None, givenTerrain)

print("Agent solves Bloxorz game problem using Breadth First Search strategy as below")
breadthFirstSearch(agent)