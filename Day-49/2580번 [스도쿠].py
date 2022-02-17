import sys

graph = []
blank = []

for i in range(9):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            blank.append((i,j))

def checkRow(x,a):
    for i in range(9):
        if a == graph[x][i]:
            return False
    return True

def checkCol(a,y):
    for i in range(9):
        if a == graph[i][y]:
            return False
    return True

def checkBox(x,y,a):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if a == graph[nx + i][ny + j]:
                return False
    return True

def DFS(idx):
    if idx == len(blank):
        for i in range(9):
            print(*graph[i])
        exit(0)

    for i in range(1, 10):
        x = blank[idx][0]
        y = blank[idx][1]

        if checkRow(x, i) and checkCol(i, y) and checkBox(x, y, i):
            graph[x][y] = i
            DFS(idx + 1)
            graph[x][y] = 0
DFS(0)