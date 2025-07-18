nums_cnt = int(input())
arr = list(map(int, input().split()))
reqst_cnt = int(input())
inf = -1
minpow = 0
q = 1
while q < nums_cnt:
    q *= 2
    minpow += 1

arr.extend([inf] * (q - nums_cnt))
arr = [[i, 1] for i in arr]
tree = [inf] * (q - 1) + arr
for node in range(q - 2, -1, -1):
    lson = tree[node * 2 + 1]
    rson = tree[node * 2 + 2]
    if lson[0] == rson[0]:
        tree[node] = [lson[0], lson[1] + rson[1]]
    elif lson[0] > rson[0]:
        tree[node] = lson
    else:
        tree[node] = rson

def get_m_and_c(node, start, end, left, right):
    if start > right or end < left:
        return -1, 0
    elif start >= left and end <= right:
        return tree[node]
    else:
        lson = get_m_and_c(node * 2 + 1, start, (start + end) // 2, left, right)
        rson = get_m_and_c(node * 2 + 2, (start + end) // 2 + 1, end, left, right)
        if lson[0] > rson[0]:
            return lson
        elif lson[0] < rson[0]:
            return rson
        return lson[0], lson[1] + rson[1]


for _ in range(reqst_cnt):
    left, right = map(int, input().split())
    print(*get_m_and_c(0, 0, q - 1, left - 1, right - 1))


