import sys

n = int(input())
words = [list(sys.stdin.readline().split()) for i in range(n)]

for i in range(n):
    for j in words[i]:
        print(''.join(reversed(list(j))), end=" ")

    print()