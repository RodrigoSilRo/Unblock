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
