import heapq
import copy
goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

def H(State):
    count=0
    for i in range(3):
        for j in range(3):
            if start[i][j]==goal[i][j]:
                cout=count+1
    return count

def reconstPath(current): 
    c=current
    while c[2]!=None:
        print(c[1])
        c=c[2]


def GetWhiteTile(current):
    for i in range(3):
        for j in range(3):
            if current[i][j]==0:
                return i,j
        
def MoveValid(X,Y):
    return 0<=X<3 and 0<=Y<3


def Best_First_src(start,goal):
    queue=[]
    visited=set()
    heapq.heappush( queue, (H(start),start,None) )

    while queue:
        current=heapq.heappop(queue)
        visited.add(tuple(map(tuple,current[1])))

     

        if current[1]==goal:
            return reconstPath(current)
        
        whiteX , whiteY = GetWhiteTile(current[1])
        List_of_possible_moves=[(whiteX-1,whiteY), (whiteX+1,whiteY), (whiteX,whiteY-1), (whiteX,whiteY+1)]

        for X_Move, Y_Move in List_of_possible_moves:
            if MoveValid(X_Move,Y_Move):
                next_state=copy.deepcopy(current[1])
                next_state[whiteX][whiteY], next_state[X_Move][Y_Move] = next_state[X_Move][Y_Move],next_state[whiteX][whiteY]

                if tuple(map(tuple,next_state)) not in visited:
                    heapq.heappush( queue, (H(next_state),next_state,current) )

                
start=[[8, 1, 3], [4, 2, 5], [7, 0, 6]]
Result=Best_First_src(start,goal)   

