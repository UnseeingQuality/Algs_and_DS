n, m = map(int, input().split())

if n > 7:
    x = n - 7
else:
    L = m + 14 - n   # длина месяца
    x = L + (n - 7)

print(x)