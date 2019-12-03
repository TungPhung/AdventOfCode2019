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

# Returns list of all manhattan distances for a set of (x,y) tuples that have origin 0
def manhattan_distance(set_of_xy_tuples):
    distance_list = []
    for x in set_of_xy_tuples:
        distance_list.append(abs(x[0]) + abs(x[1]))
    return distance_list

# Main Method
if __name__ == "__main__":

    # Find path sets for both of our input paths
    set_path_one = path_set(path_one)
    set_path_two = path_set(path_two)
    
    # Use set operation (&) to find union of our two paths (coordinates that match)
    intersected_paths = set_path_one & set_path_two
    
    # Remove (0,0) from path intersection, as the origin is not a valid point
    intersected_paths.discard((0,0))
    
    # Calculate min_manhattan distance
    min_manhattan_distance = min(manhattan_distance(intersected_paths))
    
    # Print min_manhattan_distance
    print(min_manhattan_distance)
