import sys

team = int(input())
score = list(map(int, sys.stdin.readline().rstrip().split()))

score.sort()
sum_score = 0
max_score = (team * (team - 1)) // 2
count = 0
valid = True
for i in range(team):
    sum_score = sum_score + score[i]
    if sum_score < (i * (i + 1) // 2):
        valid = False

if sum_score != max_score:
    valid = False

if valid:
    print(1)
else:
    print(-1)