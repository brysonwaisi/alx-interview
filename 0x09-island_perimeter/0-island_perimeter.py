#!/usr/bin/python3
'''Island Perimeter problem'''


def island_perimeter(grid):
    # initialize a set data structure
    visit = set()

    # helper function dfs
    def dfs(i, j, visit):
        if (i, j) in visit or grid[i][j] == 0:
            return 1
        visit.add((i, j))
        perimeter = dfs(i, j + 1, visit)
        perimeter += dfs(i + 1, j, visit)
        perimeter += dfs(i, j - 1, visit)
        perimeter += dfs(i - 1, j, visit)
        return perimeter

    # iterate over the grid and find the first land cell to start the DFS
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                return dfs(i, j, visit)

    # return 0 if no land cells are found
    return 0
