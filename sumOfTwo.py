'''
Given two lists of integers, is there a set of numbers — one from each list — whose sum is equal to a specified value
'''

def sumOfTwo(arrayA,arrayB,value):
    band = False
    for a in arrayA:
        diff = value - a
        if diff in arrayB:
            band = True
            return band
    return band
