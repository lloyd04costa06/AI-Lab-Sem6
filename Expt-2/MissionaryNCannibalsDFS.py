from MN_Graphics import MissionaryAndCannibalsGraphics

Result=[]

def reconstruct(state):
    for nodepair in closed:
        if state == nodepair[1]:
            reconstruct(nodepair[0])
            Result.append(state)
            break

def check(t):
    return t not in open and t not in closed

# Checks if Cannibals outnumber missionaries
def satisfy(w,x,y,z):
    if (w==0 or w>=x) and (y==0 or y>=z):
        return True
    else:
        return False


def moregen(node):
    lm, lc, b, rm, rc = node

    #Left to Right
    if(b=='l'):
        b='r'

        # One Missionary goes to right side
        a=(node, (lm-1, lc , b, rm+1, rc))
        if lm-1>=0 and satisfy(lm-1, lc , rm+1, rc) and check(a):
          open.append(a)

        # One Cannibal goes to right side
        a=(node, (lm, lc-1 , b, rm, rc+1))
        if lc-1>=0 and satisfy(lm, lc-1 , rm, rc+1) and check(a):
          open.append(a)

        # One Missionary and One Cannibal goes to right side
        a=(node, (lm-1, lc-1 , b, rm+1, rc+1))
        if lm-1>=0 and lc-1>=0 and satisfy(lm-1, lc-1 , rm+1, rc+1) and check(a):
          open.append(a)

        # Two Missionary goes to right side
        a=(node, (lm-2, lc , b, rm+2, rc))
        if lm-2>=0 and satisfy(lm-2, lc , rm+2, rc) and check(a):
          open.append(a)

        # Two Cannibal goes to right side
        a=(node, (lm, lc-2 , b, rm, rc+2))
        if lc-2>=0 and satisfy(lm, lc-2 , rm, rc+2) and check(a):
          open.append(a)


    # Right to Left
    else:
        b='l'

        # One Missionary goes to left side
        a=(node, (lm+1, lc , b, rm-1, rc))
        if rm-1>=0 and satisfy(lm+1, lc , rm-1, rc) and check(a):
          open.append(a)

        # One Cannibal goes to left side
        a=(node, (lm, lc+1 , b, rm, rc-1))
        if rc-1>=0 and satisfy(lm, lc+1 , rm, rc-1) and check(a):
          open.append(a)

        # One Missionary and One Cannibal goes to left side
        a=(node, (lm+1, lc+1 , b, rm-1, rc-1))
        if rm-1>=0 and rc-1>=0 and satisfy(lm+1, lc+1 , rm-1, rc-1) and check(a):
          open.append(a)

        # Two Missionary goes to left side
        a=(node, (lm+2, lc , b, rm-2, rc))
        if rm-2>=0 and satisfy(lm+2, lc , rm-2, rc) and check(a):
          open.append(a)

        # Two Cannibal goes to left side
        a=(node, (lm, lc+2 , b, rm, rc-2))
        if rc-2>=0 and satisfy(lm, lc+2 , rm, rc-2) and check(a):
          open.append(a)

# DFS
def MissionariesNCannibals():
    while open:
        nodepair = open.pop(0)
        node = nodepair[1]

        if node == goal:
            closed.append(nodepair)
            reconstruct(goal)
            return
        else:
            closed.append(nodepair)
            moregen(node)


M_G = int(input("ENTER NUMBER OF MISSIONARIES: "))
C_G = int(input("ENTER NUMBER OF CANNIBALS: "))

goal = (0, 0, 'r', M_G, C_G)

open = [((None, None, None, None, None), (M_G, C_G, 'l', 0, 0))]
closed = []

MissionariesNCannibals()
obj = MissionaryAndCannibalsGraphics(M_G, C_G, Result)
obj.Sail()