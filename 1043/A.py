n = int(input())
ais = [int(a) for a in input().split()]

min_k = max(ais)
elodreip_votes = sum(ais)
awruk_votes = sum(min_k - a for a in ais)
needed_votes = elodreip_votes - awruk_votes + 1
if needed_votes < 0:
    needed_votes = 0
k = min_k + (needed_votes + n - 1) // n

print(k)
