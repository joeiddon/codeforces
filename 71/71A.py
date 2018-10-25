words = [input() for _ in range(int(input()))]
for word in words:
    l = len(word)
    if l > 10:
        print(f'{word[0]}{l-2}{word[-1]}')
    else:
        print(word)
