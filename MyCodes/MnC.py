import copy

def reconstruct(current):
    path = []
    while current:
        path.append(current[0])
        current = current[1]
    path.reverse()
    print("Path:", path)

def ValidMove(state):
    mL, cL, mR, cR, B = state #state is ur tuple (ML,CL,MR,ML,side)

    if mL < cL and mL > 0: #Ensure that No of missionaries more than cannibals on left hand side
        return False
    if mR < cR and mR > 0: #Ensure that No of missionaries more than cannibals on right hand side
        return False
    
    return 0 <= mL <= 3 and 0 <= cL <= 3 and 0 <= mR <= 3 and 0 <= cR <= 3 #This to check if the values are between 0 or 3

def MovGen(current):
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)] #U can use any of this moves to minus
    newStates = []

    for M, C in moves:
        if current[4] == 'L':
            next_state = (current[0] - M, current[1] - C, current[2] + M, current[3] + C, 'R') #Minus the left side and add on right side and move the boat to right
        else:
            next_state = (current[0] + M, current[1] + C, current[2] - M, current[3] - C, 'L') #Minus  the right side and add on left and move on left

        if ValidMove(next_state): #now check if the state u just generated is valid or no
            newStates.append(next_state) #if yes add it to a possible list of valid moves
            
    return newStates

def DFS(start, goal):
    stack = []
    visited = set()

    stack.append((start, None))
    while stack:
        current = stack.pop()
        visited.add(current[0])

        if current[0] == goal:
            reconstruct(current)
            break

        for next_state in MovGen(current[0]):
            if next_state not in visited:
                stack.append((next_state, current))


M = int(input("ENTER NUMBER OF MISSIONARIES: "))
C = int(input("ENTER NUMBER OF CANNIBALS: "))
start = (M, C, 0, 0, 'L')
goal = (0, 0, M, C, 'R')
DFS(start, goal)
