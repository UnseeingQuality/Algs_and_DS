N = int(input())
S = str(input())
A = [0]

prev_id = 0
for i in range(1,N+1):
    operation = S[i-1]
    if operation == "R":
        paste_id = prev_id + 1
        if paste_id > len(A):
            A.append(i)
        else:
            A.append(-1)
            for j in range(len(A)-1, paste_id+1, -1):
                A[j] = A[j-1]
                A[j-1] = -1
            A[paste_id+1] = i

    elif operation == "L":
        paste_id = prev_id - 1
        if paste_id < 0:
            A.append(-1)
            for j in range(len(A)-1, paste_id+1, -1):
                A[j] = A[j-1]
                A[j-1] = -1
            A[0] = i
        else:
            A.append(-1)
            for j in range(len(A)-1, paste_id+1, -1):
                A[j] = A[j - 1]
                A[j - 1] = -1
            A[paste_id] = i
    prev_id = paste_id

print(A)