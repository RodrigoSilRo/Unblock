from unblock import *
from copy import copy, deepcopy

cars=["HT1","HT2","HC1","MC1","VT1","VT2","VC1","VC2"]
anodes=[]
goal=25000  #yeah?
currentNode=0

grid=createfield()
pgame(grid)

cars=["HT1","HT2","HC1","MC1","VT1","VT2","VC1","VC2"]
anodes=[]
openList=[]
closedList=[]


class Node(object):
    #States visited by algorithm
    def __init__(self, depth, width, matrix):
        self.depth = depth
        self.width = width
        self.matrix = matrix

#Use function to copy grids to and from Nodes
def gridCopy(oldMatrix):
    newMatrix = deepcopy(oldMatrix)
    return newMatrix

#Try all moves for all cars and store states for them
def makeChildren(grid):
    #for each car

    for elem in cars:


        #try up, if yes...
        currentGrid=gridCopy(grid)
        if up(currentGrid, elem) == "Done":
            print "up"
            #New Node
            anodes.append(Node(depth,width,currentGrid))
            openList.append(anodes[len(anodes)-1])

        #try down, if yes..
        currentGrid=gridCopy(grid)
        if down(currentGrid, elem) == "Done":
            print "down"
            #New Node
            anodes.append(Node(depth,width,currentGrid))
            openList.append(anodes[len(anodes)-1])

        #try left, if yes..
        currentGrid=gridCopy(grid)
        if left(currentGrid, elem) == "Done":
            print "left"
            #New Node
            anodes.append(Node(depth,width,currentGrid))
            openList.append(anodes[len(anodes)-1])

        #try right, if yes..
        currentGrid=gridCopy(grid)
        if right(currentGrid, elem) == "Done":
            print "right"
            #New Node
            anodes.append(Node(depth,width,currentGrid))
            openList.append(anodes[len(anodes)-1])
