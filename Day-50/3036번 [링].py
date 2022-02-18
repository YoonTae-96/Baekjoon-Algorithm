def GCD(x, y):
    while y:
        x, y = y, x % y
    return x


case_num = int(input())
r = list(map(int, input().split()))

for i in range(1, case_num):
    c = GCD(r[0], r[i])
    result1 = r[0] // c
    result2 = r[i] // c
    print(str(result1) + '/' + str(result2))
