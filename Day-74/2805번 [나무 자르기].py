import sys

N, M = map(int, input().split())
tree_high = list(map(int, sys.stdin.readline().split()))
tree_high.sort()

start = 1
end = max(tree_high)

while start <= end:
    mid = (start + end) // 2
    result = 0
    for i in range(N):
        if tree_high[i] > mid:
            result += tree_high[i] - mid
    if result >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)
