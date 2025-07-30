a, b, c, d = map(int, input().split())
m = a*d + c*b
n = b*d
for i in range(2, b*d+1):
    if (m % i == 0) and (n % i == 0):
        m //= i
        n //= i

print(m, n)