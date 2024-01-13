import random

# Initial state of the matrix
matrix = [[-1, -1, -1],
          [-1, -1, -1],
          [-1, -1, -1]]

# -1 represents an empty cell
# 0 represents the move of a human, and 1 represents the move of the computer

def printMatrix(matrix):
    for row in matrix:
        for element in row:
            print(f"{element:^3}", end=" ")  # Use string formatting for equal width
        print()

def checkWiningStatus(matrix):
    # Check rows and columns
    for i in range(3):
        if matrix[i][0] == matrix[i][1] == matrix[i][2] == 1 or matrix[0][i] == matrix[1][i] == matrix[2][i] == 1:
            return 1
        if matrix[i][0] == matrix[i][1] == matrix[i][2] == 0 or matrix[0][i] == matrix[1][i] == matrix[2][i] == 0:
            return 0

    # Check diagonals
    if matrix[0][0] == matrix[1][1] == matrix[2][2] == 1 or matrix[0][2] == matrix[1][1] == matrix[2][0] == 1:
        return 1
    if matrix[0][0] == matrix[1][1] == matrix[2][2] == 0 or matrix[0][2] == matrix[1][1] == matrix[2][0] == 0:
        return 0

    return -1

printMatrix(matrix)

while True:
    ## human turn
    while True:
        row = int(input("Enter row number in the range (0-2): "))
        col = int(input("Enter column number in the range (0-2): "))
        
        if 0 <= row <= 2 and 0 <= col <= 2:
            break
        else:
            print("Invalid input! Please enter row and column values between 0 and 2.")
    
    if matrix[row][col] == -1:
        matrix[row][col] = 0
    else:
        print("Cell already occupied. Choose a different cell.")
        continue
    
    a = checkWiningStatus(matrix)
    if a == 1:
        printMatrix(matrix)
        print("Sorry,You lost....\nBetter luck next time!! ")
        break
    if a == 0:
        printMatrix(matrix)
        print("Congratulations!,You won..... ")
        break
    
    next = 1
    # computer turn
    while next == 1:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if matrix[row][col] == -1:
            matrix[row][col] = 1
            next = 0
        else:
            print("Cell already occupied. Choose a different cell.")
            continue
    
    a = checkWiningStatus(matrix)
    if a == 1:
        printMatrix(matrix)
        print("Sorry,You lost....\nBetter luck next time!! ")
        break
    if a == 0:
        printMatrix(matrix)
        print("Congratulations!,You won..... ")
        break
    
    print("Current status of the matrix:")
    printMatrix(matrix)
