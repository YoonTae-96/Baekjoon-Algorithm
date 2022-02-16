from itertools import combinations
import sys

N = int(input())
graph = []
num = [i for i in range(N)]

result = sys.maxsize

for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

for c in combinations(num, N//2):
    visited = [False] * N
    team1 = []
    team2 = []

    for i in c:
        visited[i] = True
        team1.append(i)
    for i in range(N//2):
        if not visited[i]:
            team2.append(i)

    sum1 = 0
    sum2 = 0
    for i in range(N//2):
        for j in range(N//2):
            if graph[team1[i]][team1[j]] != 0:
                sum1 = sum1 + graph[team1[i]][team1[j]]
            if graph[team2[i]][team2[j]] != 0:
                sum2 = sum2 + graph[team2[i]][team2[j]]
    if abs(sum1 - sum2) < result:
        result = abs(sum1 - sum2)
print(result)