from unblock import *

cars=["HT1","HT2","HC1","MC1","VT1","VT2","VC1","VC2"]
anodes=[]
goal=25000  #yeah?
currentNode=0

grid=createfield()
pgame(grid)


class Node(object):
    #States visited by algorithm
    def __init__(self, depth, width, matrix):
        self.depth = depth
        self.width = width
        self.matrix = matrix

anodes.append(Node(depth,width,grid))

for depth in goal
    for width in goal

#New Node
anodes.append(Node(depth,width,grid))

#i don't even know
currentNode+=1


for elem in cars:
    if up(currentGrid, cars) == "Done":
        "yay - up"


        #New Node
        anodes.append(Node(depth,width,grid))


        #Update screen with vitals
        pgame(grid)
        print "Notes visited",len(Node)
        print "Length of path", depth
        print "Open List length"
        print "Closed List length"

    if down(anodes[currentNode].matrix, cars) == "Done":
        "yay - down"
        #Node.matrix=gridname
    if left(anodes[currentNode].matrix, cars) == "Done":
        "yay - left"
        #Node.matrix=gridname
    if right(anodes[currentNode].matrix, cars) == "Done":
        "yay - right"
        #Node.matrix=gridname


    if evaluate(grid)=="WON"
        goal=width
