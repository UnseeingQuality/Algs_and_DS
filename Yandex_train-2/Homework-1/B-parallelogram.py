rqst_cnt = int(input())

for i in range(rqst_cnt):
    coords = list(map(int, input().split()))
    dots = [[coords[j], coords[j+1]] for j in range(0,len(coords)-1,2)]
    dots.sort()

    bottom_len = abs(dots[0][0] - dots[2][0])
    top_len = abs(dots[1][0] - dots[3][0]) # или наоборот
    left_h = dots[1][1] - dots[0][1]
    right_h = dots[3][1] - dots[2][1]
    if top_len != bottom_len or left_h != right_h:
        print("NO")
    else:
        left_angle_sin = left_h / (left_h*2 + (dots[0][0] - dots[1][0])**2)**0.5
        right_angle_sin = right_h / (right_h*2 + (dots[3][0] - dots[2][0])**2)**0.5
        if left_angle_sin != right_angle_sin:
            print("NO")
        else:
            print("YES")