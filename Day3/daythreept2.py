# Day Three of Advent of Code
# Author - Tung Phung
# Date 12/3/2019

# Imports
import os, sys

# Read in input
List = open("daythreeinput.txt").readlines()
path_one = List[0].strip().split(",")
path_two = List[1].strip().split(",")

# Returns set of all unique points a single cable goes through in x, y coordinate plane
def path_set(path):
    cable_path = {(0,0)}
    current_x = 0
    current_y = 0
    for x in path:
        direction = x[0]
        distance = int(x[1:])
        if direction == "U":
             for _ in range(distance):
                 current_y += 1
                 cable_path.add((current_x, current_y))
        elif direction == "D":
             for _ in range(distance):
                 current_y -= 1
                 cable_path.add((current_x, current_y))
        elif direction == "R":
             for _ in range(distance):
                 current_x += 1
                 cable_path.add((current_x, current_y))
        if direction == "L":
             for _ in range(distance):
                 current_x -= 1
                 cable_path.add((current_x, current_y))
    return cable_path

def path_set_with_steps_dict(path):
    steps_dict = dict()
    current_x = 0
    current_y = 0
    steps = 0
    for x in path:
        direction = x[0]
        distance = int(x[1:])
        if direction == "U":
             for _ in range(distance):
                 current_y += 1
                 steps += 1
                 steps_dict[steps] = (current_x, current_y)
        elif direction == "D":
             for _ in range(distance):
                 current_y -= 1
                 steps += 1
                 steps_dict[steps] = (current_x, current_y)
        elif direction == "R":
             for _ in range(distance):
                 current_x += 1
                 steps += 1
                 steps_dict[steps] = (current_x, current_y)
        if direction == "L":
             for _ in range(distance):
                 current_x -= 1
                 steps += 1
                 steps_dict[steps] = (current_x, current_y)
    return steps_dict

# Returns list of all manhattan distances for a set of (x,y) tuples that have origin 0, 0
def manhattan_distance(set_of_xy_tuples):
    distance_list = []
    for x in set_of_xy_tuples:
        distance_list.append(abs(x[0]) + abs(x[1]))
    return distance_list

# Returns list of all minimum step totals to get to each intersection for a set of (x,y) tuples that have origin 0,0
# This is a shitty way to do it, I think
def steps_distance(intersected_paths, path_one_dict, path_two_dict):
    final_steps_list = []
    # Iterate through each intersection, checking with each path dictionary the least amount of steps to get there
    # then add the total steps to a main list for comparison to other intersections
    for i in intersected_paths:
        temp_list_1 = []
        temp_list_2 = []
        total_steps = []
        for key, value in path_one_dict.items():
            if i == value:
                temp_list_1.append(key)    
        for key, value in path_two_dict.items():
            if i == value:
                temp_list_2.append(key)
        total_steps = min(temp_list_1) + min(temp_list_2)
        final_steps_list.append(total_steps)
    
    return min(final_steps_list)

# Does all calculations based on input of two string lists of directions
def calculate_min_steps(list_1, list_2):
    # Convert input list of strings into path dictionaries
    path_one_dict = path_set_with_steps_dict(list_1)
    path_two_dict = path_set_with_steps_dict(list_2)
    
    # Convert all values into a set of all unique points crossed by each path
    path_one_set = set(path_one_dict.values())
    path_two_set = set(path_two_dict.values())
    
    # Determines intersected paths with union of two sets
    intersected_paths = path_one_set & path_two_set

    # Removes origin point if it exists
    intersected_paths.discard((0,0))

    # Returns minimum intersection with least steps required
    return steps_distance(intersected_paths, path_one_dict, path_two_dict)

# Main method    
if __name__ == "__main__":
    # Test cases
    assert calculate_min_steps(['R75','D30','R83','U83','L12','D49','R71','U7','L72'], ['U62','R66','U55','R34','D71','R55','D58','R83']) == 610
    assert calculate_min_steps(['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51'], ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']) == 410

    # Main case
    print(calculate_min_steps(path_one, path_two))
