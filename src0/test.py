import sys

class Node():
    def __init__(self, state,parent=None,action=None):
        self.state = state
        self.parent = parent
        self.action = action

class StackFrontier():
    def __init__(self,):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)
    
    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node

    def print(self):
        for index, i in enumerate(self.frontier):
            print(f'==> Node{index}, state={i.state}, parent={i.parent}, action={i.action}')

class QueueFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node

class maze():
    def __init__(self, filename):
        with open(filename) as f:
            contents = f.read()
        
        if contents.count('A') != 1:
            raise Exception('maze must have begin A')
        if contents.count('B') != 1:
            raise Exception('maze must have end B')

        contents = contents.splitlines()
        self.height = len(contents)
        self.width = max(len(row) for row in contents)
        
        self.walls = []
        for i in range(self.height):
            rows = []
            for j in range(self.width):
                try:
                    if contents[i][j] == 'A':
                        self.start = (i, j)
                        rows.append(False)

                    elif contents[i][j] == 'B':
                        self.end = (i, j)
                        rows.append(False)

                    elif contents[i][j] == ' ':
                        rows.append(False)
                    
                    else:
                        rows.append(True)

                except IndexError:
                    rows.append(False)

            self.walls.append(rows)
        
        self.solution = None

        # print(self.walls)

    def print(self):

        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col :
                    print("█", end="")

                elif (i, j) == self.start:
                    print('A', end="")

                elif (i, j) == self.end:
                    print('B', end="")
                
                elif self.solution is not None and (i, j) in self.solution[1]:
                    print("*", end="")
                else:
                    print(' ', end="")
            print()
        print()

    def neighbors(self, state):
        row, col = state
        candidates = [
            ('Up', (row-1, col)),
            ('Down', (row+1, col)),
            ('Right', (row, col+1)),
            ('Left', (row, col-1))
        ]
        result = []
        for action, (r, c) in candidates:
            if 0 <= r < self.height and 0 <= c < self.width and not self.walls[r][c]:
                result.append((action, (r, c)))
        return result

        # for i in a:
        #     print(f'state = {i[1]}, action ={i[0]}')

    def solve(self):
        self.num_explore = 0
        start = Node(state = self.start)
        frontier = StackFrontier()
        frontier.add(start)

        self.explore = set()

        while True:
            if frontier.empty():
                raise Exception(" no solution")

            node = frontier.remove()
            # frontier = frontier.remove()
            self.num_explore += 1

            if node.state == self.end:
                actions = []
                cells = []
                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                return

            self.explore.add(node.state)

            for action, state in self.neighbors(node.state):
                if state not in self.explore and not frontier.contains_state(state):
                    child = Node(state = state, parent=node, action=action)
                    frontier.add(child)


if __name__ == "__main__":
    # f = QueueFrontier()
    # node1 = Node(state=(1,1))
    # f.add(node1)
    # node2 = Node(state=(1,2), parent=node1, action='Right')
    # f.add(node2)
    # node3 = Node(state=(2,2), parent=node2, action='Up')
    # f.add(node3)
    # node4 = Node(state=(2,3), parent=(node3), action='Right')
    # f.add(node4)
    # f.remove()
    # f.remove()
    # f.remove()

    # f.print()
    # print(f.empty())
    # f.remove()
    # if f.empty():
    #     print('empty')
    m = maze('maze2.txt')
    # m.solution = [(15,2), (15,3), (15, 4), (15, 5), (15, 6), (14, 6)]
    m.print()
    # m.neighbors((15,6))
    m.solve()
    m.print()
