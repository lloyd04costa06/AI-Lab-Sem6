graph = {
    0:[(1,6),(5,3)],
    1:[(0,6),(3,2),(2,3)],
    2:[(1,3),(3,1),(4,5)],
    3:[(1,2),(2,1),(4,8)],
    4:[(2,5),(3,8),(8,5),(9,5)],
    5:[(0,3),(6,1),(7,7)],
    6:[(5,1),(8,3)],
    7:[(5,7),(8,2)],
    8:[(6,3),(7,2),(9,3),(4,5)],
    9:[(4,5),(8,3)]
}
priority = {
    0:10,
    1:8,
    2:5,
    3:7,
    4:3,
    5:6,
    6:5,
    7:3,
    8:1,
    9:2
}

from queue import PriorityQueue

# graph={}
# priority={}
l=[]
closed=[]
visited=[]

def RECONSTRUCT(state):
    for node in closed:
        if state == node[1]:
            RECONSTRUCT(node[0])
            l.append(state)
            break

def inputGph(n):
    for i in range(n):
        node=input("\ENTER THE NODES: ")
        priority[node]=int(input("\ENTER HEURISTIC VALUE: "))

        graph[node]=[]
        e=int(input('ENTER THE NUMBER OF NEIGHBOURS: '))
        for j in range(e):
            graph[node].append(tuple(map(int, input(f"ENTER THE NEIGHBOUT OF {node} AND THE COST: ").split())))

def HillClimbing():
    pq = PriorityQueue()
    pq.put((priority[src], None, src))
    visited.append(src)
     
    while pq.empty() == False:
        u = pq.get()
        print(u)
        closed.append((u[1], u[2]))
        
        while pq.empty() == False:
            x=pq.get()

        if u[2] == dest:
            break
 
        for v in graph[u[2]]:
            if v[0] not in visited:
                visited.append(v[0])
                pq.put((priority[v[0]], u[2], v[0]))

    if u[2] == dest:
        RECONSTRUCT(u[2])
        print("PATH: ",end="")
        for x in l:
            print(x,end=" ")
    else:
        print("LOCAL MINIMA")



# n=int(input('Enter the number of nodes: '))
# inputGph(n)

src = int(input("\ENTER SOURCE: "))
dest = int(input("ENTER DESITINATION: "))

HillClimbing()