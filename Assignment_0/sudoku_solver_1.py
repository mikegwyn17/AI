# function to create the board, reads in txt file with board in it and adds the values to a dictionary with ordered pair marking the row and column
def create_board ():
	# intiialize board and create variables to keep track of the column and row
	sudoku_board = {}
	row_count = 0
	column_count = 0
	with open('easy_sudoku_219.txt') as txt_file:
		for text in txt_file:
			row_count += 1
			for txt in text:
				# skip line if it is a /
				if (txt is '/'):
					continue
				else:
					# if row cell is 0, set it equal to all possible values 
					if (txt is '0'):
						txt = '123456789'
					column_count += 1
					coordinate = (row_count, column_count)
					sudoku_board.update({coordinate: txt})
					if (column_count == 9):
						column_count = 0
						break
	return sudoku_board

# function used to print the board
def print_board (sudoku_board):
    for k, v in sorted(sudoku_board.items()):
    	print(k,v)

# function used to create lists containing all of the values found in the given column, row, or block
def create_lists (tuple_array, sudoku_board):
	coordinate_array = []
	for element in tuple_array:
		coordinate_array.append(sudoku_board.get(element))
	return coordinate_array

# function used to find the row the coordinate is contained in and return a list of all of the elements in that row
def find_row (sudoku_board, coordinate):
	row = coordinate[0]
	tuple_array = create_tuples(row, 0)
	coordinate_array = create_lists(tuple_array, sudoku_board)
	return coordinate_array

# function used to find hte column the coordinate is contained in and return a list of all of the elements in that column
def find_column (sudoku_board, coordinate):
	column = coordinate[1]
	tuple_array = create_tuples(0, column)
	coordinate_array = create_lists(tuple_array, sudoku_board)
	return coordinate_array

# function used to find the block or 3X3 matrix the coordinate is contained in and return a list of all of the elements in that block
# TODO implement this better with integer division
def find_block (sudoku_board, coordinate):
	block1 = [(1,1), (1,2), (1,3), (2,1), (2,2), (2,3), (3,1), (3,2), (3,3)]
	block2 = [(1,4), (1,5), (1,6), (2,4), (2,5), (2,6), (3,4), (3,5), (3,6)]
	block3 = [(1,7), (1,8), (1,9), (2,7), (2,8), (2,9), (3,7), (3,8), (3,9)]
	block4 = [(4,1), (4,2), (4,3), (5,1), (5,2), (5,3), (6,1), (6,2), (6,3)]
	block5 = [(4,4), (4,5), (4,6), (5,4), (5,5), (5,6), (6,4), (6,5), (6,6)]
	block6 = [(4,7), (4,8), (4,9), (5,7), (5,8), (5,9), (6,7), (6,8), (6,9)]
	block7 = [(7,1), (7,2), (7,3), (8,1), (8,2), (8,3), (9,1), (9,2), (9,3)]
	block8 = [(7,4), (7,5), (7,6), (8,4), (8,5), (8,6), (9,4), (9,5), (9,6)]
	block9 = [(7,7), (7,8), (7,9), (8,7), (8,8), (8,9), (9,7), (9,8), (9,9)]

	for element in block1:
		if element == coordinate:
			coordinate_array = create_lists(block1, sudoku_board)
			return coordinate_array

	for element in block2:
		if element == coordinate:
			coordinate_array = create_lists(block2, sudoku_board)
			return coordinate_array

	for element in block3:
		if element == coordinate:
			coordinate_array = create_lists(block3, sudoku_board)
			return coordinate_array

	for element in block4:
		if element == coordinate:
			coordinate_array = create_lists(block4, sudoku_board)
			return coordinate_array

	for element in block5:
		if element == coordinate:
			coordinate_array = create_lists(block5, sudoku_board)
			return coordinate_array

	for element in block6:
		if element == coordinate:
			coordinate_array = create_lists(block6, sudoku_board)
			return coordinate_array

	for element in block7:
		if element == coordinate:
			coordinate_array = create_lists(block7, sudoku_board)
			return coordinate_array

	for element in block8:
		if element == coordinate:
			coordinate_array = create_lists(block8, sudoku_board)
			return coordinate_array

	for element in block9:
		if element == coordinate:
			coordinate_array = create_lists(block9, sudoku_board)
			return coordinate_array

# function used to create tuples of all combinations of rows or columns
def create_tuples (row, column):
	count = 1
	array = []
	if (row == 0):
		while (count <= 9):
			array.append((count,column))
			count += 1

	else:
		while (count <= 9):
			array.append((row, count))
			count += 1

	return array

def solver(block, sudoku_board, coordinate):
	contents = sudoku_board.get(coordinate)
	for cell in block:
		if len(cell) == 1:
			if cell[0] in contents:
				# print (cell[0])
				contents = contents.replace(cell[0], '')
				sudoku_board.update({coordinate: contents})
				# print (sudoku_board.get(coordinate))

# function used to solve a row, column, or block of sudoku by making sure only one of each number is used in the block once
def solve (sudoku_board, coordinate):
	contents = sudoku_board.get(coordinate)
	column = find_column(sudoku_board, coordinate)
	row = find_row(sudoku_board, coordinate)
	block = find_block(sudoku_board, coordinate)
	solver(column, sudoku_board, coordinate)
	solver(row, sudoku_board, coordinate)
	solver(block, sudoku_board, coordinate)

def check_board (sudoku_board):
    for k, v in sorted(sudoku_board.items()):
    	check = check_block(sudoku_board, k)
    	if not(check):
    		return False
    		
    return True
    	

def check_block (sudoku_board, coordinate):
	row = find_row(sudoku_board, coordinate)
	column = find_column(sudoku_board, coordinate)
	block = find_block(sudoku_board, coordinate)

	row_check = check(row)
	column_check = check(column)
	block_check = check(block)

	if (row_check and column_check and block_check):
		return True
	else:
		return False

def check (block):
	count = '123456789'
	for cell in block:
		if (len(cell) == 1):
			if cell in count:
				count = count.replace(cell[0], 'x')

		else:
			return False

	if count == 'xxxxxxxxx':
		return True
	else:
		return False

#Main method of the sudoku solver
sudoku_board = create_board()
# print_board(sudoku_board)
while not(check_board(sudoku_board)):
	for k, v in sorted(sudoku_board.items()):
		if (len(v) != 1):
			solve(sudoku_board, k)
print_board(sudoku_board)

# print (check_block(sudoku_board, (1,1)))

# print_board(sudoku_board)
# test = create_tuples(1,0)
# for taco in test:
# 	print (taco)
# test_array = find_column(sudoku_board, (1,1))
# for element in test_array:
# 	print (element)
# test_array = find_block(sudoku_board, (9,9))
# for element in test_array:
# 	print (element)

# solve(sudoku_board, (1,1))




