l, k = map(int, input().split())
cubes_idx = list(map(int, input().split()))
res = cubes_idx.copy()

lavka = [i if (i in cubes_idx) else -1 for i in range(l)]
l_part = lavka[:(l//2 + l % 2)]
r_part = lavka[(l//2):]

cubes_left = l//2 + l % 2 - l_part.count(-1)
for i in range(len(l_part)):
    if l_part[i] != -1 and cubes_left > 1:
        res.remove(l_part[i])
        cubes_left -= 1

cubes_right = l//2 + l % 2- r_part.count(-1)
for i in range(len(r_part)-1, -1, -1):
    if r_part[i] != -1 and cubes_right > 1:
        res.remove(r_part[i])
        cubes_right -= 1

print(*res)
