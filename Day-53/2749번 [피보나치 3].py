n = int(input())

fibo = [0, 1]
M = 1000000
p = 15 * 100000

for i in range(2, p):
    fibo.append(fibo[i-2] + fibo[i-1])
    fibo[i] = fibo[i] % M

print(fibo[n%p])