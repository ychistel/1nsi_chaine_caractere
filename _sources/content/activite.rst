.. 1NSI

.. toctree::
   :maxdepth: 1

Activité
========

En Python, une chaine de caractères se note entre des *quote* simples ou doubles (guillemets).

On peut manipuler les chaines de caractères en Python.

- La fonction ``len`` renvoie le nombre de caractères contenus dans la chaine.
- La fonction ``type`` renvoie le type de la variable.
- On peut accéder à un caractère précis dans la chaine de caractères.

Premières manipulations
-----------------------

On considère la variable ``ch`` de type **str** contenant la chaine *numérique science informatique*.


#. Créer dans un interpréteur Python la variable ``ch``.
#. Créer une variable ``n`` qui a pour valeur le nombre de caractères de la chaine ``ch``.
#. Chaque caractère de la chaine occupe une position précise dans la chaine. Cette position est repérée par un nombre
   entier.
   
   a. Saisir dans l'interpréteur ``ch[0]`` puis valider. De même avec ``ch[1]`` puis avec ``ch[2]``.
   b. Quelle instruction permet d'afficher la première lettre du second mot de la chaine ``ch`` ?
   c. Comment afficher la dernière lettre de la chaine ``ch`` ?

Un objet itérable
-----------------

On peut parcourir les caractères, un à un, d'une chaine de caractères avec une boucle. On dit qu'elle est **itérable**.

Voici différentes façons de le faire.

#. Recopier et compléter la boucle ``for`` suivante pour afficher un à un les caractères de la chaine ``ch``.

   .. code-block::

      for k in range(...):
	  print(...)

#. Il est également possible de parcourir une chaine de caractères sans passer par les indices de position.

   a. Selon vous, le code suivant réalise-t-il le même affichage que la méthode précédente.

      .. code-block::

	 for lettre in ch:
	     print(lettre)

   b. Que se passe-t-il si on remplace dans le code précédent ``lettre`` par ``mot`` ?

#. On peut aussi utiliser une boucle conditionnelle pour parcourir partiellement une chaine de caractères.

   a. Que permet d'obtenir le code suivant ?

      .. code-block::

	 lettre = ch[0]
	 i = 0
	 while lettre != 'i':
	     i = i + 1
	     lettre = ch[i]
	 print(i)

   b. Comment améliorer l'écriture du code précédent pour le rendre plus lisible ?
   c. Modifier ce code pour connaître la longueur du premier mot de la chaine.

La concaténation
----------------

On effectue des opérations sur les nombres. On peut effectuer deux opérations sur les chaines de caractères. L'addition
et la multiplication sont 2 opérations permises réalisant la **concaténation**.

- L'addition assemble deux chaines de caractères en une seule
- La multiplication crée une chaine de caractères à partir d'un motif qu'il concatène plusieurs fois.

#. Créer 3 variables ``m1``, ``m2`` et ``m3`` contenant respectivement les mots 'numérique', 'science' et
   'informatique'.
   Concaténer ces 3 variables dans la variable ``ch`` pour obtenir une chaine de caractères de valeur 'numérique science
   informatique'.

#. Afficher la variable ``ch``. Que remarquez-vous ? Proposer une solution pour y remédier.
#. La variable `p` est une chaine de caratères qui contient la valeur 'zzzzzzzzzzzzzzz' constituée de 15 'z'. Créer la variable `p`.
