# -*- coding: utf-8 -*-
# Submitted by Harsh Bhatia (2019AD04086), Alkesh Chaturvedi (2019AD04082), Raza Abbas (2019AD04095)
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
#   1) Read giveMap variable and prepares givenTerrain
#   2) Display Map or Terrain (Level-1)  
#    
#*****************************************************************************

def getTerrain(givenMap):
    
    givenTerrain   = []
    mapLength      = len(givenMap)
  
    for getTerrainCtr in range(0,mapLength):
        givenTerrain.append([int(x) for x in givenMap[getTerrainCtr]])
    
    print("\nPlease Note: Board starts (Topmost Left tile) at x-coordinate = 1 & y-coordinate = 1")
    print("Any references to x and y coordinates hereon should be read accordingly")
    print("**************************************************")

    print("Input board is displayed below such that 1 = valid tile, 0 = void location & 9 = goal location")
    print("**************************************************")
    for val in givenTerrain:
        print(val)
    print("**************************************************")

    print("\nStarting position of agent on playing board is at ( x-coordinate =",xInitial + 1, "and y-coordinate =", yInitial + 1,")")
    print("**************************************************")
    
    return givenTerrain

#*****************************************************************************
#
#   agentNode class declares different agent variables and agent functions
#   to manipulate agent variable values
#    
#*****************************************************************************

class agentNode:

    def __init__(self, x, y, agentAlignment, parentNode, playingCourt, action=None):
        self.x                  = x
        self.y                  = y
        self.agentAlignment     = agentAlignment  
        self.parentNode         = parentNode
        self.playingCourt       = copy.deepcopy(playingCourt)
        self.action             = action

    def goRight(self):
        childNode = agentNode(self.x, self.y, self.agentAlignment, self, self.playingCourt, self.action)

        childNode.action            = " goes right"    
        
        if childNode.agentAlignment == "standing straight":
           childNode.agentAlignment = "laying horizontally"
           childNode.x = childNode.x + 1
        elif childNode.agentAlignment == "laying horizontally":
           childNode.agentAlignment = "standing straight"
           childNode.x = childNode.x + 2
        elif childNode.agentAlignment == "laying vertically":
           childNode.x = childNode.x + 1
           
        return childNode

    def goLeft(self):
        childNode = agentNode(self.x, self.y, self.agentAlignment, self, self.playingCourt, self.action)

        childNode.action            = " goes left"
        
        if childNode.agentAlignment == "standing straight":
           childNode.agentAlignment = "laying horizontally"
           childNode.x = childNode.x - 2
        elif childNode.agentAlignment == "laying horizontally":
           childNode.agentAlignment = "standing straight"
           childNode.x = childNode.x - 1
        elif childNode.agentAlignment == "laying vertically":
           childNode.x = childNode.x - 1

        return childNode 
    
    def goUp(self):
        childNode = agentNode(self.x, self.y, self.agentAlignment, self, self.playingCourt, self.action)

        childNode.action            = " goes up"
        
        if childNode.agentAlignment == "standing straight":
           childNode.agentAlignment = "laying vertically"
           childNode.y = childNode.y - 2
        elif childNode.agentAlignment == "laying horizontally":
           childNode.y = childNode.y - 1
        
        elif childNode.agentAlignment == "laying vertically":
           childNode.agentAlignment = "standing straight"
           childNode.y = childNode.y - 1
        
        return childNode 

    def goDown(self):
        childNode = agentNode(self.x, self.y, self.agentAlignment, self, self.playingCourt, self.action)

        childNode.action            = " goes down"
        
        if childNode.agentAlignment == "standing straight":
           childNode.agentAlignment = "laying vertically"
           childNode.y = childNode.y + 1
        elif childNode.agentAlignment == "laying horizontally":
           childNode.y = childNode.y + 1

        elif childNode.agentAlignment == "laying vertically":
           childNode.agentAlignment = "standing straight"
           childNode.y = childNode.y + 2
           
        return childNode 

    def showAgentLocation(self):
        
        print("Agent" , self.action, "on board: ", self.agentAlignment, " at x-coordinate = ", self.x + 1, "and y-coordinate = ", self.y + 1)
    
    def showBoard(self):
        
        x   = self.x
        y   = self.y
    
        agentAlignment = self.agentAlignment
        playingCourt = self.playingCourt
    
    
        for i in range(len(playingCourt)):
            print("",end='  ')
            for j in range(len(playingCourt[i])):

                if (i==y and j==x and agentAlignment=="standing straight") or \
                        ((i==y and j==x) or (i==y and j==x+1) and agentAlignment=="laying horizontally") or \
                        ((i==y and j==x) or (i==y+1 and j==x) and agentAlignment=="laying vertically"):

                    print("x",end=' ')

                elif(playingCourt[i][j]==0):
                    print(" ",end=' ')
                else:
                    print(playingCourt[i][j], end=' ')
            print("")
            
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

        if agentAlignment   == "standing straight":
           return True
        elif agentAlignment == "laying horizontally":
           if x+1 < colLimit and playingCourt[y][x+1] != 0 :
              return True
        elif agentAlignment == "laying vertically":
           if y+1 < rowLimit and playingCourt[y+1][x] != 0 :
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

    for node in tempState:
        if node.x == agent.x and node.y == agent.y and node.agentAlignment == agent.agentAlignment and node.playingCourt == agent.playingCourt:
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

    if checkFloor(agent):
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
        
        childNode = agentNode(holdNode.x, holdNode.y,holdNode.agentAlignment,holdNode.parentNode,holdNode.playingCourt,holdNode.action)

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
   
    if agent.agentAlignment == "standing straight" and agent.playingCourt[agent.y][agent.x] == 9:
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

       crawl(frontier,current.goRight())
       crawl(frontier,current.goLeft())
       crawl(frontier,current.goUp())
       crawl(frontier,current.goDown())

    return False

