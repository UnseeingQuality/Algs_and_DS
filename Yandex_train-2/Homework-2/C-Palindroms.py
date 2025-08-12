string = str(input())
repair_cnt = 0
ln = len(string)

l_part = string[:(ln//2 + ln % 2)]
r_part = string[(ln//2)::]
r_part = r_part[::-1]

for i in range(ln//2 + ln % 2):
    if l_part[i] != r_part[i]:
        repair_cnt += 1

print(repair_cnt)