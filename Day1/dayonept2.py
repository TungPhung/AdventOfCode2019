# Day One of Advent of Code
# Author - Tung Phung
# Date 12/1/2019

import os, sys

# Basic Fuel Calculator
def fuel_calc(x):
   return x // 3 - 2

# Complex Fuel Calculator (Calculates fuel for fuel and outputs list of fuel amounts instead of singular amount)
def fuel_fuel_calc(x):
    temp_list = []
    temp_list.append(fuel_calc(x))
    is_true = True
    while (is_true):
      new_fuel_calc = fuel_calc(temp_list[-1])
      if new_fuel_calc > 0:
         temp_list.append(new_fuel_calc)
      else:
          is_true = False
    return temp_list

#Instantiate module_list
module_list = []

# Read in input
f = open("dayoneinput.txt", "r")
for x in f:
    module_list.append(int(x.strip()))

# Testing Only
#print(fuel_fuel_calc(100756))
#print(sum(fuel_fuel_calc(100756)))

# Process Fuel Amounts
module_list = [fuel_fuel_calc(x) for x in module_list]
print(sum([sum(x) for x in module_list]))

