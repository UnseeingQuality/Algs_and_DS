n, k = map(int, input().split()) # n-count_arr_elems, k-count_of_confuse_operations
b = list(map(int, input().split()))

s = sum(b)
mn_b = min(b)
mx_b = max(b)

# seq_sum = sum(s//(n-1)**i for i in range(1,n))
# mn_a = (s//(n-1)**k) - seq_sum - mn_b
# mx_a = (s//(n-1)**k) - seq_sum - mx_b
res = abs(mn_b - mx_b)

print(res)