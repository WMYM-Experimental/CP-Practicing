#Importing from math

from math import *

def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
    
    
def sum_fib(n):
    total = [factorial(fibo(i)) for i in range(0, n)]
    return sum(total)
    
    
#factorial funtion without importing 

def factorial(k):
    fact = 1
    while k > 1 :
        fact = fact*k
        k = k - 1
        
    return fact


#factorial funtion without importing -- using recursion

def factorial(k):
    if k == 0:
        return 1
    else:
        return k*factorial(k-1)
