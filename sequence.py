import math

def sequence(n):
    if 1 <= n <= 9223372036854775807:
        return a(n)
    else:
        return -1


def a(n):
    if n % 2 == 0:
        return 2*b(n)
    else:
        return 1 + 2*b(n)


def b(n):
    n = math.floor(n/2) - math.floor((n+1)/4)
    return n
