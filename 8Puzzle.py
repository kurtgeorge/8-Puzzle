from copy import deepcopy 
import heapq


class State:

    def __init__ (self, board, parent = None):
        self.board = board
        self.parent = parent
        self.f = 0
        self.g = 0
        self.h = 0

        if self.parent != None:
            self.g = parent.g + 1 

    def fScore(self):
        if self.parent != None:
            return (self.parent.g + 1) + (self.heuristic(self.board))
        else:
            return self.g + self.heuristic(self.board) 

    
    def printer(self):
        print("-------------")
        print(f'| {self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]} |')
        print("-------------")
        print(f'| {self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]} |')
        print("-------------")
        print(f'| {self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]} |')
        print("-------------")

    def heuristic(self,current):

        #return 1
        temp = 0
        for i in range(3):
            for j in range(3):
                if current[i][j] != goal[i][j] and current[i][j] != 0:
                    temp += 1
        return temp

        
        



def generateMoveStates(state):

        temp = state.board
        que = []
        row,col = None,None

        for a in range(3):
            for b in range(3):
                if temp[a][b] == 0:
                    x,y = a,b
                    break        

        # Checks for the possible moves adding the created states to a list for returning
        if x-1 >= 0:
            b = deepcopy(temp)
            b[x][y]=b[x-1][y]
            b[x-1][y]=0
            succ = State(b, state)
            que.append(succ)
        if x+1 < 3:
            b = deepcopy(temp)
            b[x][y]=b[x+1][y]
            b[x+1][y]=0
            succ = State(b, state)
            que.append(succ)
        if y-1 >= 0:
            b = deepcopy(temp)
            b[x][y]=b[x][y-1]
            b[x][y-1]=0
            succ = State(b, state)
            que.append(succ)
        if y+1 < 3:
            b = deepcopy(temp)
            b[x][y]=b[x][y+1]
            b[x][y+1]=0
            succ = State(b, state)
            que.append(succ)
    
        return que

def inClosedList(board,queue):

    for xy in queue:
        if board == xy.board:
            return True

    return False

def inOpenList(board,queue):

    for xy in queue:
        if board == xy[2].board:
            return True

    return False
 
def aStar(start):

    # Avoids class comparison
    compCounter = 0

    closedList = []
    openList = []

    heapq.heappush(openList,(start.fScore(), compCounter, start))
    compCounter = compCounter + 1

    # Loop while nodes are still available
    while openList:

        current = heapq.heappop(openList)
        closedList.append(current[2])

        # Exits if goal equals the current node
        if current[2].board == goal:
            print("done")
            global q 
            q = current[2]
            break 

        # Gets the possible moves (neighbours) of the current node and loops through them
        neighbours = generateMoveStates(current[2])
        for x in neighbours:

            # Skip neighbour if node is in closed
            if inClosedList(x.board,closedList):
                continue
            
            # Bulk of the algorithum'
            if not inOpenList(x.board,openList):
                x.f = (current[2].g + 1) + x.heuristic(x.board)
                x.parent = current[2]
                if not inOpenList(x.board,openList):
                    heapq.heappush(openList,(x.fScore(),compCounter, x))
                    compCounter += 1

    # Output
    steps = 0
    cur = q
    while cur != start:
        cur.printer()
        cur = cur.parent
        steps += 1
        print("      |")
        print("      |")
        print("      |")
        print("      v")
    
        
    start.printer()
    print(f"Steps To Goal: {steps}")


print("Enter Inital State")
inital = []
for i in range(0,3):
    temp = input().split(" ")
    temp = [int(i) for i in temp]
    inital.append(temp)

print("Enter Goal State")
goal = []
for i in range(0,3):
    temp = input().split(" ")
    temp = [int(i) for i in temp]
    goal.append(temp)

a = State(inital)
aStar(a)




