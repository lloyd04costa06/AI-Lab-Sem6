import random

N = 8

def printTOPBorder():
    print("   +", end="")
    for j in range (N):
        print("~~~+", end="")
    print("")

def DrawBoard(board):
    printTOPBorder()
    for queen_row in range(len(board)):
        print(queen_row+1, " |", end="")
        queen_col= board [queen_row]
        for j in range(N):
            if j == queen_col:
                print(" Q |", end="")
            else:
                print("   |", end="")
        print("")
        printTOPBorder()

def h(input):
    count = 0
    for queen_row in range(len(input)):
        queen_col = input[queen_row]
        for queen_2_row in range(queen_row + 1, len(input)):
            queen_2_col = input[queen_2_row]
            if queen_2_row == queen_row:
                continue
            if queen_2_row - queen_2_col == queen_row - queen_col:
                # same difference, collision along NW
                count += 1
            if queen_2_row + queen_2_col == queen_row + queen_col:
                # same sum, collision along NE-SW direction
                count += 1
    return count


def move_gen(input):
    res = []
    for i in range(N):
        child=input[:]
        child[0], child[i] = child[i], child[0]
        if child not in open and child not in closed:
            res.append(child)
    return res


def isSoln(board):
    # check if every queen in the board is not being attacked
    diagonal_collision = (h(board) > 0) 
    two_queens_same_column = (len(set(board)) < N)
    #row collision is not possible
    return not (diagonal_collision or two_queens_same_column)


start = [0, 1, 2, 3, 4, 5, 6, 7]
open, closed = [start], []

print("\nInput: \n")
DrawBoard(start)
print("\nOutput: \n")
while open:

    board = open.pop(0)
    # DrawBoard(board)
    # input()
    if isSoln(board):
        DrawBoard(board)
        break
    else:
        closed = [board] + closed
        children = move_gen(board)
        open = sorted(children + open, key=lambda x: h(x))
print("")