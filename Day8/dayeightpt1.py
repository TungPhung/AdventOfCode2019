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

# Main Method
if __name__  == "__main__":
   
    width = 25
    height = 6
    
    zero_list = []
    one_two_list = []
    # Open file and read lines 
    with open("dayeightinput.txt", "r") as f:
        data = list(f.read().strip())

    #print(len(data)
    while(len(data) > 0):
         test, dataout, data = grab_layer(height, width, data) 
         zero_list.append(test)
         one_two_list.append(dataout)
       
    print(one_two_list[zero_list.index(min(zero_list))][0]*one_two_list[zero_list.index(min(zero_list))][1]) 
