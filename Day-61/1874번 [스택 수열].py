t = int(input())
stack = []
result = []
push = '+'
pop = '-'
no_m = True

count = 0

for i in range(t):
    x = int(input())

    while count < x:
        count += 1
        stack.append(count)
        result.append(push)

    if stack[-1] == x:
        stack.pop()
        result.append(pop)
    else:
        no_m = False
        exit(0)

if no_m == False:
    print("NO")
else:
    print("\n".join(result))



