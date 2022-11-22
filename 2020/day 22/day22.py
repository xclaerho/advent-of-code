from collections import deque
from copy import deepcopy

def combat(deck_1, deck_2) -> (int, deque):
    while len(deck_1) > 0 and len(deck_2) > 0:
        card_1 = deck_1.popleft()
        card_2 = deck_2.popleft()
        if card_1 > card_2:
            deck_1.append(card_1)
            deck_1.append(card_2)
        else:
            deck_2.append(card_2)
            deck_2.append(card_1)
    if len(deck_1) > 0:
        return 1, deck_1
    return 2, deck_2

def recursive_combat(deck_1, deck_2):
    seen = set()
    while len(deck_1) > 0 and len(deck_2) > 0:
        game = (tuple(deck_1), tuple(deck_2))
        if game in seen:
            return 1, deck_1
        seen.add(game)
        card_1, card_2 = deck_1.popleft(), deck_2.popleft()
        winner = 1
        if card_1 <= len(deck_1) and card_2 <= len(deck_2):
            winner, _ = recursive_combat(deque(list(deck_1)[:card_1]), deque(list(deck_2)[:card_2]))
        else:
            if card_2 > card_1:
                winner = 2
        if winner == 1:
            deck_1.append(card_1)
            deck_1.append(card_2)
        else:
            deck_2.append(card_2)
            deck_2.append(card_1)
    if len(deck_1) > 0:
        return 1, deck_1
    return 2, deck_2

def score(deck) -> int:
    score = 0
    for i in range(1, len(deck) + 1):
        score += i * deck.pop()
    return score

deck_1 = deque()
deck_2 = deque()

player_1, player_2 = open('input.txt').read().split('\n\n')
for card in player_1.split('\n')[1:]:
    deck_1.append(int(card))
for card in player_2.split('\n')[1:]:
    deck_2.append(int(card))

_, winning_deck = combat(deepcopy(deck_1), deepcopy(deck_2))
print(score(winning_deck))

_, winning_deck = recursive_combat(deck_1, deck_2)
print(score(winning_deck))