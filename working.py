"""  There is an issue with movements effecting nodes in 'memory'
If I reset the flield, I can create a new node and add to memory.
However, recalling a node means that movements will change the stored matrix.

anodes[index] seems to work fine, but anodes[index].matrix is NOT static

Copy and paste into Python interpreter to see effect in action
"""

from unblock import *

cars=["HT1","HT2","HC1","MC1","VT1","VT2","VC1","VC2"]
anodes=[]
"""
class Node(object):
    #States visited by algorithm
    def __init__(self, depth, width, matrix):
        self.depth = depth
        self.width = width
        self.matrix = matrix
"""

###
grid=createfield()
#0 state node
anodes.append(Node(0,0,grid))
#######################
for elem in anodes:
  print elem, "depth", elem.depth, "width", elem.width
  pgame(elem.matrix)

#######################
grid=createfield()
down(grid, cars[4])
#1 state node
anodes.append(Node(1,1,grid))
#######################
for elem in anodes:
  print elem, "depth", elem.depth, "width", elem.width
  pgame(elem.matrix)

#######################
#2 state node
anodes.append(Node(2,2,grid))
grid=createfield()
right(anodes[2].matrix, cars[1])  #unless grid is reset, this function effects called node
#######################
for elem in anodes:
  print elem, "depth", elem.depth, "width", elem.width
  pgame(elem.matrix)

#######################
#3 state node
anodes.append(Node(3,3,grid))
grid=createfield()
right(anodes[3].matrix, cars[0])  #unless grid is reset, this function effects called node
#######################
for elem in anodes:
  print elem, "depth", elem.depth, "width", elem.width
  pgame(elem.matrix)




right(grid, cars[1])
grid=anodes[]
anodes.append(Node(6,9,grid))
