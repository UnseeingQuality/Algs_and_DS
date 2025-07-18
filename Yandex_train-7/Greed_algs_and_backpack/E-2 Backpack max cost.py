ingot_cnt, backpack = map(int, input().split())
weights = list(map(int, input().split()))
costs = list(map(int, input().split()))

res = -1
aval_costs = [-1] * (backpack + 1)
aval_costs[0] = 0

for cur_ingot in range(ingot_cnt):
    cur_aval_costs = aval_costs.copy()
    for cur_weight in range(backpack + 1):
        if (cur_aval_costs[cur_weight] >= 0) and (cur_weight + weights[cur_ingot] <= backpack):
            if cur_aval_costs[cur_weight] + costs[cur_ingot] > aval_costs[cur_weight + weights[cur_ingot]]:
                aval_costs[cur_weight + weights[cur_ingot]] = cur_aval_costs[cur_weight] + costs[cur_ingot]
                if cur_aval_costs[cur_weight] + costs[cur_ingot] >= res:
                    res = cur_aval_costs[cur_weight] + costs[cur_ingot]

print(res)