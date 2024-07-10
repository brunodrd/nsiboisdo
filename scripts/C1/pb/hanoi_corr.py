def hanoi(n, start, inter, stop):
    if n == 0:
        return None
    else:
        hanoi(n-1, start, stop, inter)
        print(start, "-->", stop)
        hanoi(n-1, inter, start, stop)