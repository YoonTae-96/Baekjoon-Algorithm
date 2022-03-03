def two_count(two):
    c_two = 0
    while two != 0:
        two = two // 2
        c_two += two
    return c_two

def five_count(five):
    c_five = 0
    while five != 0:
        five = five // 5
        c_five += five
    return c_five

n, m = map(int, input().split())

print(min(two_count(n) - two_count(m) - two_count(n-m), five_count(n) - five_count(m) - five_count(n-m)))
