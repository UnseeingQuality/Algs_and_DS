from functools import lru_cache

p = float(input())
n = int(input())

@lru_cache(None)
def f(k):
    if k == 0:
        return 0.0
    if k == 1:
        return 1 - p

    total = 0.0
    for i in range(1, k):
        total += f(i) * f(k - i)
    return p * total

print(f"{f(n):.5f}")