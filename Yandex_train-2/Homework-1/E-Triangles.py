p = int(input())

if p == 4 or p < 3:
    print(-1)
else:
    if p % 3 == 2:
        mns1 = 2 - (p % 2)
        mns2 = mns3 = (p - mns1) // 2

        mxs1 = mxs2 = mxs3 = p // 3
        mxs2 += 1
        mxs3 += 1

    if p % 3 == 1:
        mns1 = 2 - (p % 2)
        mns2 = mns3 = (p - mns1) // 2

        mxs1 = mxs2 = mxs3 = p // 3
        mxs1 += 1

    if p % 3 == 0:
        mns1 = 2 - (p % 2)
        mns2 = mns3 = (p - mns1) // 2

        mxs1 = mxs2 = mxs3 = p // 3

    print(mxs1, mxs2, mxs3)
    print(mns1, mns2, mns3)