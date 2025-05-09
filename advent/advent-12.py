from pprint import pprint
# def check_down(grid, x, y, value):
#     if y < (len(grid[x]) - 1):
#         if value == grid[x][y + 1]:
#             return True
#     return False

# def check_up(grid, x, y, value):
#     if y > 0:
#         if value == grid[x][y - 1]:
#             return True
#     return False

# def check_left(grid, x, y, value):
#     if x > 0:
#         if value == grid[x - 1][y]:
#             return True
#     return False

# def check_right(grid, x, y, value):
#     if x < (len(grid[x]) - 1):
#         if value == grid[x + 1][y]:
#             return True
#     return False


# def find_all_attached_nodes(grid, coord, found, num_nodes=0, area_cost = 0, exposed_sides=0):
#     x, y = coord
#     found.add((x, y, grid[x][y]))
#     num_nodes = num_nodes + 1

#     if check_down(grid, x, y, grid[x][y]):
#         if (x, y + 1, grid[x][y]) not in found:
#             exposed_sides, found, num_nodes = find_all_attached_nodes(
#                 grid, 
#                 (x, y + 1), 
#                 found=found, 
#                 num_nodes=num_nodes,
#                 exposed_sides=exposed_sides
#             )
#     else:
#         exposed_sides += 1

#     if check_right(grid, x, y, grid[x][y]):
#         if (x + 1, y, grid[x][y]) not in found:
#             exposed_sides, found, num_nodes = find_all_attached_nodes(
#                 grid, 
#                 (x + 1, y), 
#                 found=found, 
#                 num_nodes=num_nodes,
#                 exposed_sides=exposed_sides
#             )
#     else:
#         exposed_sides += 1

#     if check_up(grid, x, y, grid[x][y]):
#         if (x, y - 1, grid[x][y]) not in found:
#             exposed_sides, found, num_nodes = find_all_attached_nodes(
#                 grid, 
#                 (x, y - 1), 
#                 found=found, 
#                 num_nodes=num_nodes,
#                 exposed_sides=exposed_sides
#             )
#     else:
#         exposed_sides += 1

#     if check_left(grid, x, y, grid[x][y]):
#         if (x - 1, y, grid[x][y]) not in found:
#             exposed_sides, found, num_nodes = find_all_attached_nodes(
#                 grid, 
#                 (x - 1, y), 
#                 found=found, 
#                 num_nodes=num_nodes,
#                 exposed_sides=exposed_sides
#             )
#     else:
#         exposed_sides += 1

#     return exposed_sides, found, num_nodes


# with open("./inputs/input_12.txt", "r") as file:
#     input_text = file.read()

#     lines = input_text.strip().split('\n')
#     grid = [list(line) for line in lines]
#     found = set()
#     total_cost = 0
#     for x, row in enumerate(grid):
#         for y, node in enumerate(row):
#             if (x, y, grid[x][y]) not in found:
#                 exposed_sides, found, num_nodes = find_all_attached_nodes(grid, (x,y), found)
#                 total_cost += exposed_sides * num_nodes
#                 print(f"num_nodes!: {num_nodes}")

# print(total_cost)


def check_down(grid, x, y, value):
    if y < (len(grid[x]) - 1):
        if value == grid[x][y + 1]:
            return True
    return False

def check_up(grid, x, y, value):
    if y > 0:
        if value == grid[x][y - 1]:
            return True
    return False

def check_left(grid, x, y, value):
    if x > 0:
        if value == grid[x - 1][y]:
            return True
    return False

def check_right(grid, x, y, value):
    if x < (len(grid[x]) - 1):
        if value == grid[x + 1][y]:
            return True
    return False


def find_all_attached_nodes(grid, coord, found, num_nodes=0, area_cost = 0, exposed_sides=0):
    x, y = coord
    found.add((x, y, grid[x][y]))
    num_nodes = num_nodes + 1

    if check_down(grid, x, y, grid[x][y]):
        if (x, y + 1, grid[x][y]) not in found:
            exposed_sides, found, num_nodes = find_all_attached_nodes(
                grid, 
                (x, y + 1), 
                found=found, 
                num_nodes=num_nodes,
                exposed_sides=exposed_sides
            )
    else:
        exposed_sides += 1

    if check_right(grid, x, y, grid[x][y]):
        if (x + 1, y, grid[x][y]) not in found:
            exposed_sides, found, num_nodes = find_all_attached_nodes(
                grid, 
                (x + 1, y), 
                found=found, 
                num_nodes=num_nodes,
                exposed_sides=exposed_sides
            )
    else:
        exposed_sides += 1

    if check_up(grid, x, y, grid[x][y]):
        if (x, y - 1, grid[x][y]) not in found:
            exposed_sides, found, num_nodes = find_all_attached_nodes(
                grid, 
                (x, y - 1), 
                found=found,
                num_nodes=num_nodes,
                exposed_sides=exposed_sides
            )
    else:
        exposed_sides += 1

    if check_left(grid, x, y, grid[x][y]):
        if (x - 1, y, grid[x][y]) not in found:
            exposed_sides, found, num_nodes = find_all_attached_nodes(
                grid, 
                (x - 1, y), 
                found=found, 
                num_nodes=num_nodes,
                exposed_sides=exposed_sides
            )
    else:
        exposed_sides += 1

    return exposed_sides, found, num_nodes

def count_tota_sides(found_items):
    unique_sides = 0
    for item in found_items:
        x, y, v = item
        # UP
        if (x - 1, y, v) not in found_items and ((x, y - 1, v) not in found_items or (x - 1, y - 1, v) in found_items):
            unique_sides += 1
        
        # Down
        if (x + 1, y, v) not in found_items and ((x, y + 1, v) not in found_items or (x + 1, y + 1, v) in found_items):
            unique_sides += 1

        # RIGHT
        if (x, y + 1, v) not in found_items and ((x - 1, y, v) not in found_items or (x - 1, y + 1, v) in found_items):
            unique_sides += 1

        # Left
        if (x, y - 1, v) not in found_items and ((x + 1, y, v) not in found_items or (x + 1, y - 1, v) in found_items):
            unique_sides += 1
    return unique_sides

with open("./inputs/input_12.txt", "r") as file:
    input_text = file.read()

    lines = input_text.strip().split('\n')
    grid = [list(line) for line in lines]
    found = set()
    total_cost = 0
    for x, row in enumerate(grid):
        for y, node in enumerate(row):
            if (x, y, grid[x][y]) not in found:
                exposed_sides, new_found, num_nodes = find_all_attached_nodes(grid, (x,y), set())

                unique_sides = count_tota_sides(new_found)
                found = found.union(new_found)
                total_cost += unique_sides * num_nodes
                print(f"garden of {grid[x][y]} has unique_sides!: {unique_sides}")

print(total_cost)