import time

def sumItUp(n):
    sum = 0
    for k in range (n+1):
        sum += k    
    return sum

def fastSum(n):
    sum = int(n*(n+1)/2)
    return sum

def promptUser():
    noValidInput = True
    while noValidInput:
        while True:
            try:
                n = int(input("Please enter a positive integer value: "))
                break
            except ValueError:
                print("The previous input was invalid.")
        if n <= 0 or n > 1000000000:
            print("The previous input was invalid.")
        else:
            noValidInput = False
    return n

# prompt the user for an integer
n = promptUser()

# time for the iterative version
t0 = time.time()
x = sumItUp(n)
t1 = time.time()
print ("Iterative timer: sum = ", x, " n = ", n, " time = ", t1-t0)

# time for the fast version
t0 = time.time()
x = fastSum(n)
t1 = time.time()
print ("Functional timer: sum = ", x, " n = ", n, " time = ", t1-t0)
