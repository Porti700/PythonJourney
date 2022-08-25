# Given an array of integers, return a new array with each value doubled.

# For example:

# [1, 2, 3] --> [2, 4, 6]



def maps(list):
    double = []
    
    for item in list:
        double.append(item * 2)

    return double