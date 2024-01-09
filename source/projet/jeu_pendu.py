from random import randint

"""
with open('../doc/pendu4.txt',mode='rb') as p:
    p = p.read()
    print(p)
"""

def cacher_mot(m):
    """
    paramètre :
    - m est une chaine de caractère (str), représentant le mot à deviner
    
    la fonction renvoie une chaine de caractères de même longueur que le paramètre m, constituée de la
    première lettre et de la dernière lettre de m séparées par le caractère souligné '_' 
    """
    assert len(m)>2
    return m[0]+'_'*(len(m)-2)+m[-1]

def afficher(mot):
    for lettre in mot:
        print(lettre,end=' ')
    print()
    print()
         
def remplacer_lettre(mot1,mot2,lettre):
    m = mot2[0]
    for i in range(1,len(mot1)-1):
        if lettre == mot1[i]:
            m = m + lettre
        else:
            m = m+ mot2[i]
    m = m + mot2[-1]
    return m

def lettre_dans_mot(mot,lettre):
    for i in range(1,len(mot)-1):
        if mot[i] == lettre:
            return True
    return False
    
    
def reste_a_trouver(mot):
    n = 0
    for lettre in mot:
        if lettre == '_':
            n = n + 1
    return n

def afficher_pendu(n):
    p1 = '\r\n    \r\n    \r\n    \r\n    \r\n___ ___\r\n'
    p2 = '\r\n   |\r\n   |\r\n   |\r\n   |\r\n___|___\r\n'
    p3 = '   _________\r\n   |\r\n   |\r\n   |\r\n   |\r\n___|___\r\n'
    p4 = '   _________\r\n   |       |\r\n   |       o\r\n   |\r\n   |\r\n___|___\r\n'
    p5 = '   _________\r\n   |       |\r\n   |       O\r\n   |      /|\\\r\n   |      / \\\r\n___|___\r\n'
    if n == 1:
        print(p1)
    elif n == 2:
        print(p2)
    elif n == 3:
        print(p3)
    elif n == 4:
        print(p4)
    else:
        print(p5)

def choisir_mot():
    with open('pli07.txt',mode='r') as f:
        n = randint(0,78855)
        for i in range(n):
            mot = f.readline()
    return mot.strip().lower()
    
if __name__ == '__main__':
    # -----------------
    #   Initialisation
    # -----------------
    mot_a_deviner = choisir_mot()
    mot_cache = cacher_mot(mot_a_deviner)
    # r : nombre de lettres encore à trouver
    r = reste_a_trouver(mot_cache)
    # n : nombre d'erreurs ; si n = 5, le joueur a perdu
    n = 0
    # afficher le mot caché avant le début du jeu
    afficher(mot_cache)
    # -----------------
    #   Boucle de jeu
    # -----------------
    while n < 5 and r > 0:
        lettre = input('Proposer une lettre : ')
        if lettre_dans_mot(mot_a_deviner,lettre):
            mot_cache = remplacer_lettre(mot_a_deviner,mot_cache,lettre)
            r = reste_a_trouver(mot_cache)
            print("C'est bien, continue:")
            afficher(mot_cache)
        else:
            n = n + 1
            r = reste_a_trouver(mot_cache)
            print('Erreur ! Il reste',r,'lettres à trouver.')
            afficher_pendu(n)
            afficher(mot_cache)

    # -----------------
    #    Conclusion 
    # -----------------    
    if r == 0:
        print('Vous avez gagné')
    else:
        print('Vous avez perdu')
    print('le mot à deviner était',mot_a_deviner)
    