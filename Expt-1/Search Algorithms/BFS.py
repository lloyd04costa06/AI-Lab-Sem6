import collections
GRAPH={}

def InputGraph():
    N=int(input("ENTER NUMBER OF NODES: "))
    for i in range(0,N):
         print("Node:",i)
         Edges=[]
          
         EdgeList=input().split(',')
         for K in EdgeList:
           if K=="":
                continue
           else:   
                Edges.append(int(K))
   
         GRAPH[i]=Edges

def BFS(start):
    visited=set()
    queue=collections.deque([start])
    
    while queue:
        V=queue.popleft()
        if V not in visited:
            print(V,end=" ")
            visited.add(V)
    
        for neighbour in GRAPH[V]:
            if neighbour not in visited:
                queue.append(neighbour)
    
    # print(visited)
        



InputGraph()

x=int(input("ENTER START NODE"))
BFS(x)

