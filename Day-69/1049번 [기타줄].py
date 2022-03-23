import sys

N, M = map(int, input().split())
case = []
for i in range(M):
    case.append(list(map(int, sys.stdin.readline().split())))

case.sort(key=lambda x: x[0])
min_case = min(map(min, case))
bound = (N // 6)
rest = N % 6
result = 0
if case[0][0] < min_case * 6:
    if case[0][0] < rest * min_case :
        result = bound * case[0][0] + case[0][0]
    else:
        result = bound * case[0][0] + rest * min_case

elif case[0][0] > rest * min_case:
    result = N * min_case

print(result)
