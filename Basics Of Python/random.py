from numpy import random


def rand(a, b):
    return random.randint(a, b)


if '__name__' == '__main__':
    ll = int(input("Enter Lower Limit : "))
    ul = int(input("Enter Upper Limit : "))
    print(rand(ll, ul))
