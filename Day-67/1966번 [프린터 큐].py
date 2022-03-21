import sys

t = int(input())

for i in range(t):
    N, M = map(int, input().split())
    important = list(map(int, sys.stdin.readline().split()))
    queue = []
    for _ in range(N):
        queue.append(0)
    queue[M] = 1
    count = 0
    while True:
        if important[0] == max(important):
            count += 1

            if queue[0] != 1:
                del queue[0]
                del important[0]
            else:
                print(count)
                break

        else:
            important.append(important[0])
            queue.append(queue[0])
            del important[0]
            del queue[0]

