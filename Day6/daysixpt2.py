# Day Five of Advent of Code
# Author - Tung Phung
# Date 12/5/2019
# Based on code from (Jonathan Paulson
# https://www.youtube.com/watch?v=45KTbNv_gP0)
# Thanks for helping me understand BFS better!

# Imports
import os, sys
from collections import deque

#Calculate distance distance between two nodes
def orbit_distance(body1, body2, orbit_dict):
    # Instantiate dictionary to hold key:value pairs of BODY:distance in
    # reference to body1
    distance_dict = {}
    
    # Deque so we can pop/append from both ends sequentially
    deque_list = deque()
    
    #Start deque list with the reference body
    deque_list.append((body1, 0))
    
    # While deque_list has values
    while deque_list:
        # Grab the most recent element (FIFO)
        value, distance = deque_list.popleft()
    
        # If the value is not in the distance dictionary already, do not add,
        # continue with next iteration
        if value in distance_dict:
            continue
        
        # Add to distance dict the distance
        distance_dict[value] = distance
        
        # Add all the children of this new node as one further distance away
        for x in orbit_dict[value]:
            deque_list.append((x, distance + 1))
    
    # Return distance dict to body2, minus 2, because we do not count the last
    # legs to each
    return distance_dict[body2] - 2

# Create dictionary of lists of each and things that orbit them
def raw_data_convert(data):
    orbit_dict = {}
    for x in data:
        orbit_1, orbit_2 = x.strip().split(")")
        if orbit_1 not in orbit_dict:
            orbit_dict[orbit_1] = []
        if orbit_2 not in orbit_dict:
            orbit_dict[orbit_2] = []
        
        #Add bi-direction references, otherwise we can't complete a BFS
        orbit_dict[orbit_1].append(orbit_2)
        orbit_dict[orbit_2].append(orbit_1)
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
  
    # Find distance from YOU to SAN
    print(orbit_distance('YOU', 'SAN', orbit_dict)) 
