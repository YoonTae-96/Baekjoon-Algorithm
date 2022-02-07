n, m = list(map(int, input().split()))

s = []


def DFS():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(1, n + 1):
        s.append(i)
        DFS()
        s.pop()


DFS()
