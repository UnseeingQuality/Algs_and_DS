n = int(input())
arr = list(map(int, input().split()))

arr.sort()

res = sum(arr[:n-1])
print(res)
