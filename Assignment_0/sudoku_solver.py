def create_board ():
	with open('easy_sudoku_219.txt', 'r') as txt_file:
		for line in txt_file:
			print (line)

def find_row (coordinate, sudoku_board):
	for k, v in sorted(sudoku_board.items()):
		if (k[0] is coordinate[0]):
			print (k, v)

def find_column (coordinate, sudoku_board):
	for k, v in sudoku_board.items():
		if k[1] is coordinate[1]:
			print (k, v)

def find_block (coordinate, sudoku_board):
	block1 = "A1A2A3B1B2B3C1C2C3"
	block2 = "A4A5A6B4B5B6C4C5C6"
	block3 = "A7A8A9B7B8B9C7C8C9"
	block4 = "D1D2D3E1E2E3F1F2F3"
	block5 = "D4D5D6E4E5E6F4F5F6"
	block6 = "D7D8F9E7E8E9F7F8F9"
	block7 = "G1G2G3H1H2H3I1I2I3"
	block8 = "G4G5G6H4H5H6I4I5I6"
	block9 = "G7G8G9H7H8H9I7I8I9"

	if (coordinate in block1):
		print ("block1")
	elif (coordinate in block2):
		print ("block2")
	elif (coordinate in block3):
		print ("block3")
	elif (coordinate in block4):
		print ("block4")
	elif (coordinate in block5):
		print ("block5")
	elif (coordinate in block6):
		print ("block6")
	elif (coordinate in block7):
		print ("block7")
	elif (coordinate in block8):
		print ("block8")
	elif (coordinate in block9):
		print ("block9")
	else:
		print ("error")

# sudoku_board = {'A1': '0', 'A2': '0', 'A3': '0', 'A4': '0', 'A5': '0', 'A6': '0', 'A7': '0', 'A8': '0', 'A9': '0',
#                 'B1': '0', 'B2': '0', 'B3': '0', 'B4': '0', 'B5': '0', 'B6': '0', 'B7': '0', 'B8': '0', 'B9': '0',
#                 'C1': '0', 'C2': '0', 'C3': '0', 'C4': '0', 'C5': '0', 'C6': '0', 'C7': '0', 'C8': '0', 'C9': '0',
#                 'D1': '0', 'D2': '0', 'D3': '0', 'D4': '0', 'D5': '0', 'D6': '0', 'D7': '0', 'D8': '0', 'D9': '0',
#                 'E1': '0', 'E2': '0', 'E3': '0', 'E4': '0', 'E5': '0', 'E6': '0', 'E7': '0', 'E8': '0', 'E9': '0',
#                 'F1': '0', 'F2': '0', 'F3': '0', 'F4': '0', 'F5': '0', 'F6': '0', 'F7': '0', 'F8': '0', 'F9': '0',
#                 'G1': '0', 'G2': '0', 'G3': '0', 'G4': '0', 'G5': '0', 'G6': '0', 'G7': '0', 'G8': '0', 'G9': '0',
#                 'H1': '0', 'H2': '0', 'H3': '0', 'H4': '0', 'H5': '0', 'H6': '0', 'H7': '0', 'H8': '0', 'H9': '0',
#                 'I1': '0', 'I2': '0', 'I3': '0', 'I4': '0', 'I5': '0', 'I6': '0', 'I7': '0', 'I8': '0', 'I9': '0'}
create_board()

# test_array = ['A1','A2','A3','B1','B2','B3','C1','C2','C3','A4','A5','A6','B4','B5','B6','C4','C5','C6','A7','A8','A9','B7','B8','B9','C7','C8','C9',
# 			  'D1','D2','D3','E1','E2','E3','F1','F2','F3','D4','D5','D6','E4','E5','E6','F4','F5','F6','D7','D8','F9','E7','E8','E9','F7','F8','F9',
# 			  'G1','G2','G3','H1','H2','H3','I1','I2','I3','G4','G5','G6','H4','H5','H6','I4','I5','I6','G7','G8','G9','H7','H8','H9','I7','I8','I9']
# # find_row('B7', sudoku_board)
# # find_column('A1', sudoku_board)
# # find_block('A1', sudoku_board)
# for test in test_array:
# 	find_block(test, sudoku_board)

# for k, v in sorted(sudoku_board.items()):
#     print(k, v)