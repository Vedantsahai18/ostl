def fact(a):
    if a:
        return n * fact(n - 1)
    else:
        return 1


if __name__ == '__ main__':
    n = int(input("Enter an integer: "))
    print("Factorial(", n, ") = ", fact(n))
