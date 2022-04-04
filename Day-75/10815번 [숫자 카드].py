import sys

N = int(input())

N_list = list(map(int, sys.stdin.readline().split()))

M = int(input())
M_list = list(map(int, sys.stdin.readline().split()))

N_list.sort()
for i in M_list:
    start = 0
    end = N - 1
    endflag = False
    while start <= end:
        mid = (start + end) // 2
        if N_list[mid] > i:
            end = mid - 1
        elif N_list[mid] < i:
            start = mid + 1
        elif N_list[mid] == i:
                print(1, end = " ")
                endflag = True
                break

    if endflag == False:
        print(0, end = " ")
