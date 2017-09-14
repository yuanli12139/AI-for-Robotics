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
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1  # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']


# def compute_value(grid, goal, cost):  # reverse search
#     # ----------------------------------------
#     # insert code below
#     # ----------------------------------------
#     value = [[99 for col in range(len(grid[0]))] for row in range(len(grid))]
#     value[goal[0]][goal[1]] = 0
#
#     open = [[0, goal[0], goal[1]]]
#     flag = list(grid)
#
#     while 1:
#         open.sort()
#         curr = open[0]
#
#         open.pop(0)
#         for i in range(len(delta)):
#             expand = [x + y for x, y in zip(curr[-2:], delta[i])]
#
#             r = expand[0]
#             c = expand[1]
#
#             if 0 <= r <= goal[0] and 0 <= c <= goal[1]:  # robot must drive in the grid
#                 if flag[r][c] is 0:  # position not checked yet
#                     g = [curr[0] + cost]
#                     open.append(g + expand)
#                     flag[r][c] = 1
#                     if value[r][c] == 99:
#                         value[r][c] = g[0]
#
#         if not open:  # no more to expand
#             break
#
#     # make sure your function returns a grid of values as
#     # demonstrated in the previous video.
#     return value


def compute_value(grid, goal, cost):  # dynamic programming: f(x, y) = min{f(x, y)} + cost
    # ----------------------------------------
    # insert code below
    # ----------------------------------------
    value = [[99 for col in range(len(grid[0]))] for row in range(len(grid))]

    update = True
    while update:
        update = False

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if r == goal[0] and c == goal[1] and value[r][c] > 0:
                    value[r][c] = 0
                    update = True

                elif grid[r][c] == 0:
                    for i in range(len(delta)):
                        r2 = r + delta[i][0]
                        c2 = c + delta[i][1]

                        if 0 <= r2 <= goal[0] and 0 <= c2 <= goal[1] and value[r][c] > value[r2][c2] + cost:
                            value[r][c] = value[r2][c2] + cost
                            update = True

    # make sure your function returns a grid of values as
    # demonstrated in the previous video.
    return value

print compute_value(grid, goal, cost)
