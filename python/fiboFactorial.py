'''
Make a function that returns the sum of the factorial of every number in the fibbonacci sequence from 1 to n

n is an integer
'''


#Importing from math for using factorial built-in function
from math import *

def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
    
    
def sumFibboFActorialsF(n):
    total = [factorial(fibo(i)) for i in range(0, n)]
    return sum(total)
    
    
#factorial funtion without importing 
def factFaster(k):
    fact = 1
    while k > 1 :
        fact = fact*k
        k = k - 1
        
    return fact


#factorial funtion without importing -- using recursion
def factRecursive(k):
    if k == 0:
        return 1
    else:
        return k*factorial(k-1)
