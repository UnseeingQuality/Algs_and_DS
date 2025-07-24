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

# начальные обмены телами из условия
for idx in range(swaps_cnt):
    swap(swaped_bodies[idx])

# Соберем циклы перестановок
used = [False] * heroes_cnt
cycles = [] # циклы (алгебра перестановок) обменов телами
for i in range(heroes_cnt):
    if not used[i] and heroes[i] != i:
        cycle = []
        j = i
        while not used[j]:
            used[j] = True
            cycle.append(j)
            j = heroes[j]
        if len(cycle) > 1:
            cycles.append(cycle)

# дебаг
print(swaped)
print(heroes, " Начальный обмен произошел ")
print("Разбиение перестановки на циклы: ", *cycles)
print("Решение: \n")

buf_1 = heroes_cnt - 2
buf_2 = heroes_cnt - 1
bufs = [buf_1, buf_2]
is_flipped = False

for cycle in cycles:
    first, second = (bufs if not is_flipped else bufs[::-1])

    for body_idx in cycle:
        print([body_idx, first])
        swap([body_idx, first])
        print(heroes)

    if not is_flipped:
        is_flipped = True
        swap([first, second])

    for body_idx in reversed(cycle):
        print([body_idx, second])
        swap([body_idx, second])
        print(heroes)


if heroes == res:
    print("Все на местах")
else:
    print("блять")