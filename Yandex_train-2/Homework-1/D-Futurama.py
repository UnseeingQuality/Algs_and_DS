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
cycles = [] # циклы (алгебра перестановок) обменов телами

for i in range(swaps_cnt):
    swap_bodies = list(map(int, input().split()))
    swap_bodies[0] -= 1
    swap_bodies[1] -= 1 # для корректности перестановок в алгоритме

    if cycles == []:
        cycles.append(swap_bodies)
    else:
        for cycle_id in range(len(cycles)):
            if cycles[cycle_id][-1] == swap_bodies[0] and cycles[cycle_id][0] != swap_bodies[1]:
                cycles[cycle_id].append(swap_bodies[1])
            elif cycles[cycle_id][-1] == swap_bodies[1] and cycles[cycle_id][0] != swap_bodies[0]:
                cycles[cycle_id].append(swap_bodies[0])

    swaped.add(swap_bodies[0])
    swaped.add(swap_bodies[1])
    swaped_bodies.append(swap_bodies)

# # Тут добавляются циклы длины = 1
# for hero in range(heroes_cnt):
#     if not any(hero in cycle for cycle in cycles):
#         cycles.append([hero])

# print("Начальная разбивка на циклы (кроме циклов длины 1): ", cycles)

swaps = []
heroes = [i for i in range(heroes_cnt)] # число n по индексу k - разум героя n в теле героя k
res = heroes.copy()
swaped = list(swaped)
buffer_bodies = [i for i in range(heroes_cnt) if heroes[i] not in swaped] # два последних тела гарантированно не менялись

# начальные обмены телами из условия
for idx in range(swaps_cnt):
    swap(swaped_bodies[idx])

# дебаг
print(swaped)
print(buffer_bodies)
print(heroes, " Начальный обмен произошел ")
print("Решение:")

buf_ch_cnt = 0

for cycle in cycles:
    cycle_len = len(cycle)
    while cycle:
        cur_mind = cycle[0]
        cur_buff = buffer_bodies[0]
        buf_ch_cnt += 1
        if buf_ch_cnt >= cycle_len:
            buf_ch_cnt = 0
            cur_buff = buffer_bodies[1]
        cycle.pop(0)
        if cur_mind == heroes.index(cur_mind) or heroes.index(cur_mind) == cur_buff:
            continue
        else:
            print([heroes.index(cur_mind), cur_buff])
            swap([heroes.index(cur_mind), cur_buff])
            print(heroes)
            if cur_mind == cur_buff or len(cycle) == 1:
                continue
            else:
                print([cur_buff, cur_mind])
                swap([cur_buff, cur_mind])
                print(heroes)


if heroes == res:
    print("Все на местах")
else:
    print("блять")