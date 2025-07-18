group_cnt, class_cnt = map(int, input().split())
input_groups = input().split()
groups = sorted([[int(input_groups[i]), i] for i in range(group_cnt)])
comps = [0] + list(map(int, input().split()))

class_id_per_group = [0]*group_cnt
cnt_no_class = 0



















for grp_id in range(group_cnt):
    for cls_id in range(class_cnt):

        if cls_id == 0:
            if groups[grp_id][0] < comps[cls_id] and (cls_id+1 not in class_id_per_group):
                class_id_per_group[groups[grp_id][1]] = cls_id + 1
        else:
            if groups[grp_id][0] < comps[cls_id] < comps[class_id_per_group[groups[grp_id][1]] - 1] and (cls_id+1 not in class_id_per_group):
                class_id_per_group[groups[grp_id][1]] = cls_id + 1

    if class_id_per_group[grp_id] == 0:
        cnt_no_class += 1


res = group_cnt - cnt_no_class
print(res)
print(*class_id_per_group)
