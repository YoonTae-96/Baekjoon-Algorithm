num1 = input()
num2 = int(input())

result = int(num1[:-2] + '00')

while True:
    if result % num2 == 0:
        break
    result += 1
print(str(result)[-2:])
