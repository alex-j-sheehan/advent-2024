from pprint import pprint
from collections import Counter
from copy import copy

def rule_1(zeros, to_multiply):
    new_to_mult = Counter()
    if zeros[0]:
        new_to_mult[1] += zeros[0]
        del zeros[0]
    return new_to_mult, zeros

def rule_2(evens, zeros, to_multiply):
    zeros_copy = Counter()
    evens_copy = Counter()
    to_mult_copy = Counter()
    for even in evens:
        side_a, side_b = tuple((str(even)[:int(len(str(even))/2)], str(even)[int(len(str(even))/2):]))
        if len(str(side_a)) % 2 == 0:
            evens_copy[int(side_a)] += evens[even]
        else:
            to_mult_copy[int(side_a)] += evens[even]
        
        if int(side_b) == 0:
            zeros_copy[int(side_b)] += evens[even]
        elif len(str(int(side_b))) % 2 == 0:
            evens_copy[int(side_b)] += evens[even]
        else:
            to_mult_copy[int(side_b)] += evens[even]
            
    return evens_copy, zeros_copy, to_mult_copy

def rule_3(to_multiply, evens):
    evens_copy = Counter()
    to_mult_copy = Counter()
    for stone in to_multiply:
        new_stone = int(stone) * 2024
        if len(str(new_stone)) % 2 == 0:
            evens_copy[int(new_stone)] += to_multiply[stone]
        else:
            to_mult_copy[int(new_stone)] += to_multiply[stone]
    return evens_copy, to_mult_copy

def apply_rules(zeros, evens, to_multiply):
    new_to_mult, zeros = rule_1(zeros, to_multiply)
    evens_copy, zeros_copy, other_new_mult = rule_2(evens, zeros, to_multiply)
    other_evens_copy, other_other_to_mult_copy = rule_3(to_multiply, evens)
    return new_to_mult + other_new_mult + other_other_to_mult_copy, zeros + zeros_copy, evens_copy + other_evens_copy


with open("./inputs/input_11.txt", "r") as file:
    # Setup
    input_text = file.read()
    zeros = Counter()
    evens = Counter()
    to_multiply = Counter()
    stones = input_text.strip('\n').split()
    for stone in stones:
        if int(stone) == 0:
            zeros[int(stone)] += 1
        elif len(str(stone)) % 2 == 0:
            evens[int(stone)] += 1
        else:
            to_multiply[int(stone)] += 1

    # Apply rules over blinks
    for x in range(75):
        to_multiply, zeros, evens = apply_rules(zeros, evens, to_multiply)
        print("blink")

rolling_sum = 0 
together = (to_multiply + zeros + evens)
for x in together:
    rolling_sum += together[x]
            
print(rolling_sum)


    