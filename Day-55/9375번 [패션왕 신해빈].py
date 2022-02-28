from collections import Counter

n = int(input())

for i in range(n):
    cloth_num = int(input())
    s = []
    for j in range(cloth_num):
        a, b = input().split()
        s.append(b)
    wear_counter = Counter(s)
    cnt = 1
    for k in wear_counter:
        cnt *= wear_counter[k] + 1

    print(cnt - 1)