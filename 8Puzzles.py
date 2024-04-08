



## To solve 8 puzzle problem using BFS.
##
##
##
##
##
##
##
##
##
##
## consider initial state A=[[2,0,4],[1,5,6],[7,8,3]]
## Goal state=[[2,4,6],[1,0,5],7,8,3]
##
##
##
##
##
##
##
##
##
##





import numpy as np
from collections import deque


## successor function 1: To move blank left
def moveLeft(matrix):
    indexOfBlank = [-1, -1]
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if col == 0:
                indexOfBlank = [i, j]

    if indexOfBlank[1] == 0:
        print("Cannot move left...")
        return matrix.copy()
    else:
        newIndexForBlank = [indexOfBlank[0], indexOfBlank[1] - 1]
        matrix[indexOfBlank[0], indexOfBlank[1]], matrix[newIndexForBlank[0], newIndexForBlank[1]] = \
            matrix[newIndexForBlank[0], newIndexForBlank[1]], matrix[indexOfBlank[0], indexOfBlank[1]]

    return matrix



def moveRight(matrix):
    indexOfBlank = [-1, -1]
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if col == 0:
                indexOfBlank = [i, j]

    if indexOfBlank[1] == 2:
        print(" Cannot move right ... ")
        return matrix
    else:
        newIndexForBlank = [indexOfBlank[0], indexOfBlank[1] + 1]
        matrix[indexOfBlank[0], indexOfBlank[1]], matrix[newIndexForBlank[0], newIndexForBlank[1]] = \
            matrix[newIndexForBlank[0], newIndexForBlank[1]], matrix[indexOfBlank[0], indexOfBlank[1]]

    return matrix


def moveUp(matrix):
    indexOfBlank = [-1, -1]
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if col == 0:
                indexOfBlank = [i, j]

    if indexOfBlank[0] == 0:
        print(" Cannot move up ... ")
        return matrix
    else:
        newIndexForBlank = [indexOfBlank[0] - 1, indexOfBlank[1] ]
        matrix[indexOfBlank[0], indexOfBlank[1]], matrix[newIndexForBlank[0], newIndexForBlank[1]] = \
            matrix[newIndexForBlank[0], newIndexForBlank[1]], matrix[indexOfBlank[0], indexOfBlank[1]]

    return matrix



def moveDown(matrix):
    indexOfBlank = [-1, -1]
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if col == 0:
                indexOfBlank = [i, j]

    if indexOfBlank[0] == 2:
        print(" Cannot move  down  ... ")
        return matrix
    else:
        newIndexForBlank = [indexOfBlank[0] + 1, indexOfBlank[1]]
        matrix[indexOfBlank[0], indexOfBlank[1]], matrix[newIndexForBlank[0], newIndexForBlank[1]] = \
            matrix[newIndexForBlank[0], newIndexForBlank[1]], matrix[indexOfBlank[0], indexOfBlank[1]]

    return matrix

matrix = np.array([[2, 0, 4], [1, 5, 6], [7, 8, 3]])
goal = np.array([[2, 4, 6], [1, 0, 5], [7, 8, 3]])

print(matrix)


open_set = deque([tuple(map(tuple, matrix))])
explored_set = set()

while open_set:
    current_node = open_set.popleft()
    current_node_np = np.array(current_node)

    print("Current node popped",current_node_np)

    if np.array_equal(current_node_np, goal):
        print("Finally we are at ",current_node_np)
        print("Goal Achieved")
        break

    result_left = moveLeft(current_node_np.copy())
    if not np.array_equal(result_left, current_node_np):
        explored_set.add(tuple(map(tuple, result_left)))
        open_set.append(tuple(map(tuple, result_left)))

    result_right = moveRight(current_node_np.copy())
    if not np.array_equal(result_right, current_node_np):
        explored_set.add(tuple(map(tuple, result_right)))
        open_set.append(tuple(map(tuple, result_right)))

    result_up = moveUp(current_node_np.copy())
    if not np.array_equal(result_up, current_node_np):
        explored_set.add(tuple(map(tuple, result_up)))
        open_set.append(tuple(map(tuple, result_up)))

    result_down = moveDown(current_node_np.copy())
    if not np.array_equal(result_down, current_node_np):
        explored_set.add(tuple(map(tuple, result_down)))
        open_set.append(tuple(map(tuple, result_down)))

    print("Current open: ", open_set)
    ###print("Current explored: ", explored_set)
