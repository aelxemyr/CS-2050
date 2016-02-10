# Bennett Alex Myers
# CS 2050 - Homework 2
# 10 Feburary 2016

import random
import string
import time
import mergesort

main = "__main__" == __name__

class ui:
    
    # Ask the user for an integer value
    def get_integer(self, prompt):
        while True:
            try:
                n = int(input(prompt))
                break
            except ValueError:
                print("The previous value was not valid.")
        return n
    
    # Ask the user for a floating point value
    def get_float(self, prompt):
        while True:
            try:
                n = float(input(prompt))
                break
            except ValueError:
                print("The previous value was not valid.")
        return n
    
class arrayGenerator:
    
    def __init__(self):
        
        # Create a new ui object for user input
        self.ui = ui()
    
    # Generate an array of random integers
    def integer_array(self, size, big):
        return random.sample(range(big), size)
        
    # Generate an array of random real numbers
    def float_array(self, size):
        l = []
        for i in range(size):
            l.append(random.uniform(0.0, 1.0))
        return l    
    
    # Generate a random string composed of uppercase letters, lowercase letters,
    # and numbers
    def random_string(self, size):
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
        return "".join(random.choice(chars) for i in range(size))
    
    # Generate an array of random strings
    def string_array(self, size):
        l = []
        for i in range(size):
            l.append(self.random_string(6))
        return l    
    
    # Generate an array of specified type
    # Ask for the size of the array
    # If generating an array of integers, ask for an upper bound
    def generate_array_from_input(self, type):
        invalidSize = True
        while invalidSize:
            size = self.ui.get_integer("Enter the size of array to sort: ")
            if size >= 0:
                invalidSize = False
        if type == "Integer":
            invalidBig = True
            while invalidBig:
                big = self.ui.get_integer("Enter the upper bound for the array: ")
                if size > big:
                    print("The upper bound must be greater than or equal",
                          "to the size of the array.")
                else:
                    invalidBig = False
            return self.integer_array(size, big)
        if type == "Real Number":
            return self.float_array(size)
        if type == "String":
            return self.string_array(size)    

class sortTimer:
    
    # Create new arrayGenerator and merge_sort objects
    def __init__(self):
        self.arrayGenerator = arrayGenerator()
        self.sorter = mergesort.merge_sort()
    
    # Generate and sort an array and print times for merge sort and built-in sort
    def sort_and_time(self, type):
        
        # Array for merge sort
        ml = self.arrayGenerator.generate_array_from_input(type)
        
        # Make a copy of the array for the built-in sort
        sl = list(ml)
        
        t0 = time.time()
        self.sorter.sort(ml)
        tf = time.time()
        print("Merge sort for", type, "array:", tf-t0)
        
        t0 = time.time()
        sl.sort()
        tf = time.time()
        print("Built-in sort for", type, "array:", tf-t0, "\n")   
        
    # Tests
    # Note: unit tests for the sorting program are in mergesort.py
    # The following comply with items 4 and 5 in the requirements
    
    def test_one(self, type):
        size = 10
        big = 100
        if type == "Integer":
            l = self.arrayGenerator.integer_array(size, big)
        if type == "Real Number":
            l = self.arrayGenerator.float_array(size)
        if type == "String":
            l = self.arrayGenerator.string_array(size)
        print("SIZE = 10 Sort:")
        print("Unsorted:", l)
        self.sorter.sort(l)
        print("Sorted:", l)
        
    def test_two(self, size, big, type):
        if type == "Integer":
            l = self.arrayGenerator.integer_array(size, big)
        if type == "Real Number":
            l = self.arrayGenerator.float_array(size)
        if type == "String":
            l = self.arrayGenerator.string_array(size)
        t0 = time.time()
        self.sorter.sort(l)
        tf = time.time()
        print(type, "Sort,", "SIZE =", size, ": ", tf - t0)
    
if main:
    
    # **********Main Program********** 
    
    # Create a sortTimer object.
    sortTimer = sortTimer()
    
    # List of data types to sort
    typeList = ["Integer", "Real Number", "String"]
    
    # Run the sort/time comparison three times each for arrays
    # of integers, real numbers, and strings.    
    for type in typeList:
        print("\n******************", type, "Sorts ******************\n")
        for i in range(3):
            sortTimer.sort_and_time(type)


# Tests that were run to comply with items 4 and 5 in the assignment reqs:

# Integer sort tests
# sortTimer().test_one("Integer")
# sortTimer().test_two(10000, 99999, "Integer")
# sortTimer().test_two(100000, 999999, "Integer")

# Real number sort tests
# sortTimer().test_one("Real Number")
# sortTimer().test_two(10000, 99999, "Real Number")
# sortTimer().test_two(100000, 999999, "Real Number")

# String sort tests
# sortTimer().test_one("String")
# sortTimer().test_two(10000, 99999, "String")
# sortTimer().test_two(100000, 999999, "String")