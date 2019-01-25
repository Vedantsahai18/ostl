def is_armstrong(x):
    return sum([pow(int(d), 3) for d in str(x)]) == x


if __name__ == '__main__':
    ll = int(input("Enter lower limit of search : "))
    ul = int(input("Enter upper limit of search"))
    print(filter(is_armstrong, range(ll, ul)))
