# https://adventofcode.com/2024/day/14

from collections import Counter

GRID_LENGTH = 101
GRID_HEIGHT = 103

def print_guards(guards):
    for x in range(GRID_LENGTH):
        line = ''
        for y in range(GRID_HEIGHT):
            if (x, y) in guards:
                line += 'X'
            else:
                line += '.'

        print(line)

def check_for_continuous_guards(guards):
    visited = set()
    segment_lengths = []

    directions = [
        (0, 1), (1, 0), (0, -1), (-1, 0),  # Up, right, down, left
        (1, 1), (1, -1), (-1, -1), (-1, 1)  # Diagonals
    ]

    def dfs(x, y):
        visited.add((x, y))
        size = 1
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if (new_x, new_y) in guards and (new_x, new_y) not in visited:
                size += dfs(new_x, new_y)

        return size
    
    for x, y in guards:
        if (x, y) not in visited:
            segment_length = dfs(x, y)
            segment_lengths.append(segment_length)

    for segment in segment_lengths:
        # Bit of massaging here to find the right threshold
        # Had to play with this as we don't know how big/how many nodes make up the tree
        if segment > 30:
            return True

    return False

def calculate_future_position(velocity, position, seconds):
    velocity_x, velocity_y = velocity
    velocity_x = int(velocity_x)
    velocity_y = int(velocity_y)

    current_x, current_y = position
    current_x = int(current_x)
    current_y = int(current_y)

    for step in range(seconds):
        current_x += velocity_x
        current_y += velocity_y

        if current_x >= GRID_LENGTH:
            current_x -= GRID_LENGTH
        elif current_x < 0:
            current_x += GRID_LENGTH
        
        if current_y >= GRID_HEIGHT:
            current_y -= GRID_HEIGHT
        elif current_y < 0:
            current_y += GRID_HEIGHT

    return (current_x, current_y)

def calculate_quadrant(p):
    # Quandrant number doesn't matter so long as it's consistent 
    x, y = p
    quadrant = 1

    if x > int(GRID_LENGTH/2):
        pass
    elif x < int(GRID_LENGTH/2):
        quadrant += 1
    else:
        return -1

    if y > int(GRID_HEIGHT/2):
        pass
    elif y < int(GRID_HEIGHT/2):
        quadrant += 2
    else:
        return -1
    return quadrant


with open("./inputs-2024/input_14.txt", "r") as file:
    input_text = file.read()

    lines = input_text.strip().split('\n')

    guards = []

    for line in lines:
        p, v = line.split(' ')
        p = p.strip('p=')
        v = v.strip('v=')
        p = tuple(p.split(','))
        v = tuple(v.split(','))
        guards.append((p, v))
    
    for x in range(10000):
        quadrants = Counter()
        new_positions = set()
        new_guards = []
        for guard in guards:
            p, v = guard
            guard_future_position = calculate_future_position(v, p, 1)
            quadrant = calculate_quadrant(guard_future_position)
            new_positions.add(guard_future_position)

            new_guards.append((guard_future_position, v))

            if quadrant > 0:
                quadrants[quadrant] += 1
        
        if check_for_continuous_guards(new_positions):
            print(f"Found one! Second: {x + 1}")
            print_guards(new_positions)
        
        guards = new_guards
    
sum = 1
for quadrant in quadrants:
    sum *= quadrants[quadrant]

print(f"sum from multiplying number of robots in each quadrant: {sum}")
