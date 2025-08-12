def find_mx_left_dist(arr):
    mx_dist = -1
    cur_dist = 0
    is_find_home = False
    for i in range(len(arr)):
        cur = arr[i]
        if cur == 2:
            if is_find_home:
                mx_dist = max(mx_dist, cur_dist)
            cur_dist = 0
        elif cur == 1:
            is_find_home = True
            cur_dist += 1
            mx_dist = max(mx_dist, cur_dist)
        elif cur == 0:
            mx_dist = max(mx_dist, cur_dist)
            cur_dist += 1
            is_find_home = False
    return mx_dist


city = list(map(int, input().split()))
l_res = find_mx_left_dist(city)
r_res = find_mx_left_dist(city[::-1])

res = min(l_res, r_res)
print(res)