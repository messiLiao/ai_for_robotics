# ----------
# User Instructions:
# 
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal. 
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
grid = [[0, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0]]
# grid = [[0, 0, 1, 0, 0, 0],
#         [0, 0, 1, 0, 0, 0],
#         [0, 0, 1, 0, 0, 0],
#         [0, 0, 0, 0, 1, 0],
#         [0, 0, 1, 1, 1, 0],
#         [0, 0, 0, 0, 1, 0]]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def compute_value(grid,goal,cost):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------
    v_grid = [[ 99 for x in row] for row in grid]
    v_grid[goal[0]][goal[1]] = 0
    ele_set1 = set()
    ele_set1.add((goal[0], goal[1]))
    cost = 0
    while True:
        ele_set2  = set()
        cost += 1
        for x, y in ele_set1:
            for dx, dy in delta:
                nx, ny = x + dx, y + dy
                if nx >= 0 and ny >= 0 and nx < len(grid) and ny < len(grid[0]) and grid[nx][ny] < 1 and v_grid[nx][ny] == 99 and not (nx == goal[0] and ny == goal[1]) :
                    ele_set2.add((nx, ny))
        if len(ele_set2) == 0:
            break
        for x, y in ele_set2:
            v_grid[x][y] = cost
        ele_set1 = ele_set2
        # break
        
    
    # make sure your function returns a grid of values as 
    # demonstrated in the previous video.
    value = v_grid
    return value 

print compute_value(grid, goal, cost)
