import time

board = [
	[0, 0, 0, 0, 0, 5, 4, 0, 9,], 
	[4, 5, 1, 0, 0, 2, 3, 0, 0,],
	[9, 8, 2, 0, 0, 0, 5, 6, 1,],
	[6, 0, 7, 0, 0, 0, 9, 8, 0,],
	[0, 0, 3, 4, 6, 0, 0, 0, 0,],
	[5, 0, 0, 2, 8, 7, 0, 1, 0,],
	[0, 4, 0, 0, 7, 0, 0, 9, 6,],
	[3, 0, 0, 0, 0, 0, 7, 0, 0,],
	[0, 0, 5, 9, 4, 6, 8, 0, 2,],
]


def showBoard(board):
	for i in range(0,9):
		print('\n')
		if i==3 or i==6:
			print("---------------------")
		for j in range(0,9):
			if j==3 or j==6:
				print("|", end=' ')
			if(not board[i][j]):
				print(board[i][j], end=" ")
			else:
				print(board[i][j], end=" ")
	print('\n')

def isValid(val, row, col):
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


def findNext(row, col):
	if(col==8):
		col = 0
		row += 1
	else:
		col+=1

	while(board[row][col] != 0):
		if(col==8):
			col = 0
			row += 1
		else:
			col+=1

	return row, col


def getProblem(board):
	print("Enter the board values(enter 0 if blank): ")
	for i in range(0,9):
		for j in range(0,9):
			x = int(input("Enter row-wise nd hit enter after eachh value:\n"))
			board[i][j] = x


def fillValue(val, row, col):
	found = False
	for i in range(1,10):
		if(isValid(i, row, col) and i != val):
			board[row][col] = i
			found =  True
			break
	return found


def main():
	showBoard(board)
	row, col = 0, 0
	val = 0
	if(not board[row][col]):
		fillValue(val, row, col)
	while(row != 9):
		curr = row, col
		row, col = findNext(row, col)
		if(not fillValue(val, row, col)):
			val = 0
			board[row][col] = 0
			board[curr[0]][curr[1]] = 0
		else:
			val = board[row][col]
		showBoard(board)
		input()


if __name__ == '__main__':
	main()