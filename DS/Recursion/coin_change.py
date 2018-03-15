def rec_coin(target,coins):
    min_coins = target

    if target in coins:
        return 1
    else:
        for i in [c for c in coins if c <= target]:
            #recursive call (add a coin and subtract from target)
            num_coins = 1 + rec_coin(target-i,coins)

            if num_coins < min_coins:
                min_coins = num_coins

    return min_coins

#print(rec_coin(20,[1,5,10,25]))

def dyn_rec_coin(amt,coins,know_result):

    min_coins = amt

    if amt in coins:
        know_result[amt]=1
        return 1
    elif know_result[amt]>0:
        return know_result[amt]
    else:
        for i in (c for c in coins if c <= amt):
            num_coins = 1 + dyn_rec_coin(amt-i,coins,know_result)

            if num_coins<min_coins:
                min_coins = num_coins

            know_result[amt] = min_coins
    return min_coins

amt = 74
known_result = [0]*(amt+1)
print(dyn_rec_coin(amt,[1,5,10,25],known_result))