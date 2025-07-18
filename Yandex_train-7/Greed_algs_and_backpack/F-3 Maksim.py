n, m = map(int, input().split())
mi = [int(i) for i in input().split()]
ci = [int(i) for i in input().split()]
psbl = [[(0, 0)] + [(-1, -1)] * m]

for mass in range(n):
    for i in range(m - mi[mass], -1, -1):
        if psbl[-1][i] != (-1, -1):
            if psbl[-1][i + mi[mass]][0] <= psbl[-1][i][0] + ci[mass]:
                psbl[-1][i + mi[mass]] = psbl[-1][i][0] + ci[mass], mass
    psbl.append(psbl[-1].copy())
psbl = psbl[:-1]
# search max sum

index_max = 0

for x in range(1, m + 1):
    if psbl[-1][x][0] > psbl[-1][index_max][0]:
        index_max = x

generation = n - 1
result = []
while index_max != 0 and generation >= 0:
    result.append(psbl[generation][index_max][1])
    index_max -= mi[result[-1]]
    generation = result[-1] - 1

for i in sorted(result):
    print(i + 1)
