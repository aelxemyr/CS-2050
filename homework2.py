# Bennett Alex Myers
# CS 2050 - Homework 2
# 8 Feburary 2016

import random
import string
import time
import mergesort

# Ask the user for an integer value

def get_integer(prompt):
    while True:
        try:
            n = int(input(prompt))
            break
        except ValueError:
            print("The previous value was not valid.")
    return n

# Ask the user for a floating point value

def get_float(prompt):
    while True:
        try:
            n = float(input(prompt))
            break
        except ValueError:
            print("The previous value was not valid.")
    return n

# Generate an array of random integers

def integer_array(size, big):
    return random.sample(range(big), size)
    
# Generate an array of random real numbers

def float_array(size):
    l = []
    for i in range(size):
        l.append(random.uniform(0.0, 1.0))
    return l    

# Generate a random string composed of uppercase letters, lowercase letters,
# and numbers

def random_string(size):
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return "".join(random.choice(chars) for i in range(size))

# Generate an array of random strings

def string_array(size):
    l = []
    for i in range(size):
        l.append(random_string(6))
    return l    

# Generate an array of specified type
# Ask for the size of the array
# If generating an array of integers, ask for an upper bound

def generate_array_from_input(type):
    invalidSize = True
    while invalidSize:
        size = get_integer("Enter the size of array to sort: ")
        if size > 0:
            invalidSize = False
    if type == "int":
        invalidBig = True
        while invalidBig:
            big = get_integer("Enter the integer upper bound for the array: ")
            if size > big:
                print("The upper bound must be greater than or equal",
                      "to the size of the array.")
            else:
                invalidBig = False
        return integer_array(size, big)
    if type == "float":
        return float_array(size)
    if type == "string":
        return string_array(size)
        

# Generate and sort an array and print times for merge sort and built-in sort

def sort_and_time(type):
    # Array for merge sort
    ml = generate_array_from_input(type)
    
    # Make a copy of the other array for the built-in sort
    sl = list(ml)
    
    t0 = time.time()
    mergesort.merge_sort().sort(ml)
    tf = time.time()
    print("Merge sort for", type, "array:", tf-t0)
    
    t0 = time.time()
    sl.sort()
    tf = time.time()
    print("Built-in sort for", type, "array:", tf-t0, "\n")    
    
def small_sort(type):
    size = 10
    if type == "int":
        l = integer_array(size, 100)
    if type == "float":
        l = float_array(size)
    if type == "string":
        l = string_array(size)
    print("SIZE = 10 Sort:")
    print("Unsorted:", l)
    mergesort.merge_sort().sort(l)
    print("Sorted:", l, "\n")


# **********Main Program********** 

# Run the sort/time comparison three times each for arrays
# of integers, real numbers, and strings.

# Three runs of integer sorts

print("\n********************Integer Sorts********************\n")
small_sort("int")
sort_and_time("int")
sort_and_time("int")

# Three runs of real number sorts

print("\n******************Real Number Sorts******************\n")
small_sort("float")
sort_and_time("float")
sort_and_time("float")

# Three runs of string sorts

print("\n********************String Sorts********************\n")
small_sort("string")
sort_and_time("string")
sort_and_time("string")