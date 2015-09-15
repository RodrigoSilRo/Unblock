from unblock import *
from copy import copy, deepcopy
import os
import time
import sys


grid=createfield()
pgame(grid)

cars=["HT1","HT2","HC1","MC0","VT1","VT2","VC1","VC2"]
anodes=[]
openList=[]
closedList=[]
path = 1
tree = 1
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
    #time.sleep(.15)
    cls()
    print " "
    print " "
    print " "
    print " "
    print "anodes[",len(anodes)-1,"]"
    pgame(grid)
    print "Number of states created",len(anodes)
    print "Open List length", len(openList)
    print "Closed List length", len(closedList)
    #print "Total time elapsed ", time.time()-start

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
        openList.insert(0, anodes[len(anodes)-1])
        print "added node to open list with depth and width ", depth, ":", widthCounter
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




def visitedPreviously(node):

    existPreviously = False
    if len(closedList) == 0:
        print "closed list is blank"
        return existPreviously
    else:
        for elem in closedList:
            if node == elem:
                existPreviously = True
                print "closed list had this node"
                return existPreviously
            else:
                print "node was not in closed list"
                return existPreviously




def iter():
    #start = time.time()
    print "Declare variables"
    depth=1
    width=1
    bigNumber = 100000
    currentNode = 0
    gameWon = False
    counterNewKids = 0
    previousNodesAtWidth = 0
    listCounter = 0

    global closedList

    cls()

    for c in range(bigNumber):

        print "Store Initial State"
        #Store Initial State
        global anodes
        anodes.append(Node(depth,width,gridCopy(grid)))
        global openList
        openList.append(anodes[0])

        for x in range(bigNumber):
            print "openList"
            for elem in openList:
                print elem.depth, elem.width, elem

            #if open list is empty,
            if len(openList) == 0:
                anodes=[]
                openList=[]
                closedList=[]
                print "c =", c
                #raw_input("waiting to BREAK")
                break

            else:

                #if is not in closed list
                if visitedPreviously(openList[0]) == False:
                    print "Next node to be evaluated and procreated is:", openList[0].depth, openList[0].width, openList[0]

                #evaluate for winner
                if evaluate(openList[0].matrix) == "WON":
                    stats(openList[0].matrix)
                    gameWon == True

                    print "WINNERWINNERWINNERWINNERWINNERWINNERWINNERWINNERWINNERWINNERWINNERWINNERWINNERWINNER"
                    return
                elif evaluate(openList[0].matrix) == "NOT YET":
                    print "Not Winner"

                    previousNodesAtWidth=1

                    print "widthCounter info", previousNodesAtWidth
                    #set widthCounter
                    for elem in anodes:
                    #    print "Looking for nodes at same depth as children to be made"
                        if elem.depth == openList[0].depth+1:
                            previousNodesAtWidth+=1
                    #        print "New node found at depth, total now= ", previousNodesAtWidth
                    #    else:
                    #        print "No nodes found at children level depth"

                    global widthCounter
                    widthCounter = previousNodesAtWidth
                    print "after search, widthCounter now ", widthCounter

                   #add to closed list
                    #global closedList
                    closedList.append(openList[0])
                    currentNode
                    print "Added to Closed list", closedList[len(closedList)-1]
                    print "Length of Closed list", len(closedList)

                    currentNode = closedList[len(closedList)-1]

                    #Make Children of current state ONLY IF DEPTH ALLOWED
                    if openList[0].depth < c+1:
                        makeChildren(openList[0].matrix, openList[0].depth+1)
                        print "Children made!"


                    #remove from open list

                    openList.pop(openList.index(currentNode))
                    print "Removed from open list, name: ", currentNode
                    print "Length of open List", len(openList)
                    print "c =", c
                    #raw_input("waitingforkeypress")

            #else:
            #    print "Node SHOCKINGLY already visited"
                #Go to next node

            #    raw_input("presskeytoadvance")
