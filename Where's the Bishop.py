def solve():
    for i in range(1, 7):
        for j in range(1, 7):
            if grid[i-1][j-1] == grid[i-1][j+1] == grid[i+1][j-1] == grid[i+1][j+1] == "#":
                print(i+1, j+1)
                return
 
for i in range(int(input())):
    grid = []
    for i in range(8):
        arr = [item for item in input()]
        grid.append(arr)
    solve()