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


def breadth():
    print "Declare variables"
    depth=1
    width=1
    bigNumber = 100000
    currentNode = 0
    gameWon = False
    counterNewKids = 0

    cls()

    print "Store Initial State"
    #Store Initial State
    anodes.append(Node(depth,width,gridCopy(grid)))
    openList.append(anodes[0])

    for x in range(bigNumber):
        if gameWon == True:
            print "Should stop now"
            break
        elif gameWon == False:
            depth=x+1
            global tree
            tree = depth
            #reset width counter
            print "widthCounter reset"
            global widthCounter
            widthCounter=1
            counterDown=counterNewKids
            counterNewKids=0
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
                        print "Length of path is:", anodes[currentNode].depth
                        print "WINNERWINNERWINNERWINNERWINNERWINNERWINNERWINNERWINNERWINNERWINNERWINNERWINNERWINNER"
                        return
                    elif evaluate(anodes[currentNode].matrix) == "NOT YET":
                        print "Not Winner"

                        #remove from open list
                        print "currentNode ", currentNode
                        openList.remove(anodes[currentNode])
                        print "Removed from open list"
                        #add to closed list
                        closedList.append(anodes[currentNode])
                        counterDown-=1
                        print "Added to Closed list"
                        print "Length of Closed list", len(closedList)

                        beforeBirth = len(anodes)


                        #Make Children of current state
                        makeChildren(anodes[currentNode].matrix, (anodes[currentNode].depth)+1)
                        print "Children made!"

                        afterBirth = len(anodes)

                        counterNewKids+=afterBirth-beforeBirth

                        #if there is a node at current depth and next width
                        if counterDown>1:
                                print "there should still be nodes left to breadthify"
                                if visitedPreviously(anodes[currentNode]) == False:
                                    #Go to next node
                                    currentNode+=1
                                    width+=1
                                    print "Now headed for node", currentNode, "depth and with", depth, ":", width
                                    #raw_input("presskeytoadvance")

                        #if there is NOT a node at the current depth and next width
                        else:
                            #go to line 28
                            currentNode+=1

                            print "There is no node at next depth and next width", depth, ":", width+1
                            print "Moving to node", currentNode
                            #raw_input("presskeytoadvance")
                            break


                    #evaluate for winner
                    if evaluate(anodes[currentNode].matrix) == "WON":
                        stats(anodes[currentNode].matrix)
                        gameWon == True
                        print "WINNERWINNERWINNERWINNERWINNer"
                        break


                else:
                    print "Node SHOCKINGLY already visited"
                    #Go to next node
                    #raw_input("presskeytoadvance")
                    currentNode+=1

                #evaluate for winner
                if evaluate(anodes[currentNode].matrix) == "WON":
                    stats(anodes[currentNode].matrix)
                    gameWon == True
                    print "WINNERR"
                    break



def depth():
    print "Declare variables"
    depth=1
    width=1
    bigNumber = 100000
    currentNode = 0
    gameWon = False
    counterNewKids = 0
    previousNodesAtWidth = 0
    openListTotal = []
    listCounter = 0

    cls()

    print "Store Initial State"
    #Store Initial State
    anodes.append(Node(depth,width,gridCopy(grid)))
    openList.append(anodes[0])


    for x in range(bigNumber):

        #if is not in closed list
        if visitedPreviously(anodes[currentNode]) == False:
            print "Next node to be evaluated and procreated is:", openList[0].depth, openList[0].width, openList[0]
            #evaluate for winner
            if evaluate(openList[0].matrix) == "WON":
                stats(openList[0].matrix)
                gameWon == True
                print "WINNERWINNERWINNERWINNERWINNERWINNERWINNERWINNERWINNERWINNERWINNERWINNERWINNERWINNER"
                return
            elif evaluate(openList[0].matrix) == "NOT YET":
                print "Not Winner"

                #make Children
                beforeBirth = len(anodes)
                print "beforeBirth ", beforeBirth

                previousNodesAtWidth=0

                #set widthCounter
                for elem in anodes:
                    print "Looking for nodes at same depth as children to be made"
                    if elem.depth == openList[0].depth+1:
                        previousNodesAtWidth+=1
                        print "New node found at depth, total now= ", previousNodesAtWidth

                widthCounter = previousNodesAtWidth


                #Make Children of current state
                makeChildren(openList[0].matrix, openList[0].depth+1)
                print "Children made!"

                afterBirth = len(anodes)
                print "afterBirth ", afterBirth


                #add children to openListTotal
                for elem in openList:
                    openListTotal.insert(elem, listCounter)
                    listCounter+=1

                #reset listCounter
                listCounter=0
                #reset openList
                openList=[]

                #add to closed list
                closedList.append(openList[0])
                print "Added to Closed list"
                print "Length of Closed list", len(closedList)
                for elem in closedList:
                    print elem.depth, ":", elem.width, elem
                #remove from open list
                print "currentNode ", currentNode
                openList.remove(openList[0])
                print "Removed from open list"
                print "Length of open List", len(openList)

                raw_input("waitingforkeypress")

        else:
            print "Node SHOCKINGLY already visited"
            #Go to next node
            #raw_input("presskeytoadvance")
