import sys

def is_overlap(node_l, node_r, interval_l, interval_r):
    return node_l >= interval_l and node_r <= interval_r

def is_crossed(node_l, node_r, interval_l, interval_r):
    return (interval_l <= node_r <= interval_r) or (node_l <= interval_r <= node_r)

def eval_seg_tree(arr):
    seg_tree = [neutral] * (need_arr_ln - 1) + arr

    for node in range(need_arr_ln - 2, -1, -1):
        lson = seg_tree[node * 2 + 1]
        rson = seg_tree[node * 2 + 2]
        if lson == rson:
            seg_tree[node] = lson
        elif lson > rson:
            seg_tree[node] = lson
        else:
            seg_tree[node] = rson

    return seg_tree

def get_max(node, start, end, left, right):
    if is_overlap(start, end, left, right):
        return seg_tree[node]
    elif is_crossed(start, end, left, right):
        lson = get_max(node * 2 + 1, start, (start + end) // 2, left, right)
        rson = get_max(node * 2 + 2, (start + end) // 2 + 1, end, left, right)
        if lson >= rson:
            return lson
        return rson
    else:
        return -1

def change_element(change, idx):
    change_idx = need_arr_ln - 1 + idx_change
    seg_tree[change_idx] = change
    while change_idx >= 0:
        prnt_change_idx = (change_idx - 1) // 2
        lson = seg_tree[prnt_change_idx * 2 + 1]
        rson = seg_tree[prnt_change_idx * 2 + 2]
        seg_tree[prnt_change_idx] = max(lson, rson)
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

neutral = -1
mn_deg = 0
need_arr_ln = 1

while need_arr_ln < len(arr):
    mn_deg += 1
    need_arr_ln *= 2
arr.extend([neutral] * (need_arr_ln - nums_cnt))
arr = [arr[idx] for idx in range(need_arr_ln)]

seg_tree = eval_seg_tree(arr)

for _ in range(rqst_cnt):
    rqst_type = data[ptr]
    ptr += 1
    if rqst_type == 's':
        left = int(data[ptr])
        ptr += 1
        right = int(data[ptr])
        ptr += 1
        mx = get_max(0, 0, need_arr_ln - 1, left - 1, right - 1)
        output.append(f"{mx} ")
    elif rqst_type == 'u':
        idx_change = int(data[ptr])
        idx_change -= 1
        ptr += 1
        change = int(data[ptr])
        ptr += 1
        change_element(change, idx_change)

sys.stdout.write("".join(output))