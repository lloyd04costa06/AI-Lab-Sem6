import heapq
G={
    1:[(1,15),(5,4)],
    2:[(1,15),(4,5),(3,28)],
    3:[(2,28),(4,10)],
    4:[(3,10),(2,5),(5,2)],
    5:[(1,4),(4,2)]
}

h={
    1:100,
    2:200,
    3:300,
    4:90,
    5:80
}

def recon(current):
    c=current[3] 
    rev=[]
    while c!=None:
       rev.append(c[1])
       c=c[3]
    rev.reverse()

    for i in rev:
        print(f"{i}-->",end="")
    print("Goal")


    
    

def A_STAR():
    src=int(input("ENTER SOURCE NODE: "))
    goal=int(input("ENTER GOAL NODE: "))

    queue=[]
    visited=set()

    heapq.heappush(queue,(h[src]+0, src, 0,None)) 
    
    while queue:

        current=heapq.heappop(queue) 
        visited.add(current[1]) 

        if current[1]==goal:
            recon(current)
            break

        for node,cost in G[current[1]]:
            if node not in visited:
                heapq.heappush(queue,(h[node]+current[2],node,cost+current[2],current))




A_STAR()


