map = """3
7 4
2 4 6
8 5 9 3""".split("\n")
grid = []
for i in range(len(map)):
    grid.append([int(i) for i in map[i].split(" ")])
    print(i,grid[i])

for i in range(len(grid)-1,0,-1):
    for j in range(len(grid[i])):
        print(grid[i-1][j])

