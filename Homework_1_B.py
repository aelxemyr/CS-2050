# Homework 1 part B
# Questions 2-5, 6, and 13 from chapter 1 of Lee & Hubbard

# 2.
# What code would you write to create a string containing the words 
# 'Happy Birthday!'? Write some code to point a reference called 'text'
# at that newly created object.

text = "Happy Birthday!"

# 3.
# What code woul dyou write to take the string you created in the last
# question and split it into a list containing two strings? Point the 
# reference 'lst' at this newly created list.

lst = text.split(" ")

# 4.
# What code would you write to upper-ase the string created in the
# second question. Point the reference named 'bDayWish' at this upper-
# cased string.

bDayWish = text.upper()

# 5.
# If you were to execute the code you write for answering the last 
# three questions, what would the string referenced by 'text' contain
# after executing these three lines of code?

# text will contain the string "Happy Birthday!"

# 6.
# How would you create a dictionary that maps "Kent" to "Denise" and
# maps "Steve" to "Lindy"? In these two cases "Kent" and "Steve" are
# the keys and "Denise" and "Lindy" are the values.

newDict = {"Kent": "Denise", "Steve": "Lindy"}

# 13.
# What would you write so that a program asks the user to enter an
# integer and then adds up all the even integers from 2 to the integer
# entered by the user?

n = int(input("Enter an integer: "))
sum = 0
for k in range(2, n, 2):
    sum += k
print(sum)