def createemptymatrix():
	matrix = [[0 for x in range(6)]for x in range(6)]
	return matrix
	
def up(matrix, car):
	for i in range(6):
		for j in range(6):
			if matrix[i][j] == car:
				if (i-1>-1):
					if (matrix[i-1][j] == 0):
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
	for i in range(6):
		print matrix[i]
		
def createfield():
	matrix=createemptymatrix()
	matrix[2][2]="v1"
	matrix[3][2]="v1"
	
	matrix[4][2]="h1"
	matrix[4][3]="h1"
	
	matrix[2][0]="M"
	matrix[2][1]="M"
	
	return matrix
		
def evaluate(matrix):
	if matrix[2][5] == "M":
		return "WON"
	else:
		return "NOT YET"
