def swap(bodies):
    mind_swaper1 = heroes[bodies[0]]
    mind_swaper2 = heroes[bodies[1]]
    heroes[bodies[0]] = mind_swaper2
    heroes[bodies[1]] = mind_swaper1
    swaped_bodies.append(bodies)
    return 0

heroes_cnt, swaps_cnt = list(map(int, input().split()))
swaped_bodies = []
swaped = set()
for i in range(swaps_cnt):
    swap_bodies = list(map(int, input().split()))
    swap_bodies[0] -= 1
    swap_bodies[1] -= 1 # для корректности перестановок в алгоритме
    swaped.add(swap_bodies[0])
    swaped.add(swap_bodies[1])
    swaped_bodies.append(swap_bodies)


swaps = []
heroes = [i for i in range(heroes_cnt)] # число n по индексу k - разум героя n в теле героя k
res = heroes.copy()
swaped = list(swaped)
not_swaped = [heroes[i] for i in range(heroes_cnt) if i not in swaped]

# начальные обмены телами из условия
for idx in range(swaps_cnt):
    swap(swaped_bodies[idx])
# # дебаг
# print(swaped)
# print(not_swaped)
# print(heroes, " Начальный обмен произошел ")
# print("Решение:")

while heroes != res:
    while not_swaped:
        swaped.sort()
        for i in swaped:
            for j in not_swaped:
                swap([i,j])
                print(i+1, j+1) # вывод для решения (обратно правим индексацию)
                swaped.append(j)
                not_swaped.remove(j)
                print(heroes)

    for cur_body in range(heroes_cnt):
        if cur_body != heroes[cur_body]:
            right_body = heroes.index(cur_body)
            if [cur_body, right_body] not in swaped_bodies and [right_body, cur_body] not in swaped_bodies  :
                swap([cur_body, right_body])
                not_swaped.append(cur_body)
                print(cur_body+1, right_body+1) # вывод для решения (обратно правим индексацию)
                print(heroes)

print("Все на местах")