import sys
import math

t = int(input())
n = []
result = []

for i in range(t):
    n.append(int(sys.stdin.readline()))
n.sort()

gcd = n[1] - n[0]
for i in range(1, t):
    gcd = math.gcd(n[i] - n[i-1], gcd)

for i in range(2, int(gcd ** 0.5 + 1)):
    if gcd % i == 0:
        result.append(i)
        result.append(gcd // i)
result.append(gcd)

result = list(set(result))
result.sort()
for i in result:
    print(i, end = ' ')