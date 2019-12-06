# Day Five of Advent of Code
# Author - Tung Phung
# Date 12/5/2019

# Imports
import os, sys

# Create dictionary of lists of each and things that orbit them
def raw_data_convert(data):
    orbit_dict = {}
    for x in data:
        orbit_1, orbit_2 = x.strip().split(")")
        if orbit_1 not in orbit_dict:
            orbit_dict[orbit_1] = []
        orbit_dict[orbit_1].append(orbit_2)
    return orbit_dict

def orbit_count(x, orbit_dict):
    count = 0
    for each in orbit_dict.get(x, []):
        count += orbit_count(each, orbit_dict)
        count += 1
    return count

# Main Method
if __name__  == "__main__":
   
    # Open file and read lines 
    with open("daysixinput.txt", "r") as f:
        data = f.readlines()
    
    # Convert data to dictionary of orbits
    orbit_dict = raw_data_convert(data)
   
    # Print Answer 
    print(sum([orbit_count(x,orbit_dict) for x in orbit_dict]))

    # Testing Only
    # test  = ['COM)B','B)C','C)D','D)E','E)F','B)G','G)H','D)I','E)J','J)K','K)L']
    # test_dict = raw_data_convert(test)
    # print(sum([orbit_count(x,test_dict) for x in test_dict]))  
