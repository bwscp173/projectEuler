map = ""
with open("0067_triangle.txt","r") as f:
    map = f.readlines()

grid = []
for i in range(len(map)):
    grid.append([int(i) for i in map[i].split(" ")])


def solve_layer(grid,index):
    total = 0
    for i in range(len(grid)-1-index,0,-1):
        if i == len(grid)-1-index:
            continue
        for j in range(len(grid[i])):
            if j == len(grid[i])-1:
                continue#when its at the last number on the row just pick the ij index
            grid[i+index][j] += max(grid[i][j],grid[i][j+1])
            total = grid[i+index][j]
    print("total:",total)

solve_layer(grid,-1)