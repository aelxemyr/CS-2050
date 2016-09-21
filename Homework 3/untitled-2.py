import math

def fib(n):
    
    phi = (1 + math.sqrt(5))/2
    psi = 1 - phi
    
    return int((phi**n - psi**n)/(math.sqrt(5)))
    
def modpower(n,k,m):
    
    for i in range(1, k+1):
        n = n*n % m
    
    return n

def threeAndFive():
    return (modpower(3,126,2) + modpower(5,123,2)) % 2