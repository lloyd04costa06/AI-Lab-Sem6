import collections
from igraph import Graph
import igraph

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
    # edges = []
    # vertices_set = set()
    # for key in GRAPH:
    #     vertices_set.add( key )
    #     for item in GRAPH[key]:
    #         edges.append( (key, item) )
    #         vertices_set.add( item )


    # g = igraph.Graph( directed=True )
    # g.add_vertices( len(vertices_set) )
    # g.vs['name'] = list(vertices_set)
    # g.add_edges( edges )

    # print(len(g.vs))
    # print(len(g.es))
    # Graph.plot(g)
  
def DFS(start):
    visited=set()
    stack=collections.deque([start])
    
    while stack:
        V=stack.pop()
        if V not in visited:
            print(V,end=" ")
            visited.add(V)

        for neighbour in GRAPH[V]:
            if neighbour not in visited:
                stack.append(neighbour)
    
    # print(visited)
        



InputGraph()

x=int(input("ENTER START NODE"))
DFS(x)

