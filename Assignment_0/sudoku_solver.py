# digits = "123456789"
# letters = "ABCDEFGHI"
# coordinates = []
# sudoku_board = {}
#
# for letter in letters:
#         for digit in digits:
#             coordinates.append(zip(letter, digit))
#
# for coordinate in coordinates:
#     # print(*zip(coordinate))
#     sudoku_board.update(*zip(coordinate))
#
# for suduko in sudoku_board.items():
#     print(suduko)

sudoku_board = {'A1': '0', 'A2': '0', 'A3': '0', 'A4': '0', 'A5': '0', 'A6': '0', 'A7': '0', 'A8': '0', 'A9': '0',
                'B1': '0', 'B2': '0', 'B3': '0', 'B4': '0', 'B5': '0', 'B6': '0', 'B7': '0', 'B8': '0', 'B9': '0',
                'C1': '0', 'C2': '0', 'C3': '0', 'C4': '0', 'C5': '0', 'C6': '0', 'C7': '0', 'C8': '0', 'C9': '0',
                'D1': '0', 'D2': '0', 'D3': '0', 'D4': '0', 'D5': '0', 'D6': '0', 'D7': '0', 'D8': '0', 'D9': '0',
                'E1': '0', 'E2': '0', 'E3': '0', 'E4': '0', 'E5': '0', 'E6': '0', 'E7': '0', 'E8': '0', 'E9': '0',
                'F1': '0', 'F2': '0', 'F3': '0', 'F4': '0', 'F5': '0', 'F6': '0', 'F7': '0', 'F8': '0', 'F9': '0',
                'G1': '0', 'G2': '0', 'G3': '0', 'G4': '0', 'G5': '0', 'G6': '0', 'G7': '0', 'G8': '0', 'G9': '0',
                'I1': '0', 'I2': '0', 'I3': '0', 'I4': '0', 'I5': '0', 'I6': '0', 'I7': '0', 'I8': '0', 'I9': '0'}

for k, v in sorted(sudoku_board.keys()):
    print(k, v)









