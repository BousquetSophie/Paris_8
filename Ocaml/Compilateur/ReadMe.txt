Sophie Bousquet 
21001557 
L3-A

Fonctionnalités implémentées :

les type_t pour les erreurs de typage : Int_t, Bool_t

Les expressions : 
- entier (Int)
- booléen (Bool)
- variable (Var)
- appel de fonction (Call)

Les instructions : 
- Déclaration de variable (Decl)
- Assignation de variable (Assign)
- Condition if else (Cond)
- Boucle while (Loop)
- Renvoie de la valeur d'une expression (Return)

Ainsi que les blocks d'instructions (block)


Gestion d'erreurs implémentées :

- Erreur de typage pour les déclarations et assignations de variables
- Erreur de typage pour les appels de fonction
- Erreur si la variable appelée n'est pas déclarée
- Erreur s'il n'y a pas le bon nombre d'arguments pour les fonctions
- Erreur si la fonction appelée n'existe pas ou si ce n'est pas une fonction
- Erreur si l'expression de Loop ou Cond n'est pas un booléen


Syntaxe :
La syntaxe utilisée est celle du C, sauf pour les prints qui peuvent être appelés que lors d'une instruction. Le plus souvent dans mes tests, j'ai mis des prints dans le return.
De plus, on a 2 print : printi pour les int et printb pour les bool.
De même, on a scani pour demander un nombre à l'utilisateur.


Comment compiler et lancer les tests :

Pour compiler et lancer les tests, il faut lancer dune build main.exe
Puis faire ./main.exe ./tests/fichier.test 
Par exemple ./main.exe ./tests/call.test

Les fichiers tests commençant par err correspondent aux tests des erreurs.