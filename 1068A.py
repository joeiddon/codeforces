import math

no_coin_types, no_friends, ivans_coins, minimum_new_coins = map(int, input().split())

#we need to give him at least his coins plus the minimum new coins coins
min_coins_to_give  = ivans_coins + minimum_new_coins

coins_per_person = min_coins_to_give // no_friends + (1 if min_coins_to_give % no_friends else 0)

#if they're aren't enough coin types, we can't do it
if coins_per_person * no_friends > no_coin_types:
    print(-1)
else:
    print(coins_per_person)
