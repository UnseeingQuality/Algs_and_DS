group_cnt, class_cnt = map(int, input().split())
input_groups = input().split()
groups = sorted([[int(input_groups[i]), i] for i in range(group_cnt)])
comps = [1000000000000] + list(map(int, input().split()))

class_id_per_group = [0]*group_cnt
cnt_no_class = 0

for cur_grp in groups:
    is_find = 0
    for cls_id in range(class_cnt + 1):
       if cur_grp[0] < comps[cls_id] < comps[class_id_per_group[cur_grp[1]]] and (cls_id not in class_id_per_group):
            class_id_per_group[cur_grp[1]] = cls_id
            is_find = 1
    if not is_find:
        cnt_no_class += 1

res = group_cnt - cnt_no_class
print(res)
print(*class_id_per_group)