def get_highest_sum(grid):
    most = 0
    for i in range(len(grid)):
        if len(grid[i])%2==0:
            for e in range(len(grid[i])-1):
                temp = grid[i][e] + grid[i][e+1]
                if temp > most:
                    most = temp
        else:
            for e in range(len(grid[i])-2):
                temp = grid[i][e] + grid[i][e + 1]
                if temp > most:
                    most = temp
    return most
