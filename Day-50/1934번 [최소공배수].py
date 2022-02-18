def LCM(x, y):
    result = int((x * y) / GCD(x, y))
    return result


def GCD(x, y):
    while y:
        x, y = y, x % y
    return x


test_num = int(input())
for i in range(test_num):
    num = list(map(int, input().split()))
    GCD(num[0], num[1])
    print(LCM(num[0], num[1]))
