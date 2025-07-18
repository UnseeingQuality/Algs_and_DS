aval_secs = int(input())
cards = list(map(int, input().split()))
cards_cnt = 31

for card_idx in range(1, cards_cnt):
    cards[card_idx] = max(cards[card_idx], cards[card_idx - 1] * 2)

cur_cost = 0
res = 10**10

for card_idx in range(cards_cnt-1, -1, -1):
    if aval_secs <= cards[card_idx]:
        res = min(res, cur_cost + 2**card_idx)
    else:
        cur_cost += 2**card_idx
        aval_secs -= cards[card_idx]

if aval_secs == 0:
    res = min(cur_cost, res)

print(res)
