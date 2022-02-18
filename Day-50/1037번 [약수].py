case = int(input())
num = list(map(int, input().split()))

num.sort()

result = num[0] * num[case - 1]

print(result)
