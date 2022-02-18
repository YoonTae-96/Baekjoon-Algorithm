while (1):
    num = list(map(int, input().split()))
    if num[0] == int(0) and num[1] == int(0):
        break

    if num[1] % num[0] == 0:
        print("factor")

    elif num[0] % num[1] == 0:
        print("multiple")
    else:
        print("neither")
