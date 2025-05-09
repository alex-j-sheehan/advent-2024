# https://adventofcode.com/2024/day/6

def solve_guard_puzzle(input_text):
    lines = input_text.strip().split('\n')
    grid = [list(line) for line in lines]
    
    # Find starting position and direction
    start_pos = None
    start_dir = None
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] in ['^', 'v', '<', '>']:
                start_pos = (i, j)
                if grid[i][j] == '^': start_dir = (-1, 0)  # Up
                elif grid[i][j] == 'v': start_dir = (1, 0)  # Down
                elif grid[i][j] == '<': start_dir = (0, -1)  # Left
                elif grid[i][j] == '>': start_dir = (0, 1)  # Right
                break
        if start_pos:
            break
    
    # Direction mapping for turns
    turn_right = {
        (-1, 0): (0, 1),   # Up -> Right
        (0, 1): (1, 0),    # Right -> Down
        (1, 0): (0, -1),   # Down -> Left
        (0, -1): (-1, 0)   # Left -> Up
    }
    
    def simulate_basic_path(grid, start_pos, start_dir):
        visited = set([start_pos])
        pos = start_pos
        dir = start_dir
        
        while True:
            # Calculate next position
            next_pos = (pos[0] + dir[0], pos[1] + dir[1])
            
            # Check if next position is out of bounds
            if (next_pos[0] < 0 or next_pos[0] >= len(grid) or 
                next_pos[1] < 0 or next_pos[1] >= len(grid[0])):
                break
            
            # Check if next position is an obstacle
            if grid[next_pos[0]][next_pos[1]] == '#':
                # Turn right
                dir = turn_right[dir]
            else:
                # Move forward
                pos = next_pos
                visited.add(pos)
        
        return visited
    
    visited = simulate_basic_path(grid, start_pos, start_dir)
    part1_answer = len(visited)

    def would_create_loop(grid, start_pos, start_dir, obstacle_pos):
        # Create a state key: (position, direction)
        state_history = {}
        pos = start_pos
        dir = start_dir
        step = 0
        
        # Maximum steps to prevent infinite loops
        max_steps = 4 * len(grid) * len(grid[0])
        
        while step < max_steps:
            state = (pos, dir)
            
            # If we've seen this state before, we've found a loop
            if state in state_history:
                return True
            
            # Record this state
            state_history[state] = step
            
            # Calculate next position
            next_pos = (pos[0] + dir[0], pos[1] + dir[1])
            
            # Check if next position is out of bounds
            if (next_pos[0] < 0 or next_pos[0] >= len(grid) or 
                next_pos[1] < 0 or next_pos[1] >= len(grid[0])):
                return False
            
            # Check if next position is an obstacle (including our new one)
            if grid[next_pos[0]][next_pos[1]] == '#' or next_pos == obstacle_pos:
                # Turn right
                dir = turn_right[dir]
            else:
                # Move forward
                pos = next_pos
            
            step += 1
        
        # If we've reached maximum steps without finding a loop or exiting,
        # we'll assume it's not a valid loop configuration
        return False
    
    loop_creating_obstacles = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # Only try empty spaces that aren't the start position
            if grid[i][j] == '.' and (i, j) != start_pos:
                if would_create_loop(grid, start_pos, start_dir, (i, j)):
                    loop_creating_obstacles.append((i, j))
    
    return part1_answer, len(loop_creating_obstacles)

with open("./inputs-2024/input_6.txt", "r") as file:
    input_text = file.read()

part1, part2 = solve_guard_puzzle(input_text)
print(f"Part 1: {part1}")
print(f"Part 2: {part2}")