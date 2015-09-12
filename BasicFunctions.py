##Naming Vehicles: C=car; T=Truck; V=Vertical; H=Horizontal; M=Main Car; 0=Free space
##e.g. HC3 stands for third horizontal car from up to down
##e.g. VT1 stands for first vertical car from left to right

def createemptymatrix():
#creates a 6x6 zero-filled matrix
	matrix = [[0 for x in range(6)]for x in range(6)]
	return matrix
	
def up(matrix, car):
	for i in range(6):
		for j in range(6):
			#searching the field for a specific car
			if matrix[i][j] == car:
				if (i-1>-1): #if it won´t get out of the boundary:
					if (matrix[i-1][j] == 0): #if it won´t hit another vehicle:
						#move up!
						matrix[i-1][j] = car;
						matrix[i][j] = car;
						matrix[i+1][j] = 0;
						return "Done"
					else:
						return "Error"
				else:
					return "Error"

def down(matrix, car):
	for i in range(6):
		for j in range(6):
			if matrix[i][j] == car:
				if (i+2<6):
					if(matrix[i+2][j] == 0):
						matrix[i+2][j] = car;
						matrix[i+1][j] = car;
						matrix[i][j] = 0;
						return "Done"
					else:
						return "Error"
				else:
					return "Error"
					
def left(matrix, car):
	for i in range(6):
		for j in range(6):
			if matrix[i][j] == car:
				if (j-1>-1):
					if (matrix[i][j-1] == 0):
						matrix[i][j-1] = car;
						matrix[i][j] = car;
						matrix[i][j+1] = 0;
						return "Done"
					else:
						return "Error"
				else:
					return "Error"
					
def right(matrix, car):
	for i in range(6):
		for j in range(6):
			if matrix[i][j] == car:
				if (j+2<6):
					if(matrix[i][j+2] == 0):
						matrix[i][j+2] = car;
						matrix[i][j+1] = car;
						matrix[i][j] = 0;
						return "Done"
					else:
						return "Error"
				else:
					return "Error"
					
def printmatrix(matrix):
#just prints the matrix as a table
	for i in range(6):
		print matrix[i]
		
def createfield():
#this is our pre-defined field (game level)
	matrix=createemptymatrix()
	matrix[2][2]="v1"
	matrix[3][2]="v1"
	
	matrix[4][2]="h1"
	matrix[4][3]="h1"
	
	matrix[2][0]="M"
	matrix[2][1]="M"
	
	return matrix
		
def evaluate(matrix):
#to win the game, the main car (M) should get to 6th row from the 3rd line (exit of the parking lot)
	if matrix[2][5] == "M":
		return "WON"
	else:
		return "NOT YET"
