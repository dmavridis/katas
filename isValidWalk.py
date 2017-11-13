def isValidWalk(walk):
    x ,y = 0, 0
    for d in walk:
        x = x + int(d=='e') - int(d == 'w')
        y = y + int(d=='n') - int(d == 's')
    return x == 0 and y == 0 and len(walk) == 0

# return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')
walk = ['s','e','w','n', 'e']