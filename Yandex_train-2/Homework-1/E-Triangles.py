p = int(input())
half_p = p/2
s_min = 10**10
res_1 = [0,0,0]
s_max = -1
res_2 = [0,0,0]

sup_1 = p//2 - (p+1) % 2
inf_2 = (p//2 + 1)
for side_1 in range(1, sup_1 + 1):
    for side_2 in range(inf_2-side_1, p//2 + p % 2):
        side_3 = p - side_1 - side_2
        s = (half_p * (half_p - side_1) * (half_p - side_2) * (half_p - side_3))**0.5
        if s < s_min:
            s_min = s
            res_2 = [side_1, side_2, side_3]
        if s > s_max:
            s_max = s
            res_1 = [side_1, side_2, side_3]

if res_2 == [0,0,0]:
    print(-1)
else:
    print(*res_1)

    print(*res_2)
