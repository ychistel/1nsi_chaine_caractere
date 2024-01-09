.. 1NSI

.. toctree::
   :maxdepth: 1
   
Les chaines de caractères
=========================

Le type str
-----------

Une variable Python qui contient un texte entre des quote est une chaine de caractères. On dit que cette variable est
de type **str** pour **string**.

.. admonition:: Exemple

   >>> ch = 'bonjour le monde'
   >>> type(ch)
   <class 'str'>
      
Une variable de type **str** peut être manipulée:

- par des fonctions natives comme ``len`` qui renvoie sa longueur c'est à dire le nombre de caractères que contient la chaine.
- en accédant à une position particulière de la chaine.

.. admonition:: Exemple

   >>> ch = 'bonjour le monde'
   >>> len(ch)
   16

   La chaine contient 16 caractères

   >>> print(ch[0])
   b

La chaine est itérable
----------------------

Une chaine de caractères est itérable ce qui signifie qu'on peut la parcourir caractère par caractère avec une boucle.

-  Avec une boucle bornée ``for``:

   .. admonition:: Exemple

      En utilisant les indices de position:
      
      >>> ch = 'bonjour le monde'
      >>> for k in range(len(ch)):
	      print(ch[k])

      En utilisant les caractères directement:

      >>> ch = 'bonjour le monde'
      >>> for caractere in ch:
	      print(caractere) 

-  Avec une boucle conditionnelle:

   .. admonition:: Exemple
   
      >>> ch = 'bonjour le monde'
      >>> k = 0
      >>> while ch[k] != 'j':
              print(ch[k])
	      k = k + 1
      b
      o
      n

Concaténation
-------------

On peut effectuer deux opérations sur les chaines de caractères. L'**addition** et la **multiplication** sont 2 opérations
permises réalisant la **concaténation**.

-  L'addition assemble deux chaines de caractères en une seule.

   .. admonition:: Exemple

      >>> m1 = 'bon'
      >>> m2 = 'jour'
      >>> m = m1 + m2
      >>> print(m)
      bonjour

-  La multiplication d'une chaine de caractères par un nombre entier qui donne une chaine de caractères contenant la
   chaine initiale concaténée k fois.

   .. admonition:: Exemple

      >>> m1 = 'bon'
      >>> m = m1 * 2
      >>> print(m)
      bonbon

