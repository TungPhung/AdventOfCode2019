# Day Four of Advent of Code
# Author - Tung Phung
# Date 12/4/2019

# Imports
import os, sys

# Puzzle Input
low_range = 124_075
high_range = 580_769

# Password Condition 1 - Length of password is six digits
def is_length_six (int_value):
    if len(str(int_value)) == 6:
       return True
    else:
       return False

# Password Condition 2 - Password has dougle digits, but not more than 2 sequentially.
def has_double_digits (int_value):
    value_string = str(int_value)
    value_length = len(value_string)
    # Sets up value dictionary with counts of each number
    value_dict = dict(zip('0123456789',[0]*10))
    for i in range(value_length):
        value_dict[value_string[i]] = value_dict[value_string[i]] + 1 
 
    # Iterates through and finds pairs of numbers and checks with value_dict if it only appears twice
    for i in range(1, value_length):
        if value_string[i] == value_string[i-1]:
            if value_dict[value_string[i]] == 2:
                return True
    return False

# Password Condition 3 - Password values never decrease going left to right, only stay the same or increse
def never_decreases (int_value):
    value_string = str(int_value)
    value_length = len(value_string)
    count = 0 
    for i in range(1, value_length):
        if value_string[i] >= value_string[i-1]:
            count += 1
    if count == 5:
        return True
    else:
        return False

# Determines if password meets criteria, returns True if it does.
def password_check(int_value):      
    if is_length_six(int_value):
        if has_double_digits(int_value):
            if never_decreases(int_value):
                return True
    return False

# Password Generator Function - iterates through possible range and returns list of possible passwords
# Would probably gain a speed increase if I combined conditions 2 and 3 into same loop
def generate_password_list(low_range, high_range):
    password_list = []    
    for i in range(low_range, high_range+1):
        if password_check(i):
            password_list.append(i)
    return password_list

# Main method    
if __name__ == "__main__":
    # Test cases
    assert password_check(112233) == True
    assert password_check(123444) == False
    assert password_check(111122) == True
 
    # Prints length of generated password list
    print(len(generate_password_list(low_range, high_range)))

