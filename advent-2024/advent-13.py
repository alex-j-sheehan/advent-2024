# https://adventofcode.com/2024/day/13

import numpy as np

def is_close_to_integer(value, tolerance=1e-10):
    return np.isclose(value, round(value), atol=tolerance)

with open("./inputs-2024/input_13.txt", "r") as file:
    input_text = file.read()

    lines = input_text.strip().split('\n')

    total = 0
    for index, line in enumerate(lines):
        if 'Button A' in line:
            but_a = line.strip('Button A: ').split(', ')
            button_a_x = int(but_a[0].strip('X+'))
            button_a_y = int(but_a[1].strip('Y+'))

            but_b = lines[index + 1].strip('Button B: ').split(', ')
            button_b_x = int(but_b[0].strip('X+'))
            button_b_y = int(but_b[1].strip('Y+'))

            prize = lines[index + 2].strip('Prize: ').split(', ')
            
            # Part 2
            prize_x = int(prize[0].strip('X=')) + 10000000000000
            prize_y = int(prize[1].strip('Y=')) + 10000000000000

            # Part 1
            # prize_x = int(prize[0].strip('X='))
            # prize_y = int(prize[1].strip('Y='))

            # Coefficient matrix A
            A = np.array([[button_a_x, button_b_x], 
                        [button_a_y, button_b_y]])

            # Constants vector b
            b = np.array([prize_x, prize_y])

            # Solve the system- 
            # We're essentially given two linear equations for X and Y and can therefore solve
            solution = np.linalg.solve(A, b)

            x,y = solution
            if x >= 0 and y >= 0:
                # np can return an int with floating points ie 40 - 40.0000000000001 or 39.99999999999999 
                if is_close_to_integer(x) and is_close_to_integer(y):
                    # We have to round instead of casting to int
                    x_int = round(x)
                    y_int = round(y)
                    # Now that we've rounded, doublely make sure the rounded numbers fit our equation
                    x_check = x_int * button_a_x + y_int * button_b_x
                    y_check = x_int * button_a_y + y_int * button_b_y
                    if x_check == prize_x and y_check == prize_y:
                        # If so, increment our total accounting for A button presses taking 3 tokens
                        total += (x_int * 3) + y_int

    print(total)
