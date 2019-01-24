from numpy import random

if __name__ == '__main__':
    ll = int(input("Enter Lower Limit : "))
    ul = int(input("Enter Upper Limit : "))
    print(random.randint(low=ll, high=ul))
