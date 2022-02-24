import sys

N, K = map(int, input().split())
tall = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
tmp = 0
cost = []
costs = 0
for i in range(1, len(tall)):
    tmp = tall[i] - tall[i-1]
    cost.append(tmp)
cost.sort()
for i in range(N-K):
    costs = costs + cost[i]
print(costs)