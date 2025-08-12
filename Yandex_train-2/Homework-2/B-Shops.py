def find_mx_left_dist(arr):
    dists = [-1 for _ in range(len(arr))]
    mx_dist = -1
    cur_dist = 0
    is_find_home = False
    is_find_shop = False
    for i in range(len(arr)):
        cur = arr[i]
        if cur == 2:
            is_find_shop = True
            cur_dist = 0
        elif cur == 1:
            if is_find_shop:
                cur_dist += 1
                dists[i] = cur_dist
            else:
                dists[i] = len(arr) + 1
        elif cur == 0:
            cur_dist += 1
    return dists


city = list(map(int, input().split()))
l_res = find_mx_left_dist(city)
r_res = find_mx_left_dist(city[::-1])[::-1]
# print(*l_res)
# print(*r_res)

res = [min(l_res[i], r_res[i]) for i in range(len(city))]
print(max(res))