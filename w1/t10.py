from collections import deque

boris_cards = deque(map(int, input().split()))
nursik_cards = deque(map(int, input().split()))
move = 0
while boris_cards and nursik_cards:
    b_top_card = boris_cards.popleft()
    n_top_card = nursik_cards.popleft()
    if b_top_card == 9 and n_top_card == 0:
        b_wins = False
    elif b_top_card == 0 and n_top_card == 9:
        b_wins = True
    elif b_top_card > n_top_card:
        b_wins = True
    else:
        b_wins = False
    move += 1
    if b_wins:
        boris_cards.append(b_top_card)
        boris_cards.append(n_top_card)
    else:
        nursik_cards.append(b_top_card)
        nursik_cards.append(n_top_card)
if bool(boris_cards):
    print("Boris", move)
else:
    print("Nursik", move)
