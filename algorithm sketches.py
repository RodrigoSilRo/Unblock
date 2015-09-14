from AIfuncitons import *

bigNumber = 1000
currentNode = 0


def visitedPreviously(node):
    print "step 1"
        existPreviously = False
        for elem in closedList:
            print "step 2"
            if node == elem:
                print "step 3"
                existPreviously = True
                #return existPreviously
                print existPreviously, "yes"
            else:
                print existPreviously, "no"
                #return existPreviously




def breadth():


"""
1:1
2:1
2:2
2:3
2:4
3:1
3:2
"""


    #Store Initial State
    anodes.append(Node(depth,width,gridCopy(grid)))


    for x in bigNumber
        depth=x+1
        for y in bigNumber
            width = y

            if visitedPreviously(anodes[currentNode]) == False:
                #Assign Depth + Width
                anodes[currentNode].depth=depth
                anodes[currentNode].width=width

                #evaluate
                if evaluate(anodes[currentNode]) == "WON":
                    stats(anodes[currentNode].matrix)
                elif == "NOT YET":
                    #Make Children of initial state
                    makeChildren(anodes[0].matrix)

                currentNode+=1















        closedList.append("""currentNode""")







                if evaluate=="WON":
                    #then stop....   set depth range to current?
                else:
                    width+=1


            down
            left
            right

                if evaluate(currentGrid)=="WON"
                    goal=width

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
