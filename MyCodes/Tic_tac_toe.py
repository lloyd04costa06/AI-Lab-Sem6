PLAYER_X='X'
PLAYER_Y='Y'
EMPTY='-'



def Draw(board):
    for i in range(len(board)):
        for j in range(len(board)):
            print(f" {board[i][j]} ",end="")
        print("")
    print("\n")

def get_best_move(B):
     for i in range(len(B)):
            for j in range(len(B)):
                  if B[i][j]==EMPTY:
                        return i,j

def TERMINAL(board):
     
     #check rows
     for row in range(len(board)):
            if board[row][0] == board[row][1] == board[row][1] != EMPTY:
                 return True
    
     #check cols
     for col in range(len(board)):
            if board[0][col] == board[1][col] == board[2][col] != EMPTY:
                 return True
            
    #check for diagonals
     if board[0][0]==board[1][1]==board[2][2] != EMPTY:
            return True
     
     if board[0][2]==board[1][1]==board[2][0] != EMPTY:
            return True
     
     #if draw
     for i in range(len(board)):
            for j in range(len(board)):
                  if board[i][j]!=EMPTY:
                        return True
     
     
            
   

def PLAY():
    BOARD=[['-','-','-'],['-','-','-'],['-','-','-']]
    current=PLAYER_X

    while True:
        print("CURRENT BOARD: ")
        Draw(BOARD)

        if current==PLAYER_X:
                row,col=get_best_move(BOARD)
        else:
             while True:
                    try:
                         row=int(input("ENTER THE ROW: (0-2): "))
                         col=int(input("ENTER THE COL: (0-2): "))

                         if 0 <=row <= 3 and 0 <=col <= 3 and BOARD[row][col]==EMPTY:
                                break
                         else: print("INVALID MOVE! PLEASE RECTIFY\n")
                    except:
                         print("INVALID INPUT! PLEASE RECTIFY\n")
        
        BOARD[row][col]=current




        if TERMINAL(BOARD):
            print("CURRENT BOARD: ")
            Draw(BOARD)

            if any(BOARD[i][j]==PLAYER_X for i in range(len(BOARD)) for j in range(len(BOARD))):
                  print(f"PLAYER {PLAYER_X} WINS!")

            elif any(BOARD[i][j]==PLAYER_Y for i in range(len(BOARD)) for j in range(len(BOARD))):
                  print(f"PLAYER {PLAYER_Y} WINS!")
            else:
                  print("DRAW!")

        current= PLAYER_Y if current==PLAYER_X else PLAYER_X


             
                         


   



PLAY()