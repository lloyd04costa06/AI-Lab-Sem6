import heapq

# GRAPH = {}
GRAPH={
    0:[(1,15),(2,13),(3,14),(4,9),(6,8)],
    1:[(4,9),(5,10)],
    2:[(6,8)],
    3:[(2,13),(7,13)],
    4:[(8,7),(9,3)],
    5:[(9,3)],
    6:[(5,10)],
    7:[(2,13),(6,8)],
    8:[(10,0)],
    9:[(6,8),(8,7),(10,0)],
    10:[]
}

# t={
#     0:"S",
#     1:"A",
#     2:"C",
#     3:"D",
#     4:"E",
#     5:"F",
#     6:"J",
#     7:"K",
#     8:"H",
#     9:"I",
# }
# def InputGraph():
#     N = int(input("ENTER NUMBER OF NODES: "))
#     print("-1,-1 TO EXIT")
#     for i in range(N):
#         print("Node:", i)
#         EdgeList = []
#         while True:
#             Neig = int(input("NEIGHBOUR: "))
#             Heu = int(input("HEURISTIC: "))
#             temp = (Neig, Heu)
#             EdgeList.append(temp)
#             if temp == (-1, -1):
#                 break
#             print()
#         Edges = []
#         for K in EdgeList:
#             if K == (-1, -1):
#                 continue
#             else:
#                 Edges.append(K)
#         GRAPH[i] = Edges
#     # print(GRAPH)

def BestFS(start, goal):
    visited = set()
    queue = [(0, start)]
    heapq.heapify(queue)
    
    while queue:
        v = heapq.heappop(queue)
        if v[1] == goal:
            print('-->',v[1]," <-- GOAL")
            break

        if v[1] not in visited:
            print("-->", v[1],end="")
            visited.add(v[1])
            for neighbour in GRAPH[v[1]]:
                if neighbour[0] not in visited:
                    heapq.heappush(queue, (neighbour[1], neighbour[0]))

                    

# InputGraph()
x = int(input("ENTER START NODE: "))
y = int(input("ENTER GOAL NODE: "))

BestFS(x,y)
