mx = -1000000
mx_cnt = 0

cur_num = -1
while cur_num != 0:
    cur_num = int(input())
    if cur_num > mx:
        mx = cur_num
        mx_cnt = 1
    elif cur_num == mx:
        mx_cnt += 1

print(mx_cnt)