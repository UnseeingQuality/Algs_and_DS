ingot_cnt, backpack = map(int, input().split())
weights = list(map(int, input().split()))
costs = list(map(int, input().split()))

aval_costs = [-1] * (backpack + 1)
aval_costs[0] = 0

for cur_ingot in range(ingot_cnt):
    for cur_weight in range(backpack - weights[cur_ingot], -1, -1):
        if aval_costs[cur_weight] >= 0:
            if aval_costs[cur_weight] + costs[cur_ingot] > aval_costs[cur_weight + weights[cur_ingot]]:
                aval_costs[cur_weight + weights[cur_ingot]] = aval_costs[cur_weight] + costs[cur_ingot]

print(max(aval_costs))