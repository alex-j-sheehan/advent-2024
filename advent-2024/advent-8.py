# https://adventofcode.com/2024/day/8

from pprint import pprint
from math import sqrt, gcd

def find_points_on_line(grid, p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    
    dx, dy = (x2 - x1, y2 - y1)
    gcd_value = gcd(abs(dx), abs(dy))
    dx_reduced = dx // gcd_value
    dy_reduced = dy // gcd_value

    x, y = x1, y1
    antinodes = set()
    while 0 <= x < len(grid) and 0 <= y < len(grid[0]):
        if (x,y) != (x2, y2):
            antinodes.add((x, y))
        x += dx_reduced
        y += dy_reduced
    
    x, y = x1 - dx_reduced, y1 - dy_reduced
    while 0 <= x < len(grid) and 0 <= y < len(grid[0]):
        if (x,y) != (x2, y2):
            antinodes.add((x, y))
        x -= dx_reduced
        y -= dy_reduced
    
    return antinodes

def find_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

def is_point_on_line(p1, p2, point):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = point
    return ((x2 - x1) * (y3 - y1)) - ((y2 - y1) * (x3 - x1)) == 0

def is_point_in_between(p1, p2, point):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = point

    if (x1 >= x3 and x3 >= x2) or (x1 <= x3 and x3 <= x2):
        if (y1 >= y3 and y3 >= y2) or (y1 <= y3 and y3 <= y2):
            return True
    return False

def mirror_point(grid, point, ref_point):
    x1, y1 = point
    x2, y2 = ref_point

    reflected_x = 2 * x2 - x1
    reflected_y = 2 * y2 - y1

    if reflected_x >= 0 and reflected_x < len(grid):
        if reflected_y >= 0 and reflected_y < len(grid[reflected_x]):
            return (reflected_x, reflected_y)

def mirror_points_indef(grid, point, ref_point):
    running_list = []

    x1, y1 = point
    x2, y2 = ref_point

    reflected_x = 2 * x2 - x1
    reflected_y = 2 * y2 - y1

    while (reflected_x >= 0 and reflected_x < len(grid)) and (reflected_y >= 0 and reflected_y < len(grid[reflected_x])):
        running_list.append([reflected_x, reflected_y])

        temp = reflected_x
        reflected_x = 2 * reflected_x - x2
        x2 = temp

        temp = reflected_y
        reflected_y = 2 * reflected_y - y2
        y2 = temp

    return running_list


found_antinodes = set()

with open("./inputs-2024/input_8.txt", "r") as file:
    input_text = file.read()

    lines = input_text.strip().split('\n')
    grid = [list(line) for line in lines]
    frequencies = {}
    for x, line in enumerate(grid):
        for y, char in enumerate(line):
            if char != '.':
                if char in frequencies:
                    frequencies[char].append([x, y])
                else:
                    frequencies[char] = [[x, y]]

    for key, frequency in frequencies.items():
        for index, coord in enumerate(frequency):
            other_coords = frequency[:index] + frequency[index + 1:]
            for index, other_coord in enumerate(other_coords):
                # dir_vect = find_dir_vect(coord, other_coord)
                antinodes = find_points_on_line(grid, coord, other_coord)
                # if antinodes := mirror_points_indef(grid, coord, other_coord):
                for antinode in antinodes:
                    found_antinodes.add(tuple(antinode))
                # if antinodes2 := mirror_points_indef(grid, other_coord, coord):
                #     for antinode2 in antinodes2:
                #         found_antinodes.add(tuple(antinode2))

print(len(found_antinodes))
for x, line in enumerate(grid):
    line_chars = ''
    for y, char in enumerate(line):
        if char == '.':
            if (x,y) in found_antinodes:
                line_chars = line_chars + "#"
            else:
                line_chars = line_chars + char
        else:
            line_chars = line_chars + char
    print(line_chars)