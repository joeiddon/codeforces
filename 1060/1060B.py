'''
method:
always use nines for `a`, and then
match with corresponding digit for `b`
 - special case last digit as can't carry

e.g.
199
 14
---
203

'''
n = input()
carry = 0
output = 0
#reverse iterate from last to second digit
for d in map(int, n[:0:-1]):
    if d == 9 and carry == 0:
        output += 9
        carry  = 0
    else:
        output += 9 + d + 1 - carry
        carry = 1
output += int(n[0]) - carry
print(output)
