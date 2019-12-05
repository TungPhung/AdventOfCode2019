# Day Five of Advent of Code
# Author - Tung Phung
# Date 12/5/2019

# Imports
import os, sys

# Read in input
with open("dayfiveinput.txt", "r") as f:
    main_list = f.read().strip().split(",")

# Convert main list to ints
main_list = list(map(int, main_list)) 

# Decode opcode into command, and three parameter modes, in list format where
# [opcode, parameter_mode_1, parameter_mode_2, parameter_mode_3] in integers
def opcode_decode(opcode_undecoded):
    #Instantiates return opcode list
    opcode_list = []
    
    # Pulls off opcode value off two trailing values and adds as first value in
    # return list
    opcode_list.append(opcode_undecoded % 100)
    opcode_undecoded = opcode_undecoded // 100
    
    # Adds the rest of the parameter nodes and fills in 0 for trailing
    # parameter modes that aren't explicitly stated 
    opcode_list.extend(reversed([int(x) for x in str(opcode_undecoded)]))
    while(len(opcode_list) < 4):
       opcode_list.append(0)
    #Returns opcode_list
    return opcode_list

# Test assertions for opcode_decode
assert opcode_decode(1002) == [2,0,1,0]
assert opcode_decode(1103) == [3,1,1,0]
assert opcode_decode(1) == [1,0,0,0]
assert opcode_decode(2) == [2,0,0,0]
assert opcode_decode(3) == [3,0,0,0]
assert opcode_decode(4) == [4,0,0,0]
assert opcode_decode(1101) == [1,1,1,0]

# Opcode 1 - Adds values at two positions and saves at a third position
def opcode_1(start_position, param1, param2, param3, list):
    # Determines first value based on param1
    if param1 == 0:
        value_one = list[list[start_position + 1]]
    else:
        value_one = list[start_position + 1]

    # Determines second value based on param2
    if param2 == 0:
        value_two = list[list[start_position + 2]]
    else:
        value_two = list[start_position + 2]

    # Since param3 does nothing for now, it will always be in position mode
    list[list[start_position + 3]] = value_one + value_two
    
    # Returns edited list        
    return list

# Opcode 2 - Multiplies values at two positions and saves at a third position
def opcode_2(start_position, param1, param2, param3, list):
    # Determines first value based on param1
    if param1 == 0:
        value_one = list[list[start_position + 1]]
    else:
        value_one = list[start_position + 1]

    # Determines second value based on param2
    if param2 == 0:
        value_two = list[list[start_position + 2]]
    else:
        value_two = list[start_position + 2]

    # Since param3 does nothing for now, it will always be in position mode
    list[list[start_position + 3]] = value_one * value_two
    
    # Returns edited list        
    return list

assert opcode_2(0,0,1,0,[1002,4,3,4,33]) == [1002,4,3,4,99]

# Opcode 3 - Takes input instruction and puts value at position
def opcode_3(input_value, position, list):
    list[list[position]] = input_value
    return list

# Opcode 4 - Takes value at either next position index or the index the next
# position specifies, does not return
def opcode_4(position, param1, list):
    if param1 == 0:
        print(list[list[position]])
    else:
        print(list[position])
  
if __name__ == "__main__":  

    def main_loop(input_value, main_list):
        # Starting Position
        current_position = 0
        
        # Moves through int code as long as it doesn't encounter a halt code
        # 99/99999
        while((main_list[current_position] != 99) and (main_list[current_position] != 99999)):
            deciphered_code = opcode_decode(main_list[current_position])
            if (deciphered_code[0] == 1):
                main_list = opcode_1(current_position, deciphered_code[1],
                deciphered_code[2], deciphered_code[3], main_list)
                current_position += 4
            elif (deciphered_code[0] == 2):
                main_list = opcode_2(current_position, deciphered_code[1],
                deciphered_code[2], deciphered_code[3], main_list)
                current_position += 4
            elif (deciphered_code[0] == 3):
                main_list = opcode_3(input_value, current_position + 1,
                main_list)
                current_position += 2
            elif (deciphered_code[0] == 4):
                opcode_4(current_position + 1, deciphered_code[1], main_list)
                current_position += 2
    
    # Run main loop
    main_loop(1, main_list)
