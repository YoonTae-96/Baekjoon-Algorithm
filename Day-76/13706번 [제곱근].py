N = int(input())

start = 0
end = N

while start <= end:
    mid = (start + end) // 2
    if mid * mid > N:
        end = mid - 1
    else:
        start = mid + 1
print(end)