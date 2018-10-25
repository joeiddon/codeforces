import re

s = input()
print(''.join('.' + c for c in re.sub('|'.join('aoyeui'), '', s.lower())))
