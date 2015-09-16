##Naming Vehicles: C=Car; T=Truck; V=Vertical; H=Horizontal; M=Main veh; 0=Free space
##e.g. HC3 stands for third horizontal car from up to down
##e.g. VT1 stands for first vertical truck from left to right

def createemptymatrix():
#creates a 6x6 zero-filled matrix
	matrix = [["---" for x in range(6)]for x in range(6)]
	return matrix
	
def up(matrix, veh):
	if veh[0]=="V":
		for i in range(6):
			for j in range(6):
				#searching the field for a specific veh
				if matrix[i][j] == veh:
					if veh[1]=='C':
						if (i-1>-1): #if it wont get out of the boundary
							if (matrix[i-1][j] == "---"): #if it wont hit another vehicle
								#move up!
								matrix[i-1][j] = veh;
								matrix[i][j] = veh;
								matrix[i+1][j] = "---";
								return "Done"
							else:
								return "Error"
						else:
							return "Error"
							
					if veh[1]=="T":
						if (i-1>-1): #if it wont get out of the boundary
							if (matrix[i-1][j] == "---"): #if it wont hit another vehicle
								#move up!
								matrix[i-1][j] = veh;
								matrix[i][j] = veh;
								matrix[i+1][j] = veh;
								matrix[i+2][j] = "---";
								return "Done"
							else:
								return "Error"
						else:
							return "Error"
	else:
		return "Error"

def down(matrix, veh):
	if veh[0]=="V":
		for i in range(6):
			for j in range(6):
				if matrix[i][j] == veh:
					if veh[1]=='C':
						if (i+2<6):
							if(matrix[i+2][j] == "---"):
								matrix[i+2][j] = veh;
								matrix[i+1][j] = veh;
								matrix[i][j] = "---";
								return "Done"
							else:
								return "Error"
						else:
							return "Error"
							
					if veh[1]=='T':
						if (i+3<6):
							if(matrix[i+3][j] == "---"):
								matrix[i+3][j] = veh;
								matrix[i+2][j] = veh;
								matrix[i+1][j] = veh;
								matrix[i][j] = "---";
								return "Done"
							else:
								return "Error"
						else:
							return "Error"
	else:
		return "Error"
							
							
def left(matrix, veh):
	if veh[0]=="H" or veh[0]=="M":
		for i in range(6):
			for j in range(6):
				if matrix[i][j] == veh:
					if veh[1]=="C":
						if (j-1>-1):
							if (matrix[i][j-1] == "---"):
								matrix[i][j-1] = veh;
								matrix[i][j] = veh;
								matrix[i][j+1] = "---";
								return "Done"
							else:
								return "Error"
						else:
							return "Error"
							
					if veh[1]=="T":
						if (j-1>-1):
							if (matrix[i][j-1] == "---"):
								matrix[i][j-1] = veh;
								matrix[i][j] = veh;
								matrix[i][j+1] = veh;
								matrix[i][j+2] = "---";
								return "Done"
							else:
								return "Error"
						else:
							return "Error"
	else:
		return "Error"
							
							
def right(matrix, veh):
	if veh[0]=="H" or veh[0]=="M":
		for i in range(6):
			for j in range(6):
				if matrix[i][j] == veh:
					if veh[1]=="C":
						if (j+2<6):
							if(matrix[i][j+2] == "---"):
								matrix[i][j+2] = veh;
								matrix[i][j+1] = veh;
								matrix[i][j] = "---";
								return "Done"
							else:
								return "Error"
						else:
							return "Error"
							
					if veh[1]=="T":
						if (j+3<6):
							if(matrix[i][j+3] == "---"):
								matrix[i][j+3] = veh;
								matrix[i][j+2] = veh;
								matrix[i][j+1] = veh;
								matrix[i][j] = "---";
								return "Done"
							else:
								return "Error"
						else:
							return "Error"
	else:
		return "Error"						
						
def printmatrix(matrix):
#just prints the matrix as a table
	for i in range(6):
		print matrix[i]
		
def pgame(matrix):
	print matrix[0]
	print matrix[1]
	print matrix[2] ,"EXIT"
	print matrix[3]
	print matrix[4]
	print matrix[5]
		
def createfield():
#this is our pre-defined field (game level)
	matrix=createemptymatrix()
	
	matrix[2][0]="MC0"
	matrix[2][1]="MC0"
	
	matrix[5][3]="HT1"
	matrix[5][4]="HT1"
	matrix[5][5]="HT1"
	
	
	matrix[0][2]="HC1"
	matrix[0][3]="HC1"
	
	matrix[1][2]="HC2"
	matrix[1][3]="HC2"
	
	matrix[4][4]="HC3"
	matrix[4][5]="HC3"

	matrix[0][1]="VC1"
	matrix[1][1]="VC1"
	
	matrix[0][4]="VC2"
	matrix[1][4]="VC2"
	
	matrix[2][2]="VC3"
	matrix[3][2]="VC3"
	
	matrix[4][2]="VC4"
	matrix[5][2]="VC4"
	
	matrix[3][0]="VT1"
	matrix[4][0]="VT1"
	matrix[5][0]="VT1"
	
	matrix[2][3]="VT2"
	matrix[3][3]="VT2"
	matrix[4][3]="VT2"
	
	
	return matrix
		
def evaluate(matrix):
#to win the game, the main car (MC0) should get to 6th row from the 3rd line (exit of the parking lot)
	if matrix[2][5] == "MC0":
		return "WON"
	else:
		return "NOT YET"
