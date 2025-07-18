items_cnt, backpack_capacity = map(int, input().split())
weights = list(map(int, input().split()))
costs = list(map(int, input().split()))

res_items = []
aval_costs = [[[-1,-1,-1] for i in range(backpack_capacity+1)] for _ in range(items_cnt)]
aval_costs[0][0] = [0,0,0]

for item_idx in range(items_cnt):
    if item_idx > 0:
        aval_costs[item_idx] = aval_costs[item_idx-1].copy()
    for cur_weight in range(backpack_capacity - weights[item_idx], -1, -1):
        if aval_costs[item_idx][cur_weight][1] > -1:
            if aval_costs[item_idx][cur_weight][1] + costs[item_idx] > aval_costs[item_idx][cur_weight + weights[item_idx]][1]:
                aval_costs[item_idx][cur_weight + weights[item_idx]] = [item_idx, aval_costs[item_idx][cur_weight][1] + costs[item_idx], cur_weight]


res = sorted(aval_costs[-1], key=lambda x: x[1], reverse=True)[0]
res_items.append(res)
cur_res_item = res
while cur_res_item != [0, 0, 0]:
    cur_res_item = aval_costs[cur_res_item[0]-1][cur_res_item[2]]
    if cur_res_item == [0, 0, 0]:
        break
    else:
        res_items.append(cur_res_item)

res_items = sorted(res_items, key=lambda x: x[0])
for item in res_items:
    print(item[0]+1)