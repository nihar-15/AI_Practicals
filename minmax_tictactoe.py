# -*- coding: utf-8 -*-
"""MinMax_TicTacToe.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11Cawl7L3ETNzNfz1qMQkgodjwVBxrZiK
"""

def canMove(matrix):
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == -1:
                return True
    return False

def evaluate(b):
    # Checking for Rows
    for row in range(3):
        if b[row][0] == b[row][1] and b[row][1] == b[row][2]:
            if b[row][0] == 0:
                return 1
            elif b[row][0] == 1:
                return -1

    # Checking for Columns
    for col in range(3):
        if b[0][col] == b[1][col] and b[1][col] == b[2][col]:
            if b[0][col] == 0:
                return 1
            elif b[0][col] == 1:
                return -1

    # Checking for Diagonals
    if b[0][0] == b[1][1] and b[1][1] == b[2][2]:
        if b[0][0] == 0:
            return 1
        elif b[0][0] == 1:
            return -1

    if b[0][2] == b[1][1] and b[1][1] == b[2][0]:
        if b[0][2] == 0:
            return 1
        elif b[0][2] == 1:
            return -1

    # Draw
    return 0

def getAllAvailablePos(matrix):
    ans = []
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == -1:
                ans.append([i, j])
    return ans

def miniMax(matrix, isPlayer, depth):
    utilityFuncVal = evaluate(matrix)

    if utilityFuncVal == 1 or utilityFuncVal == -1:
        return utilityFuncVal

    if not canMove(matrix):
        return 0

    if isPlayer:
        best = -1
        for i in range(3):
            for j in range(3):
                if matrix[i][j] == -1:
                    matrix[i][j] = 0
                    best = max(best, miniMax(matrix, False, depth + 1))
                    matrix[i][j] = -1
        return best
    else:
        best = 1
        for i in range(3):
            for j in range(3):
                if matrix[i][j] == -1:
                    matrix[i][j] = 1
                    best = min(best, miniMax(matrix, True, depth + 1))
                    matrix[i][j] = -1
        return best

def computer_move(matrix):
    avl_pos = getAllAvailablePos(matrix)
    max_val = -float('inf')
    best_row, best_col = -1, -1
    for pos in avl_pos:
        row = pos[0]
        col = pos[1]
        matrix[row][col] = 0
        val = miniMax(matrix, False, 0)
        matrix[row][col] = -1
        if val > max_val:
            max_val = val
            best_row, best_col = row, col
    return best_row, best_col

def printMatrix(matrix):
    for row in matrix:
        for cell in row:
            if cell == -1:
                print(" ", end=" | ")
            elif cell == 0:
                print("O", end=" | ")
            elif cell == 1:
                print("X", end=" | ")
        print("\n" + "-" * 11)


matrix = [
    [-1, -1, -1],
    [-1, -1, -1],
    [-1, -1, -1]
]

isOver = False

while not isOver:
    row = int(input("Enter row number: "))
    col = int(input("Enter column number: "))

    if row <= 2 and col <= 2 and matrix[row][col] == -1:
        matrix[row][col] = 1
    else:
        continue

    row2, col2 = computer_move(matrix)
    matrix[row2][col2] =0

    if not canMove(matrix):
        isOver = True

    printMatrix(matrix)

if evaluate(matrix) == 1:
    print("You lost!!!!!")

if evaluate(matrix) == -1:
    print("You won!!!!!")

if evaluate(matrix) == 0:
    print("Draw!!!!!")