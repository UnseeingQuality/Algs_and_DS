# Найти наименьшее натуральное число, не представимое в виде суммы подмножества элементов массива.
# Ограничение: время O(n log n)

n = int(input())
arr = list(map(int, input().split()))
res = 1

arr.sort()

for i in range(n):
    if arr[i] <= res:
        res += arr[i]
    elif arr[i] > res:
        break

print(res)
