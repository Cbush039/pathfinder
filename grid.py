class Grid:
    def __init__(self, width, height, start, goal, walls=None):
        self.width = width
        self.height = height
        self.start = start
        self.goal = goal
        if walls is None:
            walls = set()
        self.walls = walls

    def display(self, path=None):
        for row in range(self.height):
            for col in range(self.width):
                cell = (row, col)
                if cell == self.start:
                    print("S", end=" ")
                elif cell == self.goal:
                    print("G", end=" ")
                # use in rather than == because in checks for if there is one in the set, not the entire thing needing to be equal to the set.
                elif cell in self.walls:
                    print("#", end=" ")
                elif path and cell in path:
                    print("*", end=" ")
                else:
                    print(".", end=" ")

            print()
