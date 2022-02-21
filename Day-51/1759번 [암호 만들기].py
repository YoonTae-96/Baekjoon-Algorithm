import sys
from itertools import combinations

L, C = map(int, input().split())
chars = sorted(list(map(str, sys.stdin.readline().rstrip().split())))

possible = list(combinations(chars, L))
vowels = ['a', 'e', 'i', 'o', 'u']

for c in possible:
    consonant_num = vowel_num = 0
    for i in range(L):
        if c[i] in vowels:
            consonant_num += 1
        else:
            vowel_num += 1
    if consonant_num >=1 and vowel_num >= 2:
        print(''.join(c))