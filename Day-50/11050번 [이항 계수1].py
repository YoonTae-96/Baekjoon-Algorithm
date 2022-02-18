# 풀이 1
def factorial(x):
    if x > 1:
        return x * factorial(x-1)
    else:
        return 1

num = list(map(int, input().split()))
a = factorial(num[0])
b = factorial(num[1])
c = factorial(num[0]-num[1])
result = a // (b*c)
print(result)

# 풀이 2
import math

num = list(map(int, input().split()))

a = math.factorial(num[0])
b = math.factorial(num[1])
c = math.factorial(num[0]-num[1])
result = a // (b*c)
print(result)