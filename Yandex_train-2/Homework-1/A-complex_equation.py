# Решить в целых числах уравнение (a * x + b) / (c * x + d) = 0
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a == 0:
    if b == 0:
        print("INF")
    else:
        print("NO")
else:
    if c != 0:
        sol = -b/a
        if (sol != -d/c) and (sol % 1 == 0):
            print(int(sol))
        else:
            print("NO")
    else:
        sol = -b/a
        if (sol % 1 == 0):
            print(int(sol))
        else:
            print("NO")