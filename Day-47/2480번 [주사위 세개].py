dice = list(map(int, input().split()))

dice.sort()

result = 0
count = 0

for i in range(2):
    if dice[i] == dice[i + 1]:
        count = count + 1

if count == 2:
    result = 10000 + (1000 * dice[0])
elif count == 1:
    result = 1000 + (100 * dice[1])
else:
    result = dice[2] * 100
print(result)