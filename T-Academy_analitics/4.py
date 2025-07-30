N = int(input())
S = str(input())
A = [-1 for i in range(N+1)]
idxs = [-1 for i in range(N+1)] # индекс - число в массиве, значение - его индекс в массиве

idxs[0] = 0
for i in range(N):
    opr = S[i]
    num = i+1
    if opr == "L":
        idxs[num] = idxs[num-1]
        for j in range(num):
            idxs[j] += 1
    if opr == "R":
        idxs[num] = idxs[num-1]
        for j in range(num):
            idxs[j] -= 1

for i in range(N+1):
    A[idxs[i]] = i

print(*A)