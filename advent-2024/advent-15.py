# https://adventofcode.com/2024/day/15

from pprint import pprint

# Setup & Helper functions
directions = {
    '>': (0, 1), 
    'v': (1, 0), 
    '<': (0, -1), 
    '^': (-1, 0)
}

# simple method to niavely determine if a move is possible
def can_be_moved(grid, direction, coord):
    x, y = coord
    dx, dy = directions[direction]
    while True:
        new_x, new_y = x + dx, y + dy
        if grid[new_x][new_y] == '#':
            return False
        if grid[new_x][new_y] == '.':
            return True

        x = new_x
        y = new_y

# method to check if there is a wall blocking a stack of 2-wide boxes
def look_for_block(grid, direction, coord, found=False):
    x, y = coord
    dx, dy = directions[direction]
    new_x, new_y = x + dx, y + dy

    if grid[new_x][new_y] == '#':
        return True
    
    if grid[new_x][new_y] == '.':
        return False
    
    next_coord_1 = (new_x, new_y)
    if grid[new_x][new_y] == ']':
        next_coord_2 = (new_x, new_y - 1)
    elif grid[new_x][new_y] == '[':
        next_coord_2 = (new_x, new_y + 1)

    return look_for_block(grid, direction, next_coord_1, found) or look_for_block(grid, direction, next_coord_2, found)

# method to return whether one or more stacked blocks can be pushed in a particular direction 
def can_move_big_room(grid, direction, coord):
    if direction in ['<', '>']:
        return can_be_moved(grid, direction, coord)

    x, y = coord
    dx, dy = directions[direction]

    return not look_for_block(grid, direction, coord)

# helper method to print grids
def print_grid(grid):
    for x, line in enumerate(grid):
        yo = ''
        for y, char in enumerate(line):
            yo += char
            if char == '@':
                robot_pos = (x, y)
        print(yo)

# method to recursively push a stack of zero, one or more 2x1 blocks
def push_connected_boxes(grid, direction, coord, moved):
    x, y = coord
    dx, dy = directions[direction]
    new_x, new_y = x + dx, y + dy

    # Edge case- if we're looking at an empty space, return
    if grid[x][y] == '.':
        return grid

    # Add the current coord to the list of coords dealt with
    moved.add(coord)

    # With 2x1 blocks, pushing up and down comes with the possibilities of uneven stacks 
    if direction in ['^', 'v']:

        # Checking for a stack:
        # if the space being pushed to is not empty, and not a wall
        if grid[new_x][new_y] != '.' and grid[new_x][new_y] != '#':
            # Push what's above in the stack first, before pushing lower in the stack
            grid = push_connected_boxes(
                grid,
                direction,
                (new_x, new_y),
                moved,
            )

        # Now that everything above this block has been pushed, push this block
        # First, make sure to push the entire block
        if grid[x][y] == ']':
            if (x,y - 1) not in moved:
                grid = push_connected_boxes(
                    grid,
                    direction,
                    (x, y - 1),
                    moved,
                )
        elif grid[x][y] == '[':
            if (x, y + 1) not in moved:
                grid = push_connected_boxes(
                    grid,
                    direction,
                    (x, y + 1),
                    moved,
                )
    else:
        # If we're pushing left or right, we don't need to worry about stacks
        # Recursively push blocks at the end of the stack first 
        if grid[new_x][new_y] != '.':
            grid = push_connected_boxes(
                grid,
                direction,
                (new_x, new_y),
                moved,
            )
        
    # Finally, 'push' the current node
    grid[new_x][new_y] = grid[x][y] 
    grid[x][y] = '.'

    return grid

# method to push zero, one or more 1x1 blocks
def move_pieces(grid, direction, coord):
    new_grid = grid[::]
    x, y = coord
    dx, dy = directions[direction]

    # if we're moving without pushing boxes
    if grid[x + dx][y + dy] == '.':
        new_grid[x][y] = '.'
        new_grid[x + dx][y + dy] = '@'
        return new_grid

    # if we're pushing a box
    elif grid[x + dx][y + dy] == 'O':
        new_grid[x][y] = '.'
        new_grid[x + dx][y + dy] = '@'
        x += dx
        y += dy

        while True:
            if grid[x + dx][y + dy] == '.':
                new_grid[x + dx][y + dy] = 'O'
                return new_grid
            x += dx
            y += dy

# PART 1
# with open("./inputs-2024/input_15a.txt", "r") as file:
#     input_text = file.read()
#     lines = input_text.strip().split('\n')
#     grid = []
#     steps = ''
#     for line in lines:
#         row = list(line)
#         if len(row) > 0 and row[0] == "#":
#             grid.append(row)
#         elif len(row) > 1 and "#" not in row:
#             steps += line

# for x, line in enumerate(grid):
#     for y, char in enumerate(line):
#         if grid[x][y] == '@':
#             robot_pos = x, y
#             break

# for char in steps:
#     if can_be_moved(grid, char, robot_pos):
#         new_x, new_y = directions[char]
#         robot_pos_x, robot_pos_y = robot_pos
#         new_robot_pos = (robot_pos_x + new_x, robot_pos_y + new_y)
#         grid = move_pieces(grid, char, robot_pos)
#         robot_pos = new_robot_pos


# rolling_sum = 0
# for x, line in enumerate(grid):
#     for y, char in enumerate(line):
#         if char == 'O':
#             rolling_sum += 100 * x + y

# print(f"part 1: {rolling_sum}")

# PART 2
print("PART 2")
with open("./inputs-2024/input_15.txt", "r") as file:
    input_text = file.read()
    lines = input_text.strip().split('\n')
    grid = []
    steps = ''
    for line in lines:
        row = list(line)
        if len(row) > 0 and row[0] == "#":
            new_line = ''
            for char in row:
                if char == '#':
                    new_line += '##'
                elif char == 'O':
                    new_line += '[]'
                elif char == '@':
                    new_line += '@.'
                elif char == '.':
                    new_line += '..'
            grid.append(list(new_line))
        elif len(row) > 0 and "#" not in row:
            steps += line

print("starting pos")
for x, line in enumerate(grid):
    yo = ''
    for y, char in enumerate(line):
        yo += char
        if char == '@':
            # set robot_pos for the calculations
            robot_pos = (x, y)
    print(yo)


for char in steps:
    if can_move_big_room(grid, char, robot_pos):
        new_x, new_y = directions[char]
        robot_pos_x, robot_pos_y = robot_pos
        new_robot_pos = (robot_pos_x + new_x, robot_pos_y + new_y)
        grid = push_connected_boxes(grid, char, new_robot_pos, set())
        new_rob_x, new_rob_y = new_robot_pos
        grid[new_rob_x][new_rob_y] = '@'
        grid[robot_pos_x][robot_pos_y] = '.'
        robot_pos = new_robot_pos
    
    print_grid(grid)

print("Final position:")
print_grid(grid)

rolling_sum = 0
for x, line in enumerate(grid):
    for y, char in enumerate(line):
        if char == '[':
            rolling_sum += 100 * x + y

print(f"part 2: {rolling_sum}")
