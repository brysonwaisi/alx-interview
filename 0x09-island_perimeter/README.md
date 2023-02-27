# Island Perimeter
We count the perimeter of the island. 1s represent Island and 0s represent water.
We count the parts connected to the boundary with water
This is a graph problem that we will solve using DFS.

### DFS base cases
In the dfs functionality, we pass in coordinates of cells we are visiting and check the following base cases:
+ if we are out of bounds `i >= len(grid)` if `i` is greater or equal to the num of rows.
+ if `j` is equal or greater than num of columns `j >= len(grid[0])`
+ if `i < 0`
+ if `j < 0`
+ if position we reached is inbound `grid[i][j] == 0`
+ if position we reach is in visited set `if (i, j) in visit`

We then start adding to the perimeter on all 4 directions recursively.

Time Complexity: O(n * m)
Space Complexity: O(n * m)