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

def nodeAtDepthWidth(depth, width):
    print "looking for next node over within function"
    #nodePresent = False
    for elem in anodes:
        print elem.depth, elem.width
        if elem.depth == depth and elem.width == width:
            #nodePresent = True
            print "next node over has been found"
            #return nodePresent
        else:
            print "there is no node next over"
            #return nodePresent


def breadth():
    print "Declare variables"
    depth=1
    width=1
    bigNumber = 100000
    currentNode = 0
    gameWon = False


    cls()

    print "Store Initial State"
    #Store Initial State
    anodes.append(Node(depth,width,gridCopy(grid)))
    openList.append(anodes[0])

    for x in range(bigNumber):
        if gameWon == True:
            break
        elif gameWon == False:
            depth=x+1
            path = depth
            #reset width counter
            global widthCounter
            widthCounter=1
            print "Width counter reset should now be 1, but it is ", widthCounter
            print "Depth is now", depth
            for y in range(bigNumber):
                width = y+1
                print "Width is now", width

                #if is not in closed list
                if visitedPreviously(anodes[currentNode]) == False:

                    #evaluate for winner
                    if evaluate(anodes[currentNode].matrix) == "WON":
                        stats(anodes[currentNode].matrix)
                        gameWon == True
                        break
                    elif evaluate(anodes[currentNode].matrix) == "NOT YET":
                        print "Not Winner"

                        #remove from open list
                        print "currentNode ", currentNode
                        openList.remove(anodes[currentNode])
                        print "Removed from open list"
                        #add to closed list
                        closedList.append(anodes[currentNode])
                        print "Added to Closed list"
                        print "Length of Closed list", len(closedList)


                        #Make Children of current state
                        makeChildren(anodes[currentNode].matrix, (anodes[currentNode].depth)+1)

                        #if there is NOT a node at the current depth and next width
                        if nodeAtDepthWidth(depth, width+1) == False:
                            #go to line 28
                            currentNode+=1

                            print "There is no node at next depth and next width", depth, ":", width+1
                            print "Moving to node", currentNode
                            stopping=raw_input('Waiting for poke')
                            break


                        #if there is a node at the current depth and next width
                        if nodeAtDepthWidth(depth, width+1) == True:
                            print "There is a node at current depth and next width", depth, ":", width+1
                            if visitedPreviously(anodes[currentNode]) == False:
                                #Go to next node
                                currentNode+=1
                                width+=1
                                print "Now headed for node", currentNode, "depth and with", depth, ":", width
                                stopping=raw_input('Waiting for poke')
                else:
                    print "Node SHOCKINGLY already visited"
                    #Go to next node
                    currentNode+=1
                    stopping=raw_input('Waiting for poke')




def depth():


    """
    1:1
    2:1
    3:1
    4:1
    5:1
    2:2
    3:2
    4:2
    """
