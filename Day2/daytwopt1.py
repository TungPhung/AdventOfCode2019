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
    
# Replace values at two positions according to prompt
main_list[1] = 12
main_list[2] = 2

# Run main loop
main_list = main_loop(main_list)
print(main_list)
