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

# grid = [[0, 0, 1, 0, 0, 0],
#         [0, 0, 1, 0, 0, 0],
#         [0, 0, 0, 0, 1, 0],
#         [0, 0, 1, 1, 1, 0],
#         [0, 0, 0, 0, 1, 0]]
# grid = [[0, 1, 0, 1, 0, 0],
#         [0, 1, 0, 1, 0, 0],
#         [0, 1, 0, 1, 0, 0],
#         [0, 1, 0, 1, 0, 0],
#         [0, 0, 0, 1, 0, 0]]
grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']


def search(grid, init, goal, cost):
    # ----------------------------------------
    # insert code here
    open = [[0] + init]
    flag = list(grid)

    while 1:
        open.sort()
        curr = open[0]

        open.pop(0)
        for i in range(len(delta)):
            expand = [x + y for x, y in zip(curr[-2:], delta[i])]

            r = expand[0]
            c = expand[1]

            if 0 <= r <= goal[0] and 0 <= c <= goal[1]:  # robot must drive in the grid
                if flag[r][c] is 0:  # position not checked yet
                    g = [curr[0] + cost]
                    open.append(g + expand)
                    flag[r][c] = 1
                    #print curr
        if not open:  # no more to expand
            break

    if curr[-2:] == goal:
        path = curr
    else:
        path = "fail"
    # ----------------------------------------

    return path

print search(grid, init, goal, cost)
