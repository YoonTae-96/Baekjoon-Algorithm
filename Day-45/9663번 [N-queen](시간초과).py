n = int(input())

count = 0
arr = [0] * n

def is_promising(x):
    for i in range(x):
        if arr[i] == arr[x] or abs(arr[i] - arr[x]) == abs(i - x):
            return False

    return True



def N_queen(x):
    global count
    if x == n:
        count = count + 1

    else:
        for i in range(n):
            arr[x] = i

            if is_promising(x):
               N_queen(x + 1)

N_queen(0)
print(count)