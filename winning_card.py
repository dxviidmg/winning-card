def winning_card(cards):
    res = -1
    for player_cards in cards:
        aux = {}
        for card in player_cards:
            if card in aux:
                aux[card] += 1
            else:
                aux[card] = 1
        
        aux = {k: v for k, v in aux.items() if v == 1}
        
        if aux == {}:
            continue
        pos_max = max(aux.keys())
        if pos_max > res:
            res = pos_max
        
    return res

print(winning_card([[5,7,3,9,4,9,8,3,1], [1,2,2,4,4,1], [1,2,3]]))
print(winning_card([[5,5], [2,2]]))