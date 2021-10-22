def minPathSum(grid) -> int:
    k = []
    temp = 0
    for i in range(len(grid[0])):
        temp += grid[0][i]
        k.append(temp)
    temp = grid[0][0]
    k = [k]
    for j in range(1, len(grid)):
        temp += grid[j][0]
        tt = [[temp] + [0] * (len(grid[0]) - 1)]
        k = k + tt
    for i in range(1, (len(grid))):
        for j in range(1, (len(grid[0]))):
            k[i][j] = min(k[i - 1][j], k[i][j - 1]) + grid[i][j]
    print(k)
    return k[len(grid) - 1][len(grid[0]) - 1]

grid = [[1,3,1],[1,5,1],[4,2,1]]
p = minPathSum(grid)
