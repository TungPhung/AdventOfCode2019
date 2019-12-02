# Day One of Advent of Code
# Author - Tung Phung
# Date 12/1/2019

import os, sys

# Fuel Calculator
def fuel_calc(x):
   return x // 3 - 2

#Instantiate module_list
module_list = []

# Read in input
f = open("dayoneinput.txt", "r")
for x in f:
    module_list.append(int(x.strip()))

module_list = [fuel_calc(x) for x in module_list]

print(sum(module_list))
