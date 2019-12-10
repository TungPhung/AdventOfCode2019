# Day Eight of Advent of Code
# Author - Tung Phung
# Date 12/8/2019

# Imports
import os, sys

def grab_layer(height, width, main_list):
    sub = main_list[0:height*width]
    main_list = main_list[height*width:]
    x = sub.count('0')
    y = sub.count('1')
    z = sub.count('2')
    return x, (y,z), main_list

def layer_only(height, width, main_list):
    sub = main_list[0:height*width]
    main_list = main_list[height*width:]
    return sub, main_list

# Main Method
if __name__  == "__main__":
   
    width = 25
    height = 6
    
    total_list = []
    final_pixel_list = []
    # Open file and read lines 
    with open("dayeightinput.txt", "r") as f:
        data = list(f.read().strip())

    len_data = len(data)
    while(len(data) > 0):
        layer, data = layer_only(height, width, data)
        total_list.append(layer)
    
    for x in range(len(total_list[0])):
        for y in range(len(total_list)):
            if(total_list[y][x]=='2'):
                continue
            elif(total_list[y][x]=='1'):
                final_pixel_list.append("*")
                break
            elif(total_list[y][x]=='0'):    
                final_pixel_list.append(" ")
                break
    
    print("".join(final_pixel_list[:25]))
    print("".join(final_pixel_list[25:50]))
    print("".join(final_pixel_list[50:75]))
    print("".join(final_pixel_list[75:100]))
    print("".join(final_pixel_list[100:125]))
    print("".join(final_pixel_list[125:150]))
