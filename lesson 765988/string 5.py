alpha = ' abcdefghijklmnopqrstuvwxyz'
s = input().strip()
n = int(input())
res = ''
for c in s:
    res += alpha[(alpha.index(c) + n) % len(alpha)]
print(res)