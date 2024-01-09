.. 1NSI

Jeu du pendu
============

Présentation
------------

Bien que tout le monde connaisse le jeu du pendu, on en rappelle succinctement la règle. Le jeu du pendu consiste
à deviner un mot caché en énumérant des lettres. A chaque erreur, une potence se construit.
Lorsque la potence est construite avec un pendu avant que le mot soit découvert, le joueur a perdu.

On donne l'exemple d'une partie:

.. literalinclude:: exemple.txt

Fonctions utiles
----------------

Nous verrons plus loin le programme principal qui s'occupe du déroulement du jeu selon la règle. Pour le rendre plus
lisible et facile à écrire, nous nous appuyons sur des fonctions qui réalisent des tâches simples appelées par le
programme principal.

.. rubric:: Cacher un mot

La fonction ``cacher_mot`` prend en paramètre un mot ``m`` et renvoie ce mot en remplaçant chacune de ses lettres par des
caractères soulignés ``_`` sauf la première et la dernière lettre. La chaine de caratères renvoyée par la fonction a la
même longueur que le mot passé en argument lors de l'appel.

On donne des exemples d'appels de cette fonction:

>>> cacher_mot('pendu')
p___u

>>> cacher_mot('bonjour')
b_____r


.. rubric:: Afficher un mot

On peut remarquer que l'affichage du mot caché ne laisse pas apparaître clairement les différents caractères soulignés
``_``. Pour cette raison, on va créer une fonction d'affichage en insérant des espaces entre chaque caractère du mot
passé en argument.

La fonction ``afficher`` prend en paramètre un mot ``m`` et affiche celui-ci en insérant des espaces entre chaque
caractère. La fonction ne renvoie rien.

On donne des exemples d'appels de cette fonction:

>>> afficher('pendu')
p e n d u

>>> cacher_mot('b_____r')
b _ _ _ _ _ r


.. rubric:: Lettre découverte

Lorsqu'on propose une lettre correcte, il faut remplacer le souligné par cette lettre dans le mot caché. La fonction
``remplacer_lettre(mot1,mot2,lettre)`` a trois paramètres:

- mot1 est une chaine de caractères associée au mot à deviner;
- mot2 est une chaine de caractères associée au mot caché;
- lettre qui est le caractère qui remplace un caractère souligné.

La fonction renvoie un mot associé au mot caché avec la lettre qui remplace un ou plusieurs caractères soulignés.

On donne des exemples d'appels de cette fonction:

>>> remplacer_lettre('pendu','p___u','n')
p_n_u

>>> cacher_mot('bonjour','b_____r','o')
bo__o_r


.. rubric:: Vérifier la présence d'une lettre

A chaque proposition de lettre du joueur, il faut vérifier si la lettre est bien dans le mot à deviner. La fonction
``lettre_dans_mot`` prend en paramètre le mot à deviner et la lettre à vérifier.

La fonction renvoie un booléen, c'est à dire la valeur ``True`` si la lettre passée en argument est dans le mot passé
en argument ou la valeur ``False`` dans le cas contraire.

On donne des exemples d'appels de cette fonction:

>>> lettre_dans_mot('pendu','n')
True

>>> lettre_dans_mot('bonjour','s')
False

.. rubric:: Nombre de lettres à trouver

La fonction ``reste_a_trouver`` est une fonction qui renvoie le nombre de lettres à trouver dans le mot. Elle prend en
paramètre un mot ``m`` et renvoie un nombre entier correspondant au nombre de soulignés encore présent dans le mot
passé en argument.

On donne des exemples d'appels de cette fonction:

>>> reste_a_trouver('pendu')
0

>>> reste_a_trouver('bo__o_r')
3

.. rubric:: Dessiner la potence

Il existe différentes façons de représenter la potence. La potence a finalement 5 états différents. Pour notre jeu,
nous allons la représenter dans chaque état par une chaine de caractère. L'exemple ci-dessus nous en donne une
illustration.

La fonction ``afficher_pendu`` a pour paramètre un nombre entier ``n`` et renvoie une chaine de caratères qui
représente l'une des 5 potences possibles. La potence renvoyée dépend de la valeur de l'argument ``n``.

Les 5 figures peuvent être tracées dans un fichier texte et ensuite transformée en chaine de caractères. Vous pouvez
apporter votre touche persionnelle à ces représentations.

On donne des exemples d'appels de cette fonction:

>>> afficher_pendu(2)
   |
   |
   |
   |
___|___


>>> afficher_pendu(5)
   _________
   |       |
   |       O
   |      /|\
   |      / \
___|___


Programme principal
-------------------

Le programme principal consiste à dérouler une partie contre la machine jusqu'à l'issue du jeu. Soit le joueur gagne en
trouvant le mot, soit il est pendu et perd.

Le programme principal se décompose en trois parties:

#. On initialise les variables du programme
#. On crée une boucle de jeu
#. On conclut en affichant le gagnant ou le perdant.

.. rubric:: Initialiser les variables

Il faut considérer au moins quatre variables : ``mot_a_deviner``, ``mot_cache``, ``n`` et ``r``.

- La variable ``mot_a_deviner`` contient le mot à deviner que le joueur doit ignorer. Pour les test on saisira un mot choisi en exemple.
- la variable ``mot_cache`` contient le mot à deviner en remplaçant les lettres par des soulignés. Il évolue au fil de la partie en remplaçant les soulignés par les lettres trouvées.
- La variable ``n`` est le nombre entier qui contient le nombre d'erreurs commises par le joueur.
- La variable ``r`` est le nombre entier qui contient le nombre de lettre qu'il faut encore découvrir.

Il faut donc créer ces variables et leur donner une valeur initale.

.. rubric:: Boucle de jeu

Le jeu se déroule tant que le joueur n'a pas touver toutes les lettres et s'il n'a pas commis plus de 5 erreurs.

A chaque itération, plusieurs instructions sont effectuées:

- Le joueur voit le mot caché affiché avec des caractères soulignés.
- Une proposition de saisie de lettre est affichée juste après.
- Le joueur doit saisir une lettre qui est mémorisée dans une variable ``lettre``.
- La lettre est vérifiée. Si elle est correcte, elle remplace le ou les caractères soulignés correspondant dans le mot caché. Dans le cas contraire, on affiche la potence qui se complète.

.. rubric:: Fin de la partie

La boucle se termine lorsque le joueur a trouvé le mot ou lorsqu'il a perdu et se retrouve pendu.

Dans les 2 cas, on affiche un message et le mot qui était à trouver.

Amélioration du jeu
-------------------

#. Intégrer des tests pour gérer certaines situations:

   - une mauvaise saisie (chiffre, vide, plusieurs lettres)
   - les accents dans les mots
   - les mots avec un tiret comme week-end
   - le nombre de lettre réellement à trouver et non le nombre de caractères soulignés

#. Afficher des informations supplémentaires:

   - les lettres déjà proposées par le joueur
   - le nombre d'échecs du joueur

#. Ajouter une fonction qui choisit un mot au hasard parmi une liste de mots placés dans un fichier texte. La création
   de cette fonction est difficile et requiert des recherches sur le web, notamment sur l'instruction python ``open``
   qui gère la lecture de fichier texte.

#. Toute autre idée qui rend le jeu plus attrayant. Soyez créatifs mais restez dans la possibilité du programmable !
