ingot_cnt, backpack_capacity = map(int, input().split())
weights = sorted(list(map(int, input().split())))

avaliable_weig_on_each_step = [[0 for i in range(backpack_capacity+1)] for _ in range(ingot_cnt + 1)]
avaliable_weig_on_each_step[0][0] = 1
res = -1000

for ingot_id in range(ingot_cnt):
    for aval_weig in range(backpack_capacity+1):
        if ingot_id > 0 and avaliable_weig_on_each_step[ingot_id-1][aval_weig] > 0:
            avaliable_weig_on_each_step[ingot_id][aval_weig] = avaliable_weig_on_each_step[ingot_id-1][aval_weig]
        if (avaliable_weig_on_each_step[ingot_id][aval_weig] == 1) and (aval_weig + weights[ingot_id] <= backpack_capacity):
            avaliable_weig_on_each_step[ingot_id+1][aval_weig + weights[ingot_id]] = 1
            if aval_weig + weights[ingot_id] >= res:
                res = aval_weig + weights[ingot_id]

print(res)