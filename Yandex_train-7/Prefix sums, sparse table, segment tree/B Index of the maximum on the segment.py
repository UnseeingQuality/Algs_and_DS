def is_overlap(node_l, node_r, interval_l, interval_r):
    return node_l >= interval_l and node_r <= interval_r

def is_crossed(node_l, node_r, interval_l, interval_r):
    return (interval_l <= node_r <= interval_r) or (node_l <= interval_r <= node_r)


nums_cnt = int(input())
arr = list(map(int, input().split()))
reqst_cnt = int(input())

neutral = -1
mn_deg = 0
need_arr_ln = 1

while need_arr_ln < len(arr):
    mn_deg += 1
    need_arr_ln *= 2
arr.extend([neutral] * (need_arr_ln - nums_cnt))
arr = [[arr[idx], idx] for idx in range(need_arr_ln)]

seg_tree = [neutral]*(need_arr_ln - 1) + arr

for node in range(need_arr_ln - 2, -1, -1):
    lson = seg_tree[node * 2 + 1]
    rson = seg_tree[node * 2 + 2]
    if lson[0] == rson[0]:
        seg_tree[node] = lson
    elif lson[0] > rson[0]:
        seg_tree[node] = lson
    else:
        seg_tree[node] = rson


def get_m_and_id(node, start, end, left, right):
    if is_overlap(start, end, left, right):
        return seg_tree[node]
    elif is_crossed(start, end, left, right):
        lson = get_m_and_id(node * 2 + 1, start, (start + end) // 2, left, right)
        rson = get_m_and_id(node * 2 + 2, (start + end) // 2 + 1, end, left, right)
        if lson[0] >= rson[0]:
            return lson
        return rson
    else:
        return [-1, -1]


for _ in range(reqst_cnt):
    left, right = map(int, input().split())
    print(get_m_and_id(0, 0, need_arr_ln - 1, left - 1, right - 1)[1] + 1)