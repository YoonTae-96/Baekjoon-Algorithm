import sys

input = sys.stdin.readline
N, L = map(int, input().split())
point = sorted(list(map(int, input().split())))

tmp = 0
cnt = 0

for i in point:
    if tmp < i:
        cnt += 1
        tmp = i + L - 1

print(cnt)