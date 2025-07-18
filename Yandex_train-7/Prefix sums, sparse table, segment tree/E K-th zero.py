import sys


def is_overlap(node_l, node_r, interval_l, interval_r):
    return node_l >= interval_l and node_r < interval_r

def is_crossed(node_l, node_r, interval_l, interval_r):
    return (interval_l <= node_r < interval_r) or (node_l < interval_r <= node_r)

def eval_seg_tree(arr):
    seg_tree = [neutral] * (need_arr_ln - 1) + arr

    for node in range(need_arr_ln - 2, -1, -1):
        lson = seg_tree[node * 2 + 1]
        rson = seg_tree[node * 2 + 2]
        if lson[0] == rson[0]:
            seg_tree[node] = [lson[0], lson[1] + rson[1]]
        elif lson[0] > rson[0]:
            seg_tree[node] = rson
        else:
            seg_tree[node] = lson

    return seg_tree

def get_k_zero_pref(node, start, end, k_id):
    if node * 2 + 2 <= 2**(mn_deg+1) - 1:
        lson = seg_tree[node * 2 + 1]
        rson = seg_tree[node * 2 + 2]
        if lson[1] - (k_id + 1) >= 0 and lson[0] == 0:
            return get_k_zero_pref(node * 2 + 1, start, (start + end) // 2, k_id)
        elif rson[0] == 0:
            return get_k_zero_pref(node * 2 + 2, (start + end) // 2 + 1, end, k_id - lson[1])
        else:
            return -1
    else:
        return (node + 1 - (need_arr_ln - 1))


def get_min_and_cnt(node, start, end, left, right):
    if is_overlap(start, end, left, right):
        return seg_tree[node]
    elif is_crossed(start, end, left, right):
        lson = get_min_and_cnt(node * 2 + 1, start, (start + end) // 2, left, right)
        rson = get_min_and_cnt(node * 2 + 2, (start + end) // 2 + 1, end, left, right)
        if lson[0] > rson[0]:
            return rson
        elif lson[0] < rson[0]:
            return lson
        return [lson[0], lson[1] + rson[1]]
    else:
        return [10**5, 0]


def change_element(change, idx):
    change_idx = need_arr_ln - 1 + idx_change
    seg_tree[change_idx] = change
    while change_idx >= 0:
        prnt_change_idx = (change_idx - 1) // 2
        lson = seg_tree[prnt_change_idx * 2 + 1]
        rson = seg_tree[prnt_change_idx * 2 + 2]
        if lson[0] < rson[0]:
            seg_tree[prnt_change_idx] = lson
        elif lson[0] > rson[0]:
            seg_tree[prnt_change_idx] = rson
        else:
            seg_tree[prnt_change_idx] = [lson[0], lson[1] + rson[1]]
        change_idx = prnt_change_idx



output = []
data = sys.stdin.read().split()
ptr = 0

nums_cnt = int(data[ptr])
ptr += 1
arr = list(map(int, data[ptr:ptr + nums_cnt]))
ptr += nums_cnt
rqst_cnt = int(data[ptr])
ptr += 1

neutral = 10**5
mn_deg = 0
need_arr_ln = 1

while need_arr_ln < len(arr):
    mn_deg += 1
    need_arr_ln *= 2
arr.extend([neutral] * (need_arr_ln - nums_cnt))
arr = [[arr[idx], 1] for idx in range(need_arr_ln)]

seg_tree = eval_seg_tree(arr)

for _ in range(rqst_cnt):
    rqst_type = data[ptr]
    ptr += 1
    if rqst_type == 's':
        if seg_tree[0][0] != 0:
            output.append('-1 ')
            ptr += 3
            continue

        left = int(data[ptr])
        ptr += 1
        right = int(data[ptr])
        ptr += 1
        k = int(data[ptr])
        k -= 1 # нуль-нумерация
        ptr += 1
        zero_cnt_bef_seg = get_min_and_cnt(0, 0, need_arr_ln - 1, 0, left - 1)[1]
        res = get_k_zero_pref(0, 0, need_arr_ln - 1, zero_cnt_bef_seg + k)
        if res > right:
            output.append("-1 ")
        else:
            output.append(f"{res} ")
    elif rqst_type == 'u':
        idx_change = int(data[ptr])
        idx_change -= 1
        ptr += 1
        change = [int(data[ptr]), 1]
        ptr += 1
        change_element(change, idx_change)

sys.stdout.write("".join(output))