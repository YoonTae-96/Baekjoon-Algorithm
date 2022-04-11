N, M = map(int, input().split())
arr_A = []
test = []

for i in range(N):
    arr_A.append(int(input()))

for j in range(M):
    test.append(int(input()))

arr_A.sort()

for i in test:
    target = i
    start = 0
    end = N-1
    result = 0
    while start <= end:
        mid = (start + end) // 2
        if arr_A[mid] > target:
            end = mid - 1
        elif arr_A[mid] < target:
            start = mid + 1
        elif arr_A[mid] == target:
            if end == mid:
                break
            end = mid
    if arr_A[mid] == target:
        print(mid)
    else:
        print(-1)