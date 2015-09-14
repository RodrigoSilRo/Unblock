from AIfunctions import *




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
            break
        elif gameWon == False:
            depth=x+1
            path = depth
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
                        break
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
                                    raw_input("presskeytoadvance")

                        #if there is NOT a node at the current depth and next width
                        else:
                            #go to line 28
                            currentNode+=1

                            print "There is no node at next depth and next width", depth, ":", width+1
                            print "Moving to node", currentNode
                            raw_input("presskeytoadvance")
                            break





                else:
                    print "Node SHOCKINGLY already visited"
                    #Go to next node
                    raw_input("presskeytoadvance")
                    currentNode+=1





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
