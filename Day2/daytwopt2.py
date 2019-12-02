# Day Two of Advent of Code
# Author - Tung Phung
# Date 12/2/2019

# Imports
import os, sys

# Read in input
f = open("daytwoinput.txt", "r")
for x in f:
    main_list = x.strip().split(",")

# Convert main list to ints
main_list = list(map(int, main_list)) 

# Opcode 1 - Adds values at two positions and saves at a third position
def opcode_1(start_position, list):
    list[list[start_position + 3]] = list[list[start_position + 1]] + list[list[start_position + 2]]
    return list

# Opcode 2 - Multiplies values at two positions and saves at a third position
def opcode_2(start_position, list):
    list[list[start_position + 3]] = list[list[start_position + 1]] * list[list[start_position + 2]]
    return list

# Main Function
def main_loop(main_list):
    current_position = 0
    while(main_list[current_position] != 99):
        if(main_list[current_position] == 1):
            main_list = opcode_1(current_position, main_list)
        elif (main_list[current_position] == 2):
            main_list = opcode_2(current_position, main_list)
        current_position += 4
    return main_list

# Find noun and verb that correspond to target_value    
def target(target_value, main_list):
    for i in range(0,100):
        for j in range(0,100):    
            temp_list = main_list[:]
            temp_list[1] = i
            temp_list[2] = j
            temp_list = main_loop(temp_list)
            if(temp_list[0] == target_value):
                return i,j

# Set target_value
target_1, target_2 = target(19690720, main_list)

# Print calculated noun/verb combo via 100*noun + verb formula
print(100*target_1 + target_2)
