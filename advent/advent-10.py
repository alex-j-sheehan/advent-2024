from pprint import pprint

def get_trailhead_score(grid, trailhead, path=[], paths=set(), level=0):
    curr_x = trailhead[0]
    curr_y = trailhead[1]

    if grid[curr_x][curr_y] == str(9):
        paths.add(tuple(path))
        return paths

    # up
    if curr_x > 0 and grid[curr_x - 1][curr_y] != '.' and int(grid[curr_x - 1][curr_y]) == level + 1:
        path.append(tuple((curr_x - 1, curr_y)))
        paths = get_trailhead_score(
            grid, 
            tuple((curr_x - 1, curr_y)),
            path=path,
            paths=paths,
            level=level + 1
        )

    # down
    if curr_x < len(grid) - 1 and grid[curr_x + 1][curr_y] != '.' and int(grid[curr_x + 1][curr_y]) == level + 1:
        path.append(tuple((curr_x + 1, curr_y)))
        paths = get_trailhead_score(
            grid, 
            tuple((curr_x + 1, curr_y)), 
            path=path,
            paths=paths,
            level=level + 1
        )

    # right
    if curr_y < len(grid[0]) - 1 and grid[curr_x][curr_y + 1] != '.' and int(grid[curr_x][curr_y + 1]) == level + 1:
        path.append(tuple((curr_x, curr_y + 1)))
        paths = get_trailhead_score(
            grid, 
            tuple((curr_x, curr_y + 1)), 
            path=path,
            paths=paths,
            level=level + 1
        )

    # left
    if curr_y > 0 and grid[curr_x][curr_y - 1] != '.' and int(grid[curr_x][curr_y - 1]) == level + 1:
        path.append(tuple((curr_x, curr_y - 1)))
        paths = get_trailhead_score(
            grid, 
            tuple((curr_x, curr_y - 1)), 
            path=path,
            paths=paths,
            level=level + 1
        )
    
    return paths

# PART 1 CODE 

# def get_trailhead_score(grid, trailhead, found=set(), found_9s=set(), level=0):
#     curr_x = trailhead[0]
#     curr_y = trailhead[1]

#     if grid[curr_x][curr_y] == str(9):
#         found_9s.add(tuple((trailhead)))
#         return found_9s

#     # up
#     if tuple((curr_x - 1, curr_y)) not in found:
#         if curr_x > 0 and grid[curr_x - 1][curr_y] != '.' and int(grid[curr_x - 1][curr_y]) == level + 1:
#             found.add(tuple((curr_x - 1, curr_y)))
#             found_9s = get_trailhead_score(
#                 grid, 
#                 tuple((curr_x - 1, curr_y)), 
#                 found=found, 
#                 found_9s=found_9s, 
#                 level=level + 1
#             )

#     # down
#     if tuple((curr_x + 1, curr_y)) not in found:
#         if curr_x < len(grid) - 1 and grid[curr_x + 1][curr_y] != '.' and int(grid[curr_x + 1][curr_y]) == level + 1:
#             found.add(tuple((curr_x + 1, curr_y)))
#             found_9s = get_trailhead_score(
#                 grid, 
#                 tuple((curr_x + 1, curr_y)), 
#                 found=found, 
#                 found_9s=found_9s,
#                 level=level + 1
#             )

#     # right
#     if tuple((curr_x, curr_y + 1)) not in found:
#         if curr_y < len(grid[0]) - 1 and grid[curr_x][curr_y + 1] != '.' and int(grid[curr_x][curr_y + 1]) == level + 1:
#             found.add(tuple((curr_x, curr_y + 1)))
#             found_9s = get_trailhead_score(
#                 grid, 
#                 tuple((curr_x, curr_y + 1)), 
#                 found=found, 
#                 found_9s=found_9s, 
#                 level=level + 1
#             )

#     # left
#     if tuple((curr_x, curr_y - 1)) not in found:
#         if curr_y > 0 and grid[curr_x][curr_y - 1] != '.' and int(grid[curr_x][curr_y - 1]) == level + 1:
#             found.add(tuple((curr_x, curr_y - 1)))
#             found_9s = get_trailhead_score(
#                 grid, 
#                 tuple((curr_x, curr_y - 1)), 
#                 found=found, 
#                 found_9s=found_9s, 
#                 level=level + 1
#             )
    
#     return found_9s


with open("./inputs/input_10.txt", "r") as file:
    input_text = file.read()

    lines = input_text.strip().split('\n')
    grid = [list(line) for line in lines]

    rolling_sum = 0
    for x, line in enumerate(grid):
        for y, char in enumerate(line):
            if char != '.' and char != '*' and int(char) == 0:
                thing = set()
                thing_2 = set()
                trailhead_score = get_trailhead_score(
                    grid, 
                    tuple((x,y)), 
                    path=[], 
                    paths=set(),
                    level=0
                )
                rolling_sum += len(trailhead_score)

    print(f"Rolling sum: {rolling_sum}")
