# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    g_x, g_y = goal
    try_path = [[0, init[0], init[1]]]
    path = []
    path_dict = {}
    while True:
        if len(try_path) == 0:
            path = []
            break

        path = []
        for c, x, y in try_path:
            grid[x][y] = 1
            if x == g_x and y == g_y:
                path.append((c, x, y))
        if len(path) > 0:
            break
        for c, x, y in try_path:
            for i, (dx, dy) in enumerate(delta):
                nx, ny = x + dx, y + dy
                valid_path = (c + cost, nx, ny)
                if (0 <= nx < len(grid)) and (0 <= ny < len(grid[0])) and (grid[nx][ny] == 0) and valid_path not in path:
                    path.append(valid_path)
                    path_key = ((init[0], init[1]), (nx, ny))
                    if c == 0:
                        path_dict[path_key] = [(init[0], init[1], ' '), (nx, ny, delta_name[i])]
                    elif c > 0:
                        pre_key = ((init[0], init[1]), (x, y))
                        pre_path = path_dict[pre_key][:]
                        pre_path.append((nx, ny, delta_name[i]))
                        path_dict[path_key] = pre_path
            # print path_dict

        try_path = path
    expand = [[' ' for i in range(len(grid[0]))] for j in range(len(grid))]
    expand[x][y] = 0
    expand_index = 1

    path_key = ((init[0], init[1]), (goal[0], goal[1]))
    if path_key in path_dict:
        valid_path = path_dict[path_key]
        for i in range(1, len(valid_path)):
            x, y, ch = valid_path[i-1]
            _, _, ch = valid_path[i]
            expand[x][y] = ch
    expand[g_x][g_y] = '*'
    try_path = []
    for valid_path in path:
        try_path.extend(valid_path)

    path = try_path
    if len(path) == 0:
        path = 'fail'
    return expand

print search(grid,init,goal,cost)
