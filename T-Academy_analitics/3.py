import math

a, b, c, d = map(int, input().split())
m = a*d + c*b
n = b*d
g = math.gcd(m, n)
m //= g
n //= g
print(m, n)
