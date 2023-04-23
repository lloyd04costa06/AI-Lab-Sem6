from pickle import APPEND
from WaterJugGraphics import JUGS

class node:
    def __init__(self,data):
        self.x=0
        self.y=0
        self.rule=0
        self.parent=data
    def __repr__(self):
        return "("+str(self.x)+","+str(self.y)+")"

def Law(currentNode,rule):
    x=currentNode.x
    y=currentNode.y
  
    if rule==1:
        if x<jug1:
            x=jug1
        else:
            return None

    elif rule==2:
        if y<jug2:
            y=jug2
        else:
            return None
    
    elif rule==3:
        if x>0:
            x=0
        else:
            return None
    
    elif rule==4:
        if y>0:
            y=0
        else:
            return None
    
    elif rule==5:
        if x+y >=jug1:
            y=y-(jug1-x)
            x=jug1
        else:
            return None
    
    elif rule==6:
        if x+y >=jug2:
            x=x-(jug2-y)
            y=jug2
        else:
            return None
        
    elif rule==7:
        if x+y < jug1:
            x=x+y
            y=0
        else:
            return None
    
    elif rule==8:
        if x+y < jug2:
            y=x+y
            x=0
        else:
            return None
    
    if (x==currentNode.x and y==currentNode.y):
        return None
    
    nextNode=node(currentNode)
    nextNode.x=x
    nextNode.y=y
    nextNode.rule=rule

    nextNode.parent=currentNode
    return nextNode

def it_is_the_Goal(c,g):
    if c.x==g.x and c.y==g.y:
        return True
    return False

def ConstructPath(Sol):
    temp=Sol
    l=[]

    while temp!=None:
        l.append(temp)
        temp=temp.parent
    l.reverse()
    for i in l:
        print(str(i))

    obj=JUGS(jug1,jug2,Goal_node)
    obj.JugAction(l)




class BFS:
    def __init__(self):
        self.queue=[]

    def pushList(self,list1):
        for i in list1:
          self.queue.append(i)
    
    def popNode(self):
        if len(self.queue)==0:
            return None
        else:
            return self.queue.pop(0)
        
    def generateSuccessors(self,currentNode):
        list1=[]

        for rule in range(1,9):
            nextNode=Law(currentNode,rule)
        
            if nextNode!=None:
                list1.append(nextNode)
        return list1
    
    def bfsMain(self,initialNode,GoalNode):
        self.queue.append(initialNode)

        while len(self.queue)!=0:
            visitedNode=self.popNode()
            if it_is_the_Goal(visitedNode,GoalNode):
                return visitedNode
            
            successor_nodes=self.generateSuccessors(visitedNode)
            self.pushList(successor_nodes)
            


if __name__=='__main__':
    jug1=int(input("ENTER MAX SIZE OF JUG1: "))
    jug2=int(input("ENTER MAX SIZE OF JUG2: "))

    initial_node=node(None)
    initial_node.x=0
    initial_node.y=0
    initial_node.parent=None
    initial_node.rule=None

    Goal_node=node(None)
    Goal_node.x=int(input("ENTER THE GOAL OF JUG-1: "))
    Goal_node.y=0
    Goal_node.parent=0
    

    solutionNode=BFS().bfsMain(initial_node,Goal_node)

    if solutionNode!=None:
        print("Solution Found")
        ConstructPath(solutionNode)
    else:
        print("Solution not found")


