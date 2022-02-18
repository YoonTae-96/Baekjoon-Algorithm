import math

case_num = int(input())

for i in range(case_num):
    bridge = list(map(int, input().split()))
    result1 = math.factorial(bridge[0])
    result2 = math.factorial(bridge[1])
    result3 = math.factorial(bridge[1]-bridge[0])

    ans = result2 // (result1 * result3)
    print(ans)