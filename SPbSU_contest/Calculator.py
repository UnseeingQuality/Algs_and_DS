exp = str(input())
levels = [[] for i in range(11)]

ln = len(exp)
mx_lvls = 0
scobs_pairs = 0
is_find_scobes = False

for i in range(ln):
    if exp[i] == '(':
        scobs_pairs += 1
        if is_find_scobes == False:
            is_find_scobes = True
            cur_exp = ""
    elif exp[i] == ")":
        scobs_pairs -= 1
    mx_lvls = max(mx_lvls, scobs_pairs)

    if is_find_scobes == True and (exp[i] not in "()" or (scobs_pairs > 0 and cur_exp != "")):
        cur_exp += exp[i]

    if scobs_pairs == 0 and is_find_scobes == True:
        levels[0] = cur_exp
    elif scobs_pairs == 0 and is_find_scobes == False:
        levels[0] = exp


for i in range(mx_lvls):
    scobs_pairs = 0
    is_find_scobes = False

    for i in range(ln):
        if exp[i] == '(':
            scobs_pairs += 1
            if is_find_scobes == False:
                is_find_scobes = True
                cur_exp = ""
        elif exp[i] == ")":
            scobs_pairs -= 1

        if is_find_scobes == True and (exp[i] not in "()" or (scobs_pairs > 0 and cur_exp != "")) :
            cur_exp += exp[i]

        if scobs_pairs == 0 and is_find_scobes == True:
            levels[i+1] = cur_exp
