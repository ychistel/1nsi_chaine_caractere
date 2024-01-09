.. 1NSI

.. toctree::
   :maxdepth: 1

Exercices
=========

Exercice 1
----------

#. Créer 3 variables ``a``, ``b`` et ``c`` de type **str**  ayant pour valeurs respectives "numérique", "science" et
   "informatique".
#. Soit ``t`` la variable de type **str**. Quelle opération sur les variables ``a``, ``b`` et ``c`` permet d'affecter
   la valeur "numérique science informatique" à la variable ``t`` ?
#. Ecrire une suite d'instructions en Python pour ajouter un "s" à la fin de chaque mot de la chaine de caractères
   contenue dans la variable ``t``.


Exercice 2
----------

On donne le code de la fonction ``occurence`` ci-après.

.. literalinclude:: ../python/exercices.py
   :lines: 3-8
   :language: python

#. Quelle est la valeur renvoyée par la fonction ``occurence`` suite à l'appel ``occurence('abracadabra')`` ?
#. On veut connaître le nombre d'apparitions de la lettre 'e' dans la chaine passée en argument lors de l'appel de la
   fonction. Quelle(s) modifications faut-il faire sur la fonction ?
#. Proposer un code Python qui permet de compter le nombre d'apparitions d'une lettre passée en argument de la fonction
   ``occurence``.

.. note::

   On appelle **occurence** d'un caractère le nombre de fois que ce caractère est contenu dans une chaine de
   caractères.

Exercice 3
----------

Toute variable de type **str** est ce qu'on appelle un **objet** en Python. Un **objet** est une structure de donnée
qui permet d'appliquer des fonctions définies pour cet objet. Ces fonctions propres à l'objet sont appelées des
**méthodes** et s'appliquent à l'objet selon la syntaxe ``objet.méthode()``.

Les méthodes disponibles pour les objets de type **str** sont nombreuses. En voici quelques unes:

- ``count(caractere)`` renvoie le nombre d'occurence du caractère passé en argument.
- ``upper()`` renvoie la chaine de caractères en lettre majuscule.
- ``lower()`` renvoie la chaine de caractères en lettre minuscule.
- ``replace(caractère_1, caractere_2)`` remplace dans la chaine de caractères chaque ``caractere_1`` par le
  ``caractere_2``.

Soit ``ch`` la variable de type **str** contenant la chaine 'numérique science informatique'.

#. Soit ``M`` la variable de type **str**. Ecrire une instruction Python qui affecte la même chaine de caractères que la
   variable ``ch`` en majuscules.

#. Ecrire une instruction qui renvoie le nombre d'occurence de la lettre 'e' dans la chaine ``ch``.

#. Remplacer dans la chaine de caractère ``ch`` chaque lettre 'i' par la lettre 'o'.

#. Ecrire une instruction Python qui supprime les espaces de la chaine de caractères ``ch``.

Exercice 4
----------

On souhaite écrire la fonction ``nombre_mots`` en Python qui renvoie le nombre de mots contenus dans une chaine de
caractères. On considère que les mots présents dans une chaine sont séparés par un espace.

La fonction ``nombre_mots`` a pour paramètre ``chaine`` qui est de type **str**. Elle renvoie un nombre entier positif.

#. Ecrire le code de cette fonction et la tester avec la chaine 'numérique science informatique'.
#. On appelle la fonction avec la chaine 'un tour de passe-passe' qui contient 5 mots. La valeur renvoyée par la
   fonction est-elle correcte ? Apporter une correction à votre fonction pour qu'elle renvoie la valeur attendue.
