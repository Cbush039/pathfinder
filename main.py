from grid import Grid

walls = {(0, 3), (1, 3), (2, 3), (3, 3)}
g = Grid(width=6, height=4, start=(0, 0), goal=(3, 5), walls=walls)
g.display()
