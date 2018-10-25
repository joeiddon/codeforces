n = int(input())
possible = False
for i in range(1, int(n/2)+1):
    if possible: break
    for j in range(i, int(n/2)+1):
        if i + j == n/2:
            print('YES')
            possible = True
if not possible:
    print('NO')
