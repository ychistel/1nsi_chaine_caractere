# exercice 2

def occurence(chaine):
    n = 0
    for c in chaine:
        if c == 'a':
            n = n + 1
    return n

r = occurence('abracadabra')