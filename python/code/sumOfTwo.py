'''
Given two lists of integers, is there a set of numbers — one from each list — whose sum is equal to a specified value
'''

def sum_of_two(arrayA,arrayB,value):
    """verify if the difference of A elements minus value is in B"""
    flag = False
    for a in arrayA:
        diff = value - a
        if diff in arrayB:
            flag = True
            return flag
    return flag
