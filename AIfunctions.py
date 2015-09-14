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
path = 1
widthCounter = 1

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
    #time.sleep(.5)
    cls()
    print " "
    print " "
    print " "
    print " "
    print "anodes[",len(anodes)-1,"]"
    pgame(grid)
    print "Number of states created",len(anodes)
    print "Length of path", path
    print "Open List length", len(openList)
    print "Closed List length", len(closedList)

def newNode(currentGrid, depth):
    #check to make sure Node not previously created
    existPreviously = False
    for elem in anodes:
        if currentGrid == elem.matrix:
            existPreviously = True
            print "this node has already existed, I'm not making a new node for you"
    if existPreviously == False:
        print "making a new node for ya"
        #New Node
        global widthCounter
        anodes.append(Node(depth,widthCounter,currentGrid))
        widthCounter+=1
        openList.append(anodes[len(anodes)-1])
        stats(currentGrid)




#Try all moves for all cars and store states for them
def makeChildren(grid, depth):

    #for each car
    currentGrid = gridCopy(grid)
    for elem in cars:

        #try up, if yes...
        if up(currentGrid, elem) == "Done":
            print "Moved up car", elem
            newNode(currentGrid, depth)

            currentGrid = gridCopy(grid)
            if down(currentGrid, elem) == "Done":
                newNode(currentGrid, depth)

        #try down, if yes..
        elif down(currentGrid, elem) == "Done":
            print "Moved down car", elem
            newNode(currentGrid, depth)

            currentGrid = gridCopy(grid)
            if up(currentGrid, elem) == "Done":
                newNode(currentGrid, depth)

            #try left, if yes..
        elif left(currentGrid, elem) == "Done":
            print "Moved left car", elem
            newNode(currentGrid, depth)

            currentGrid = gridCopy(grid)
            if right(currentGrid, elem) == "Done":
                newNode(currentGrid, depth)

            #try right, if yes..
        elif right(currentGrid, elem) == "Done":
            print "Moved right car", elem
            newNode(currentGrid, depth)

            currentGrid = gridCopy(grid)
            if left(currentGrid, elem) == "Done":
                newNode(currentGrid, depth)

        else:
            print "tried car", elem, " and No New Children"
