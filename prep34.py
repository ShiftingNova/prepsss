def get_highest_neighbor(grid,one,two):
    value = grid[one][two]
    if value < grid[one-1][two]:
        value = grid[one-1][two]
    if value < grid[one+1][two]:
        value = grid[one+1][two]
    if value < grid[one][two+1]:
        value = grid[one][two+1]
    if value < grid[one][two-1]:
        value = grid[one][two-1]
    return value
