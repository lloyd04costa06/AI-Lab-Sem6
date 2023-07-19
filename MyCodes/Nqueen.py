import random
import heapq
import copy

def H(state):
    h = 0
    for i in range(len(state)):
        for j in range(i+1, len(start)):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                h += 1
    return h

def isSol(board):
    for i in range(len(board)):
        for j in range(i+1,len(board)):
            if board[i]==board[j] or abs(board[i]-board[j])==abs(i-j) :
                return False;
    return True

def movGen(board):
    possible=[]
    for i in range(len(board)):
        child=copy.deepcopy(board)
        child[0],child[i]=child[i],child[0]
        possible.append(child)
    return possible


def Best_First_Search(start):

    queue=[]
    visited=set()
    heapq.heappush(queue,(H(start),start,None))
    
    while queue:

        current=heapq.heappop(queue)
        visited.add(tuple(current[1]))
        

        if isSol(current[1]):
            Draw(current[1])
            break;

        for i in movGen(current[1]):
            if tuple(i) not in visited:
                heapq.heappush(queue,(H(i),i,current))
 

def Draw(board):
    for row in range(len(board)):
        for col in range(len(board)):
            if col==board[row]:
                print("Q  ",end="")
            else:
                print("*  ",end="")
        print()

    







N=int(input("ENTER N: "))
start=list(range(N))
random.shuffle(start)

print("Initial State: ")
Draw(start)
print("\n\nOUTPUT:\n ")
Best_First_Search(start)

