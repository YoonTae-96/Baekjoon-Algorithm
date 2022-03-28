import sys

N = int(input())
N_list = set(map(int, sys.stdin.readline().split()))
M = int(input())
M_list = list(map(int, sys.stdin.readline().split()))

for i in M_list:
    if i in N_list:
        print(1)
    else:
        print(0)