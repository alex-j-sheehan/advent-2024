word_array = []

with open("./inputs/input_4.txt","r", encoding="utf8") as file:
    for line in file:
        line_array = []
        for char in line:
            if char != '\n':
                line_array.append(char)
        
        word_array.append(line_array)

def check_down(word_array, x, y):
    if (y + 4) <= len(word_array[x]):
        if ("".join(word_array[x][y:y+4]) == 'XMAS' or "".join(word_array[x][y:y+4])[::-1] == 'XMAS'):
            print(f"FOUND DOWN {word_array[x][y:y+4]}!")
            print()
            return True
    return False

def check_left(word_array, x, y):
    if (x >= 3):
        arrays = word_array[x - 3 : x + 1]
        left_string = ""
        for array in arrays:
            left_string += array[y]
        if (left_string == 'XMAS' or left_string[::-1] == 'XMAS'):
            print(f"FOUND LEFT {list(left_string)}!")
            print()
            return True
    return False

def check_diag_right_up(word_array, x, y):
    if (x + 4) <= len(word_array):
        if y >= 3:
            up_right_diag_string = ""
            for itr, column in enumerate(word_array[x : x + 4]):
                up_right_diag_string += column[y - itr]

            if (up_right_diag_string == 'XMAS' or up_right_diag_string[::-1] == 'XMAS'):
                print(f"FOUND UP RIGHT DIAG {list(up_right_diag_string)}!")
                print()
                return True
    return False

def check_diag_right_down(word_array, x, y):
    if (x + 4) <= len(word_array):
        if (y + 4) <= len(word_array[x]):
            down_right_diag_string = ""
            for itr, column in enumerate(word_array[x : x + 4]):
                try:
                    down_right_diag_string += column[y + itr]
                except Exception as exc:
                    print(f"something went wrong: {exc}")

            if (down_right_diag_string == 'XMAS' or down_right_diag_string[::-1] == 'XMAS'):
                print(f"FOUND DOWN RIGHT DIAG {list(down_right_diag_string)}!")
                print()
                return True
    
def check_xmas(word_array, x, y, num_found):
    if check_down(word_array, index_x, index_y):
        num_found += 1
    if check_left(word_array, index_x, index_y):
        num_found += 1
    if check_diag_right_up(word_array, index_x, index_y):
        num_found += 1
    if check_diag_right_down(word_array, index_x, index_y):
        num_found += 1
    return num_found

def check_surrounding_corners(word_array, x, y):
    TL_BR_corners = [word_array[x - 1][y - 1], word_array[x + 1][y + 1]]
    TR_BL_corners = [word_array[x - 1][y + 1], word_array[x + 1][y - 1]]
    if "M" in TL_BR_corners and "S" in TL_BR_corners:
        if "M" in TR_BL_corners and "S" in TR_BL_corners:
            return True

    return False

def check_x_mas(word_array, x, y, num_found):
    if word_array[x][y] == 'A':
        if y > 0 and y <= len(word_array[x]) - 2:
            if x > 0 and x <= len(word_array) - 2:
                if check_surrounding_corners(word_array, x, y):
                    num_found += 1
    return num_found

num_found = 0
for index_x, x in enumerate(word_array):
    for index_y, y in enumerate(x):
        num_found = check_x_mas(word_array, index_x, index_y, num_found)

print(num_found)