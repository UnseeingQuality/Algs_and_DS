ingot_cnt, backpack = map(int, input().split())
weights = sorted(list(map(int, input().split())))

res = -1
aval_weights = [0] * (backpack + 1)
aval_weights[0] = 1

for cur_ingot in weights:
    cur_aval_weights = aval_weights.copy()
    for cur_weight in range(backpack + 1):
        if (cur_aval_weights[cur_weight] == 1) and (cur_weight + cur_ingot <= backpack):
            aval_weights[cur_weight + cur_ingot] = 1
            if cur_weight + cur_ingot >= res:
                res = cur_weight + cur_ingot

print(res)