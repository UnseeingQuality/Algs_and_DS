tests_cnt = int(input())

for _ in range(tests_cnt):
    line_ln = int(input())
    line = list(map(int, input().split()))
    split_cnt = 0
    split_ln = []
    cur_split_ln = 0
    cur_split = [1000000000000]
    cur_split_mn = 100000000000
    line_idx = -1
    while line_idx < line_ln - 1:
        if min(cur_split_mn, line[line_idx+1]) > cur_split_ln:
            cur_split.append(line[line_idx+1])
            cur_split_ln += 1
            if cur_split_mn > line[line_idx+1]:
                cur_split_mn = line[line_idx+1]
        else:
            split_cnt += 1
            split_ln.append(cur_split_ln)
            cur_split = [line[line_idx+1]]
            cur_split_ln = 1
            cur_split_mn = line[line_idx+1]
        line_idx += 1

    split_cnt += 1
    split_ln.append(cur_split_ln)

    print(split_cnt)
    print(*split_ln)
