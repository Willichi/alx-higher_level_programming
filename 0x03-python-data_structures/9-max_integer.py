#!/usr/bin/python3
def max_integer(my_list=[]):
    """
    a function that finds the biggest integer of a list.
    """
    for i in range len(my_list) - 1:
        if my_list == []:
           return None
              max_value = max_integer(my_list[i])
         print("max_value: {:d} ".format(my_list[i]))
