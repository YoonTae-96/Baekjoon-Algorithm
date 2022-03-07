t = int(input())
count = 0
for _ in range(t):
    BCML = list(input())
    for b in BCML:
        if b == '(':
            count += 1
        elif b == ')':
            count += -1
        if count < 0:
            break
    if count == 0:
        print("YES")
    else:
        print("NO")