meeting_num = int(input())

meeting_time = []

last = 0
count = 0

for i in range(meeting_num):
    start, end = map(int, input().split())
    meeting_time.append([start, end])

meeting_time = sorted(meeting_time, key = lambda a:a[0])
meeting_time = sorted(meeting_time, key = lambda a:a[1])

for i, j in meeting_time:
    if i >= last:
        count = count + 1
        j = last
print(count)
