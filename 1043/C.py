'''
sol:
you can always make the ideal: aaa...bbb.. string,
just need to find the flips to get there
flip in order to group all the a characters
'''

s = input()
o = ''
for i,c in enumerate(s[:-1]):
    #print(f'c: "{c}", s: "{s}", o: {o}')
    if c == 'b':
        if s[i+1] == 'a':
            s = s[:i+1][::-1] + s[i+1:]
            o += '1'
        else:
            o += '0'
    else: #'a'
        if s[i+1] == 'b':
            o += '1'
            s = s[:i+1][::-1] + s[i+1:]
        else:
            o += '0'

#print(f'c: "{c}", s: "{s}", o: {o}')
if s[0] == 'b':
    s = s[::-1]
    #print(f'c: "{c}", s: "{s}", o: {o}')
    o += '1'
else:
    o += '0'

#print(f'c: "{c}", s: "{s}", o: {o}')
print(' '.join(o))