#*****************************************************************************
#
#                   MAIN PROGRAM STARTS HERE
#
#   1) Input board for agent as a Map. Also input start position of agent  
#   2) Invoke getTerrain() & obtain playing Court or board for agent to crawl
#   3) Get agent or block node created  
#   4) Invoke breadFirstSearch() uninformed search
#                
#*****************************************************************************
#
#                INPUT AREA FOR PROGRAM STARTS HERE
#
# Enter playing board here
# Topmost left tile is at x-coordinate = 1, y-coordinate = 1
#
givenMap = [[1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 1, 1, 9, 1, 1],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 0]] 
#
# Enter Agent or Block start position as [x-coordinate, y-coordinate]:
# x-coordinate = corresponding column value on playing board
# y-coordinate = corresponding row value on playing board
# 
# Agent at topmost left tile will have startAt = [1,1]   
# Please enter agent's startAt position accordingly...  
#
startAt = [1,1]
#
#
#                INPUT AREA FOR PROGRAM ENDS HERE
#                
#*****************************************************************************

xInitial  = int(startAt[0]) - 1
yInitial  = int(startAt[1]) - 1

rowLimit = len(givenMap)
colLimit = len(givenMap[0])
    
givenTerrain = getTerrain(givenMap)

tempState = []

agent = agentNode(xInitial, yInitial, "standing straight", None, givenTerrain, "is")

print("Checking for Agent's starting position...")

if checkFloor(agent):
    print("Agent's start position found to be legal. Proceeding further...")
    print("Agent solves Bloxorz game problem using Breadth First Search strategy as below")
    breadthFirstSearch(agent)
else:
    print("Agent starting position is found to be illegal. Agent is not a valid tile on playing court")
    print("Agent's x-coordinate can be between 1 and",colLimit, "on a valid tile & not a void location")
    print("Agent's y-coordinate can be between 1 and",rowLimit, "on a valid tile & not a void location")

#
#                   MAIN PROGRAM ENDS HERE
#                
#*****************************************************************************