N = int(input())
S = input().strip()

L = [-1] * (N + 1)
R = [-1] * (N + 1)
head = 0

for i, c in enumerate(S, start=1):
    p = i - 1
    if c == 'L':
        prev = L[p]

        L[i] = prev
        R[i] = p
        L[p] = i
        if prev != -1:
            R[prev] = i
        else:
            head = i
    else:
        nxt = R[p]
        L[i] = p
        R[i] = nxt
        R[p] = i
        if nxt != -1:
            L[nxt] = i

res = []
v = head
while v != -1:
    res.append(v)
    v = R[v]

print(*res)