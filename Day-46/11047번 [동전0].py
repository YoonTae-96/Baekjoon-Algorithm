coin_num, money = list(map(int, input().split()))
rest = []
count = 0

for i in range(coin_num):
    rest_case = int(input())
    rest.append(rest_case)

rest.sort(reverse=True)

for i in rest:
    count = count + money // i
    money = money % i
print(count)
