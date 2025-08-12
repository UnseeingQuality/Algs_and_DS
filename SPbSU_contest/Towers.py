n = int(input())
cubes = list(map(int, input().split()))
tower_tops = []

def search_right(arr, x):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= x:
            left = mid + 1
        else:
            right = mid
    return left

for cube in cubes:
    idx = search_right(tower_tops, cube)
    if idx < len(tower_tops):
        tower_tops[idx] = cube
    else:
        tower_tops.append(cube)

print(len(tower_tops))


