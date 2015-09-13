from unblock import *
from copy import copy, deepcopy
import os
import time



grid=createfield()
pgame(grid)

cars=["HT1","HT2","HC1","MC1","VT1","VT2","VC1","VC2"]
anodes=[]
openList=[]
closedList=[]
###
depth=1
width=1
###

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

def cls():
    os.system(['clear','cls'][os.name == 'nt'])

def stats(grid):
    #Update screen with vitals
    time.sleep(.5)
    cls()
    print " "
    print " "
    print " "
    print " "
    pgame(grid)
    print "Number of states created",len(anodes)
    print "Length of path", depth
    print "Open List length", len(openList)
    print "Closed List length", len(closedList)

def newNode(currentGrid):
    #check to make sure Node not previously created
    existPreviously = False
    for elem in anodes:
        if currentGrid == elem.matrix:
            existPreviously = True

    if existPreviously == False:
        #New Node
        anodes.append(Node(depth,width,currentGrid))
        openList.append(anodes[len(anodes)-1])
        stats(currentGrid)




#Try all moves for all cars and store states for them
def makeChildren(grid):
    #for each car
    currentGrid = gridCopy(grid)
    for elem in cars:

        #try up, if yes...
        if up(currentGrid, elem) == "Done":
            newNode(currentGrid)
            currentGrid = gridCopy(grid)
            if down(currentGrid, elem) == "Done":
                newNode(currentGrid)

        #try down, if yes..
        elif down(currentGrid, elem) == "Done":
            newNode(currentGrid)
            currentGrid = gridCopy(grid)
            if up(currentGrid, elem) == "Done":
                newNode(currentGrid)

            #try left, if yes..
        elif left(currentGrid, elem) == "Done":
            newNode(currentGrid)
            currentGrid = gridCopy(grid)
            if right(currentGrid, elem) == "Done":
                newNode(currentGrid)

            #try right, if yes..
        elif right(currentGrid, elem) == "Done":
            newNode(currentGrid)
            currentGrid = gridCopy(grid)
            if left(currentGrid, elem) == "Done":
                newNode(currentGrid)

        else:
            stats(grid)
            print "No New Children"
