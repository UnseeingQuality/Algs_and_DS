def take_sect_lvl(left, right):
    ln = right - left + 1
    deg = 0

    while 2**deg < ln:
        deg += 1
        if 2**(deg+1) >= ln:
            return deg + 1


def is_crossed(element, interval):
    if (element[2] >= interval[0] and interval[1] >= element[2]) or (interval[1] >= element[1] and element[2] >= interval[1]):
        return True
    return False

def is_overlap(element, interval):
    if interval[0] <= element[1] and interval[1] >= element[2]:
        return True
    return False


def get_max(element,cur_lvl,left, right):
    if is_overlap(element, [left, right]):
        return element
    elif is_crossed(element, [left, right]):
        element_id = seg_tree[cur_lvl].index(element)
        l_son = seg_tree[cur_lvl - 1][element_id*2]
        r_son = seg_tree[cur_lvl - 1][element_id*2 + 1]

        l_son_give = get_max(l_son, cur_lvl - 1, left, right)
        r_son_give = get_max(r_son, cur_lvl - 1, left, right)

        if l_son_give[0] > r_son_give[0]:
            return l_son_give
        elif r_son_give[0] > l_son_give[0]:
            return r_son_give
        else:
            return [r_son_give[0], l_son_give[1], r_son_give[2], r_son_give[3] + l_son_give[3]]
        # return max(get_max(l_son, cur_lvl - 1, left, right), get_max(r_son, cur_lvl - 1, left, right))
    else:
        return [inf,inf,inf,inf] #возвращаем нейтральный


nums_cnt = int(input())
arr = list(map(int, input().split()))
reqst_cnt = int(input())

arr_h = take_sect_lvl(0,len(arr))
inf = -1
while len(arr) < 2**arr_h:
    arr.append(inf)

seg_tree = [[] for i in range(arr_h + 1)]
seg_tree[0] = [[arr[i], i, i, 1] for i in range(2**arr_h)] #элемент, левая и правая граница, и сколько встречался

#print(arr)
for tree_lvl in range(1, arr_h + 1):
    for parent_id in range(len(seg_tree[tree_lvl-1])//2):
        l_son = seg_tree[tree_lvl-1][parent_id*2]
        r_son = seg_tree[tree_lvl-1][parent_id*2+1]
        if l_son[0] > r_son[0]:
            seg_tree[tree_lvl].append([l_son[0], l_son[1], r_son[2], l_son[3]])
        elif r_son[0] > l_son[0]:
            seg_tree[tree_lvl].append([r_son[0], l_son[1], r_son[2], r_son[3]])
        else:
            seg_tree[tree_lvl].append([r_son[0], l_son[1], r_son[2], r_son[3] + l_son[3]])
#    print(seg_tree[tree_lvl])

for _ in range(reqst_cnt):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    cur_mx = get_max(seg_tree[-1][0], arr_h, l, r)
    print(cur_mx[0], cur_mx[3])

