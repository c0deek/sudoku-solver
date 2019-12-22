import os, time

problem = [
	[0, 0, 6, 0, 3, 0, 2, 0, 8,], 
	[7, 0, 0, 0, 2, 0, 0, 0, 4,],
	[0, 9, 2, 0, 0, 4, 1, 0, 0,],
	[1, 0, 0, 2, 0, 0, 0, 0, 6,],
	[0, 0, 8, 0, 0, 5, 0, 1, 0,],
	[0, 2, 0, 0, 1, 0, 0, 4, 0,],
	[8, 0, 0, 4, 0, 0, 0, 0, 0,],
	[0, 0, 5, 0, 6, 0, 4, 8, 0,],
	[0, 1, 0, 0, 0, 2, 0, 0, 3,],
]


filled = [
	[0, 0, 0, 0, 0, 0, 0, 0, 0,],
	[0, 0, 0, 0, 0, 0, 0, 0, 0,],
	[0, 0, 0, 0, 0, 0, 0, 0, 0,],
	[0, 0, 0, 0, 0, 0, 0, 0, 0,],
	[0, 0, 0, 0, 0, 0, 0, 0, 0,],
	[0, 0, 0, 0, 0, 0, 0, 0, 0,],
	[0, 0, 0, 0, 0, 0, 0, 0, 0,],
	[0, 0, 0, 0, 0, 0, 0, 0, 0,],
	[0, 0, 0, 0, 0, 0, 0, 0, 0,],
]


def getProblem(board):
	print("Enter the board values row-wise\nEnter 0 for blank and hit enter after each value: ")
	for i in range(0,9):
		for j in range(0,9):
			x = int(input())
			board[i][j] = x


def showBoard(board):
	for i in range(0,9):
		print('')
		if i==3 or i==6:
			print("---------------------")
		for j in range(0,9):
			if j==3 or j==6:
				print("|", end = ' ')
			if(not board[i][j]):
				print(' ', end=' ')
			else:
				print(board[i][j], end=' ')
	print('\n')


def createSuppliment(board, inverse):
	for i in range(0,9):
		for j in range(0,9):
			if(not board[i][j]):
				inverse[i][j] += 1


def isValid(val, board, row, col):
	isOk = True
	for i in range(0,9):
		if(i != col and board[row][i] == val):
			isOk = False

	for i in range(0,9):
		if(i != row and board[i][col] == val):
			isOk = False

	for i in range(0,3):
		i += int(row/3)*3
		for j in range(0,3):
			j += int(col/3)*3
			if(i != row and j != col and board[i][j] == val):
				isOk = False

	return isOk


def fillValue(board, row, col):
	found = False
	for i in range(1,10):
		if(isValid(i, board, row, col) and i > board[row][col]):
			board[row][col] = i
			found =  True
			break
	return found


def gotoNext(row, col):
	if(col==8):
		col = 0
		row += 1
	else:
		col+=1

	return row, col


def getPrevious(filled, row, col):
	while True:
		if(col==0):
			col = 8
			row -= 1
		else:
			col -= 1

		if(filled[row][col]):
			return row, col


def solve(problem, filled):
	createSuppliment(problem, filled)
	anim = input("Show animation?(y/n): ")
	row, col = 0, 0
	while(row < 9 and col < 9):
		if(filled[row][col]):
			isFilled = fillValue(problem, row, col)
		else:
			isFilled = True

		if(not isFilled):
			problem[row][col] = 0
			row, col = getPrevious(filled, row, col)
		else:
			row, col = gotoNext(row, col)
		
		if(anim == 'y'):
			showBoard(problem)
			time.sleep(0.01)
			clear()

	showBoard(problem)


def clear(): 
    if os.name == 'nt': # for windows 'nt' and for mac+linux 'posix'
        _ = os.system('cls') 
    else: 
        _ = os.system('clear')


def main():
	print("Sudoku-Solver")
	print("1. Enter problem")
	print("2. Sample problem")
	choice = int(input(">> "))
	if(choice==1):
		getProblem(problem)
	elif(choice==2):
		pass
	else:
		print("Wrong choice. WTF!!")

	solve(problem, filled)


if __name__ == '__main__':
	main()