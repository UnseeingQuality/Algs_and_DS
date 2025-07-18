aval_secs = int(input())
cards_count = 31
seconds_cards = list(map(int, input().split()))

inf = 100*10
aval_secs_cost = [inf] * (aval_secs+1)
aval_secs_cost[0] = 0

mx_card_cnt = (aval_secs // min(second_cards)) + 1

for card_order in range(mx_card_cnt):
    for card_id in range(cards_count):
        for cur_sec in range(aval_secs, -1, -1):
            if (aval_secs_cost[cur_sec] <= inf) and (cur_sec + seconds_cards[card_id] <= aval_secs):
                if aval_secs_cost[cur_sec] + 2**card_id < aval_secs_cost[cur_sec + seconds_cards[card_id]]:
                    aval_secs_cost[cur_sec + seconds_cards[card_id]] = aval_secs_cost[cur_sec] + 2**card_id
