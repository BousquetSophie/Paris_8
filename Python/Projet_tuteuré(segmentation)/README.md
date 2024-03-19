# Projet Tuteuré 
Découper la recette de l’omelette (programmation python)

# Sujet

L’idée de ce projet est de découper automatiquement les transcriptions
écrites de l’oral en utilisant Python.

C’est un défi, car la parole peut être pleine d’hésitations, de répétitions et de
mots tronqués. Par ailleurs, lors de la transcription, lorsqu’on rencontre ces
problème-là, cela entraîne des anomalies telles que des parenthèses en pleins
milieu du mot ou encore des hésitation telles que « heu », « hm » etc.

L’objectif, c’est de regarder comment nous pouvons supprimer ces anomalies
qui perturbent le découpage de la transcription écrite.

On va d’abord passer en revue ce qui se fait déjà pour découper la parole.
Ensuite, on va créer un outil qui prendra en compte ces particularités de la
parole.

On va tester cet outil sur des enregistrements, comme la recette de l’omelette
que l’on trouve sur Cocoon. Cocoon est une plateforme contenant divers cor-
pus audios accompagnés par leurs annotations qui incluent « qui parle », «
à quel moment », ainsi que leur transcription écrite de l’oral.

L’idée, c’est de découper tout cela en phrases et en mots, pour permettre
l’analyse ultérieur.

# Etape

1. Crée un fichier XML basique qui contient les dialogues, découper en mot dans des balises.
2. Rajouter des balises pour les hésitations.
3. Rajouter des balises annomalie pour les mots contenant des parenthèses. (exemple : <mot original="i(l)"> il <mot> )
4. Tokénisation des "-" à part
5. Rajouter des balises ambiance pour les description d'ambiance contenu dans des crochets.
6. Rajouter des balises pour les répétitions de mot dans les dialogues.
