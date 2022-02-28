import math

N, K = list(map(int, input().split()))

a = math.factorial(N)
b = math.factorial(K)
c = math.factorial(N-K)

result = a // (b * c)

print(result % 1000000007)