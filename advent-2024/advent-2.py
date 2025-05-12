# https://adventofcode.com/2024/day/2

def check_safe(levels, decreasing, safe=True):
    for index, level in enumerate(levels):
        if isinstance(level, str):
            level = int(level.strip('\n'))
        levels[index] = level

        if index < len(levels) - 1:
            if decreasing:
                if level <= int(levels[index + 1]):
                    safe = False
                    print()
                    print("FOUND NOT SAFE INCREASING WHEN LIST DECREASING")
                    print(f"item 1: {level}, item 2: {int(levels[index + 1])}")
                    print(levels)
                    print()
                    break
            else:
                if level >= int(levels[index + 1]):
                    safe = False
                    print()
                    print("FOUND NOT SAFE DECREASING WHEN LIST INCREASING")
                    print(f"item 1: {level}, item 2: {int(levels[index + 1])}")
                    print(levels)
                    print()
                    break
            
            diff = abs(level - int(levels[index + 1]))

            if safe and (diff > 3 or diff < 1):
                safe = False
                print()
                print("FOUND NOT SAFE DIFFER MORE THAN THREE")
                print(f"item 1: {level}, item 2: {int(levels[index + 1])}")
                print(levels)
                print()
                break

    return safe


with open("./inputs-2024/input_2.txt","r", encoding="utf8") as file:
    num_safe = 0
    for report in file:
        levels = report.split(' ')
        decreasing = True
        safe = True
        if int(levels[0]) < int(levels[1]):
            decreasing = False

        safe = check_safe(levels, decreasing, safe)

        if not safe:
            for index, item in enumerate(levels):
                new_list = levels[:index] + levels[index + 1:]
                decreasing = True
                if int(new_list[0]) < int(new_list[1]):
                    decreasing = False
                if check_safe(new_list, decreasing):
                    num_safe += 1
                    print(f"reduced report: {new_list} safe! level: {item} ommited from report: {levels}")
                    break
        else:
            print(f"report: {levels} safe!")
            num_safe += 1

return num_safe

