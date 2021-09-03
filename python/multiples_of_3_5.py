'''
From projecteuler.net
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''


#list comprehension solution
def solution(n):
    return sum(num for num in range(1,n,1) if num%3==0 or num%5==0)


#solution 1
def solution(n):
    sum = 0
    for i in range(1,n,1):
        if i%3==0 or i%5==0:
            sum = sum + i
    return sum
