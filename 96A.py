ones = zeros = 0
for c in input():
    if c == '1':
        ones += 1
        zeros = 0
    else:
        ones = 0
        zeros += 1
    if ones >= 7 or zeros >= 7:
        print('YES')
        break
else:
    print('NO')
