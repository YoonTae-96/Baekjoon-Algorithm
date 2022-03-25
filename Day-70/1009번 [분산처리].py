import math

N = int(input())

for i in range(N):
    a, b = map(int, input().split())
    num = pow(a, b, 10)
    if not num:
        print(num + 10)
    else:
        print(num)
