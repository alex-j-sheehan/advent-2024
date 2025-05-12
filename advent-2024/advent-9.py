# https://adventofcode.com/2024/day/9

from pprint import pprint

with open("./inputs-2024/input_9.txt", "r") as file:
    input_text = file.read().strip('\n')

id = 0
working_string = ''
memory_array = []
for index, char in enumerate(input_text):
    if index % 2 > 0:
        for x in range(int(char)):
            memory_array.append('.')
            working_string = working_string + '.'
    else:
        for _ in range(int(char)):
            working_string = working_string + str(id)
            memory_array.append(str(id))
        id += 1

def find_free_space(block, file_length, file_start):
    curr = 0
    while curr < file_start:
        x = block[curr]
        if x == '.':
            length = get_free_len(block, curr)
            if length >= file_length and curr < file_start:
                return curr, length
            curr += length
        else:
            curr += 1

    return -1, -1

def get_free_len(block, start):
    file_id = block[start]
    curr = start
    length = 0
    try:
        while curr < len(block) and block[curr] == file_id:
            length += 1
            curr += 1
        return length
    except IndexError as exc:
        import pdb;
        pdb.set_trace()
        p = 10 

def get_file_len(block, file):
    file_id = block[file]
    curr = file
    length = 0
    while block[curr] == file_id and curr >= 0:
        length += 1
        curr -= 1
    return length

def swap_file_location(memory_array, free_space_start, file_start, file_length, file_id):
    for x in range(file_length):
        memory_array[free_space_start + x] = file_id
        memory_array[file_start + x] = '.'
    
    return memory_array

y = len(memory_array) - 1
run = 0
farthest_up_memory_injection_index = 0
while y > 0:
    if memory_array[y] != '.':
        file_id = memory_array[y]
        print(f'attempting to shift file: {file_id}...')
        file_length = get_file_len(memory_array, y)
        y = y - file_length + 1

        free_space_start, free_space_length = find_free_space(memory_array, file_length, y)
        if free_space_start > 0:
            print(f'swapping file: {file_id} to index: {free_space_start}')
            memory_array = swap_file_location(memory_array, free_space_start, y, file_length, file_id)
            farthest_up_memory_injection_index = free_space_start
        else:
            print(f'failed to shift file: {file_id}, no suitable space found')
    y -= 1

rolling_sum = 0
for index, x in enumerate(memory_array):
    if x != '.':
        rolling_sum += int(x) * index

print(rolling_sum)