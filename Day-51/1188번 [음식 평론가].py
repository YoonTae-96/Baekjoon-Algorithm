s, p = map(int, input().split())

def gcd(a,b):
    while b:
        a, b = (b, a%b)
    return a
print(p - gcd(s,p))