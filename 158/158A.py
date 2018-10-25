n,k = map(int, input().split())
scores = [int(s) for s in input().split()]
assert len(scores) == n

n = 0
for s in scores:
    if s == 0 or s < scores[k-1]:
        break
    n += 1

print(n)
