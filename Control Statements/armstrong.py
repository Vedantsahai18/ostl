if __name__ == '__main__':
    a = int(input("Enter a number : "))
    if sum([pow(int(d), 3) for d in str(a)]) == a:
        print(a, " is an armstrong number")
    else:
        print(a, " is not an armstrong number")
