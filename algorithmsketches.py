from AIfunctions import *




def visitedPreviously(node):
    existPreviously = False
    for elem in closedList:
        if node == elem:
            existPreviously = True
            return existPreviously
        else:
            return existPreviously

def nodeAtDepthWidth(depth, width):
    nodePresent = False
    for elem in anodes:
        if elem.depth == depth and elem.width == width:
            nodePresent = True
            return nodePresent
        else:
            return nodePresent


def breadth():
    print "Declare variables"
    depth=1
    width=1
    bigNumber = 1000
    currentNode = 0

    print "Store Initial State"
    #Store Initial State
    anodes.append(Node(depth,width,gridCopy(grid)))


    for x in range(bigNumber):
        depth=x+1
        print "Depth is now", depth
        for y in range(bigNumber):
            width = y+1
            print "Width is now", width
            #if there is NOT a node at the current depth and width
            if nodeAtDepthWidth(depth, width) == False:
                #go to line 28
                currentNode+=1
                print "There is no node at current depth and width", depth, ":", width
                print "Moving to node", currentNode
                break


            #if there is a node at the current depth and width
            if nodeAtDepthWidth(depth, width) == True:
                print "There is a node at current depth and width", depth, ":", width
                if visitedPreviously(anodes[currentNode]) == False:
                    #Assign Depth + Width

                    anodes[currentNode].depth=depth
                    anodes[currentNode].width=width

                    #evaluate
                    if evaluate(anodes[currentNode]) == "WON":
                        stats(anodes[currentNode].matrix)
                    elif evaluate(anodes[currentNode]) == "NOT YET":
                        #Make Children of initial state
                        makeChildren(anodes[currentNode].matrix)


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
