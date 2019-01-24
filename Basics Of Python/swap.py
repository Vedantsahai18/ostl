def swap(p, q):
    return q, p


if __name__ == '__main__':
    print("Enter 2 values : ")
    a = str(input()).split(" ")
    if len(a) == 2:
        swap(a[0], a[1])
    else:
        print("Error : Wrong number of arguments")
