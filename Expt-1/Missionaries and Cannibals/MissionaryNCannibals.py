from MN_Graphics import MissionaryAndCannibalsGraphics

class Node:
    def __init__(self, M, C, B, P):
        self.M = M
        self.C = C
        self.B = B
        self.rule = 0
        self.parent = P

    def __repr__(self):
        return "(" + str(self.M) + "," + str(self.C) + "," + str(self.B) + ")"

    def is_valid_state(self):
        if self.M < 0 or self.C < 0 or self.M > M_G or self.C > C_G:
            return False
        
        if self.M < self.C and self.M > 0:
            return False
        
        if M_G - self.M < C_G - self.C and M_G - self.M > 0:
            return False
        
        return True

    def is_goal_state(self):
        if self.C == 0 and self.M == 0 and self.B == 'R':
            return True
        
        return False

def construct_path(sol):
    temp = sol
    path = []
    while temp is not None:
        path.append(temp)
        temp = temp.parent
    path.reverse()
    
    for node in path:
        print(str(node))

    obj = MissionaryAndCannibalsGraphics(M_G, C_G, path[1:])
    obj.Sail()

class BFS:
    def __init__(self):
        self.queue = []

    def push_node(self, node):
        self.queue.append(node)
    
    def pop_node(self):
        if len(self.queue) == 0:
            return None
        else:
            return self.queue.pop(0)
        
    def generate_successors(self, current_node):
        successors = []
        for i in range(M_G):
            for j in range(M_G):
                if i + j == 0:
                    continue
                if i + j > M_G-1:
                    continue
                if current_node.B == 'L':
                    next_node = Node(current_node.M - i, current_node.C - j, 'R', current_node)
                else:
                    next_node = Node(current_node.M + i, current_node.C + j, 'L', current_node)
                if next_node.is_valid_state():
                    successors.append(next_node)
        return successors
    
    def bfs_main(self, initial_node):
        self.queue.append(initial_node)
        
        while len(self.queue) != 0:
            visited_node = self.pop_node()
            if visited_node.is_goal_state():
                return visited_node
            successor_nodes = self.generate_successors(visited_node)
            for node in successor_nodes:
                self.push_node(node)
            

if __name__ == '__main__':
    M_G = int(input("ENTER NUMBER OF MISSIONARIES: "))
    C_G = int(input("ENTER NUMBER OF CANNIBALS: "))

    initial_node = Node(M_G, C_G, 'L', None)

    solution_node = BFS().bfs_main(initial_node)

    if solution_node is not None:
        print("SOLUTION FOUND")
        construct_path(solution_node)
    else:
        print("SOLUTION NOT FOUND")
