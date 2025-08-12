x = str(input())
z = str(input())
y = ""

if len(z) > len(x):
    x *= ((len(z) // len(x)) + 1)

