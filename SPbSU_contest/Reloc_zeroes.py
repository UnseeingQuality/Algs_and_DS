arr = list(map(int, input().split()))
buf = -1
lst_zero_idx = None
print(arr)

for i in range(len(arr)-1,-1,-1):
    if arr[i] == 0:
        if lst_zero_idx is None:
            lst_zero_idx = len(arr) -1
        buf = arr[lst_zero_idx]
        arr[lst_zero_idx] = arr[i]
        arr[i] = buf
        lst_zero_idx -= 1

print(arr)