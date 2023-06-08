import math
from TicTacToeUi import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", end = " ")
        for j in range(3):
            print(board[i][j], "|", end = " ")
        print()
        print("-------------")

def EVAL(board):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2]:
            if board[row][0] == 'X':
                return 10
            elif board[row][0] == 'O':
                return -10

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == 'X':
                return 10
            elif board[0][col] == 'O':
                return -10

    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == 'X':
            return 10
        elif board[0][0] == 'O':
            return -10

    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == 'X':
            return 10
        elif board[0][2] == 'O':
            return -10

    return 0

def IS_MOVES_LEFT(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                return True
    return False

def MINIMAX(board, depth, is_maximizing):
    score = EVAL(board)

    if score == 10:
        return score - depth

    if score == -10:
        return score + depth

    if not IS_MOVES_LEFT(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'X'
                    score = MINIMAX(board, depth + 1, False)
                    board[i][j] = '_'
                    best_score = max(score, best_score)
        return best_score

    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'O'
                    score = MINIMAX(board, depth + 1, True)
                    board[i][j] = '_'
                    best_score = min(score, best_score)
        return best_score

def find_best_move(board):
    best_score = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = 'X'
                score = MINIMAX(board, 0, False)
                board[i][j] = '_'
                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    return best_move

def PLAY_GAME():
    board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    

    while IS_MOVES_LEFT(board):
        while ui.count==False:
            QApplication.processEvents()
        row=ui.row
        col=ui.col

        if board[row][col] != '_':
            print("INVALID MOVE, TRY AGAIN.")
            continue

        board[row][col] = 'O'
      

        if EVAL(board) == -10:
            ui.label.setText('YOU WIN!')
            return

        if not IS_MOVES_LEFT(board):
            ui.label.setText('ITS A TIE!')
            return

        (row, col) = find_best_move(board)
        bt[(row, col)].setText("O")
        board[row][col] = 'X'
     
        ui.count=False

        if EVAL(board) == 10:
            ui.label.setText('YOU LOSE!')
            return

        if not IS_MOVES_LEFT(board):
            ui.label.setText('ITS A TIE!')
            return

import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

ui = Ui_MainWindow()
ui.setupUi(MainWindow)
ui.label.setText('START!!')
MainWindow.show()
bt={
    (0,0):ui.B00,
    (0,1):ui.B01,
    (0,2):ui.B02,

    (1,0):ui.B10,
    (1,1):ui.B11,
    (1,2):ui.B12,

    (2,0):ui.B20,
    (2,1):ui.B21,
    (2,2):ui.B22,
}

PLAY_GAME()
sys.exit(app.exec_())
