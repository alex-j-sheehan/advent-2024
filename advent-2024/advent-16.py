import heapq
from pprint import pprint


def solve_reindeer_maze(grid, start, end):
    paths = []
    # Directions
    directions = {
        0: (0, 1),   # East (>)
        1: (1, 0),   # South (v)
        2: (0, -1),  # West (<)
        3: (-1, 0)   # North (^)
    }
    start_x, start_y = start

    # (score, x, y, direction)
    queue = [(0, start_x, start_y, 0, [(start_x, start_y)])]
    
    visited = {}
    while queue:
        score, x, y, direction, path = heapq.heappop(queue)
        state = (x, y, direction)

        if state in visited and visited[state] < score:
            continue

        if (x, y) == end:
            if len(paths) > 0:
                if score <= paths[0][0]:
                    if score == paths[0][0]:
                        paths.append((score, path))
                    else:
                        paths = [(score, path)]
            else:
                paths.append((score, path))
            
            continue

        visited[state] = score

        # add going forward to the queue
        fdx, fdy = directions[direction]
        forward_x, forward_y = (x + fdx, y + fdy)
        if grid[forward_x][forward_y] != '#':
            new_state = (forward_x, forward_y, direction)
            if new_state not in visited or visited[new_state] > score + 1:
                new_path = path.copy()
                new_path.append((forward_x, forward_y))
                heapq.heappush(queue, (score + 1, forward_x, forward_y, direction, new_path))

        # add going right to the queue
        rfdx, rfdy = directions[(direction + 1) % 4]
        right_x, right_y = (x + rfdx, y + rfdy)
        if grid[right_x][right_y] != '#':

            new_state = (right_x, right_y, (direction + 1) % 4)
            if new_state not in visited or visited[new_state] > score + 1001:
                new_path = path.copy()
                new_path.append((right_x, right_y))
                heapq.heappush(queue, (score + 1001, right_x, right_y, (direction + 1) % 4, new_path))

        # add going left to the queue
        lfdx, lfdy = directions[(direction - 1) % 4]
        left_x, left_y = (x + lfdx, y + lfdy)
        if grid[left_x][left_y] != '#':

            new_state = (left_x, left_y, (direction - 1) % 4)
            if new_state not in visited or visited[new_state] > score + 1001:
                new_path = path.copy()
                new_path.append((left_x, left_y))
                heapq.heappush(queue, (score + 1001, left_x, left_y, (direction - 1) % 4, new_path))

    set_of_unique_coords = set()
    for path in paths:
        for coord in path[1]:
            set_of_unique_coords.add(coord)
    return set_of_unique_coords

# Main code
with open("./inputs-2024/input_16.txt", "r") as file:
    input_text = file.read()
    lines = input_text.strip().split('\n')
    grid = []
    start = (0, 0)
    end = (0, 0)
    
    for x, line in enumerate(lines):
        row = list(line)
        if len(row) > 0:
            for y, char in enumerate(line):
                if char == 'S':
                    start = (x, y)
                elif char == 'E':
                    end = (x, y)
            grid.append(row)
    
    if start == end:
        print("Something went wrong")
    else:
        unique_best_paths_spots = solve_reindeer_maze(grid, start, end)

        # printing for verification
        for x, line in enumerate(grid):
            line_str = ''
            for y, char in enumerate(line):
                if (x, y) in unique_best_paths_spots:
                    line_str += 'O'
                else:
                    line_str += grid[x][y]
            pprint(line_str) 

        print(len(set(unique_best_paths_spots)))
