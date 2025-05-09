# Convert Base-10 to Base-3
def ternary (n, min_digits=0):
    if n == 0:
        return '0'.zfill(min_digits)
    nums = []

    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    result = ''.join(reversed(nums))

    return result.zfill(min_digits)

with open("./inputs/input_7.txt", "r") as file:
    running_value = 0
    for line in file:
        split = line.split(':')
        candidate = int(split[0])
        entry = split[1].lstrip(' ')
        num_operations = entry.count(' ')
        nums = entry.split(' ')
        largest_bin = "2" * num_operations
        num_steps = 3 ** num_operations
        for x in range(num_steps):
            operations_str = ternary(x, num_operations)
            result = int(nums[0])

            for index, y in enumerate(operations_str):
                if y == '0':
                    result = result + int(nums[index + 1])
                elif y == '1':
                    result = int( str(result) + str(nums[index + 1]) )
                else:
                    result = result * int(nums[index + 1])
            
            if result == candidate:
                running_value += candidate
                print("found!")
                break

print(running_value)
