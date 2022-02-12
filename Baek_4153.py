while True:
    a = list(map(int, input().split()))
    if sum(a) == 0:
        break
    max_size = max(a)
    a.remove(max(a))
    if a[0]**2 + a[1]**2 == max_size**2:
        print("right")
    else:
        print("wrong")