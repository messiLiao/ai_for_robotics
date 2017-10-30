# -----------
# User Instructions
#
# Define a function smooth that takes a path as its input
# (with optional parameters for weight_data, weight_smooth,
# and tolerance) and returns a smooth path. The first and 
# last points should remain unchanged.
#
# Smoothing should be implemented by iteratively updating
# each entry in newpath until some desired level of accuracy
# is reached. The update should be done according to the
# gradient descent equations given in the instructor's note
# below (the equations given in the video are not quite 
# correct).
# -----------

from copy import deepcopy

# thank you to EnTerr for posting this on our discussion forum
def printpaths(path,newpath):
    for old,new in zip(path,newpath):
        print '['+ ', '.join('%.3f'%x for x in old) + \
               '] -> ['+ ', '.join('%.3f'%x for x in new) +']'

# Don't modify path inside your function.
path = [[0, 0],
        [0, 1],
        [0, 2],
        [1, 2],
        [2, 2],
        [3, 2],
        [4, 2],
        [4, 3],
        [4, 4]]

def smooth(path, weight_data = 0.5, weight_smooth = 0.1, tolerance = 0.000001):

    # Make a deep copy of path into newpath
    newpath = deepcopy(path)

    #######################
    ### ENTER CODE HERE ###
    #######################
    error  = 1e9
    while error > tolerance:
        temp_path = []
        error = 0.0
        for i, (x, y) in enumerate(path):
            if (i == 0) or (i == len(path) - 1):
                temp_path.append((x, y))
                continue
            nx, ny = newpath[i]
            yi_x = nx + weight_data * (x - nx)
            yi_y = ny + weight_data * (y - ny)

            yi_x = nx + weight_smooth * (path[i-1][0] + path[i+0][0] - 2 * nx)
            yi_y = ny + weight_smooth * (path[i-1][1] + path[i+1][1] - 2 * ny)

            error += (yi_y - ny) ** 2 + (yi_x - nx) ** 2
            temp_path.append((yi_x, yi_y))
            print error
        newpath = temp_path
        # yi = yi + alpha * (yi - xi)
        # yi_x = 
        # yi = yi + beta * (yi_1 + yi_2 - 2 * yi)
        pass
    return newpath # Leave this line for the grader!

printpaths(path,smooth(path))
