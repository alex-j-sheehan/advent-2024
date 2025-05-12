# https://adventofcode.com/2024/day/3

with open("./inputs-2024/input_3.txt","r", encoding="utf8") as file:
    rolling_sum = 0
    enabled = True
    for line in file:
        do_line = ""
        for index, char in enumerate(line):
            if index <= (len(line) - 8):
                if line[index:index + 7] == "don't()":
                    enabled = False
            if index <= (len(line) - 4):
                if line[index:index + 4] == "do()":
                    enabled = True
            if enabled:
                do_line += char

        split_up = do_line.split("mul(")
        for split in split_up:
            func_call = split.split(")")[0]
            params = func_call.split(',')
            if (len(params) == 2):
                p1 = params[0]
                p2 = params[1]
                p1_d = len(str(p1)) 
                p2_d = len(str(p2)) 
                if p1.isdigit() and p2.isdigit() and p1_d > 0 and p1_d <= 3 and p2_d > 0 and p2_d <= 3:
                    rolling_sum += (int(p1) * int(p2))
print(rolling_sum)