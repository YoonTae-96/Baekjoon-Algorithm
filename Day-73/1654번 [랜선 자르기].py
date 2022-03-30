import sys

N, K = map(int, input().split())

wire = [int(sys.stdin.readline()) for _ in range(N)]

start = 1
end = max(wire)

while start <= end:
    mid = (start + end) // 2
    count = 0

    for i in wire:
        count += i // mid
    if count >= K:
        start = mid + 1
    else:
        end = mid - 1
print(end)


