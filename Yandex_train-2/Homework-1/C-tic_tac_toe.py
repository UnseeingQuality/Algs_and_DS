def is_win(board,sig):
    if any([sig]*3 == board[i:i+3] for i in range(0,len(board),3)):
        return True
    elif [sig]*3 == board[::4] or [sig]*3 == board[2:7:2]:
        return True
    elif any([sig]*3 == board[i::3] for i in range(0,3)):
        return True
    else:
        return False


field = []
free = 0
cross = 0
zeros = 0

for i in range(3):
    a,b,c = list(map(int, input().split()))
    row = [a,b,c]
    field.append(a)
    field.append(b)
    field.append(c)
    free += row.count(0)
    cross += row.count(1)
    zeros += row.count(2)

if (not is_win(field,1)) and (not is_win(field,2)):
    if free == 0 and cross != zeros + 1:
        print("NO")
    elif free % 2 == 1 and cross != zeros:
        print("NO")
    elif free % 2 == 0 and cross != zeros + 1:
        print("NO")
    elif free == 9:
        print("YES")
    else:
        print("YES")
elif is_win(field,1) and is_win(field,2):
    print("NO")
elif is_win(field,1):
    if free % 2 == 0 and cross == zeros+1:
        print("YES")
    else:
        print("NO")
elif is_win(field,2):
    if free % 2 == 1 and cross == zeros:
        print("YES")
    else:
        print("NO")