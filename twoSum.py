'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

def twoSum(array,value):
    band = False
    for i in array:
        diff = value - i
        if diff in array:
            band = True
            return band
    return band
