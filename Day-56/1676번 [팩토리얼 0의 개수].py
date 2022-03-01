import math

n = int(input())

fac = math.factorial(n)
count = 0

while fac > 0:
    tmp = fac
    result = tmp % 10
    fac = fac // 10
    if result == 0:
        count += 1
    elif result != 0:
        break
print(count)
