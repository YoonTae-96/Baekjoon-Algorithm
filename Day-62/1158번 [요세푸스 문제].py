N, K = map(int, input().split())

josephus = []
result = []
count = 0

for i in range(N):
    josephus.append(i + 1)

while len(josephus):
    count += K - 1
    if count >= len(josephus):
        count = count % len(josephus)

    result.append(str(josephus.pop(count)))

print("<", ", ".join(result), ">", sep="")
