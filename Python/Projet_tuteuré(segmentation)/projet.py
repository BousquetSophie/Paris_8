from lxml import etree
import spacy
import re

print("Chargement du modèle de langue en cours veuillez patienter.")
#Chargement du modèle de traitement du langage naturel pour le français en utilisant que la tokenisation
nlp = spacy.load("fr_core_news_sm", disable=["tagger", "parser", "ner"])

#Liste des mots d'hésitation
hesitation = ["euh", "oh", "hm", "ben"]
#Expression régulière pour les parenthèses
parenthese = r"[()]"
#Expressions régulières pour le texte entre parenthèses
texte_p = r"[A-Z]|[a-z]\([A-Z]|[a-z]"
texte_po = r"[A-Z]|[a-z]\([A-Z]|[a-z]"
texte_pf = r"[A-Z]|[a-z]\)[A-Z]|[a-z]"
est_dans_p = False
texte_dans_p = ""

titre = input("Entrez le nom de votre document : ")

#Chargement du fichier XML
fichier = etree.parse(titre)

#Titres des différents fichiers
titre2 = titre.replace(".xml", "_tokeniser.xml")
titre_brut = titre.replace(".xml", "_brut.txt")
titre_clear = titre.replace(".xml", "_nettoyer.txt")

#Création fichier XML tokeniser
with open(titre2, 'w') as resultat:
    print("\nVotre document est en cours de tokenisation veuillez patienter.\n")
    #En-tête du fichier XML
    resultat.write('<?xml version="1.0" encoding="utf-8"?>' + "\n")
    resultat.write("<entretient>\n")
    mot_avant = "" #utiliser pour les répétitions
    for i, dialogue in enumerate(fichier.xpath("/TEXT/S/FORM")):
        #On ajoute des espace après les ] sinon sa créer des problème de tokenisation
        dialogue.text = re.sub(r'\]', r'] ', dialogue.text)
        resultat.write("    <tour id="+'"'+ str(i) +'">\n')
        phrase = nlp(dialogue.text)
        #Parcourir chaque token des dialogues
        for i, token in enumerate(phrase):
            #Gestion des hésitation
            if token.text in hesitation :
                resultat.write("        <hesitation>" + token.text + "</hesitation>\n")
                mot_avant = token.text
            #Ignorer les parenthèses
            elif(token.text == "(") or (token.text == ")"):
                pass
            #Gestion des mots contenant des parenthèses
            elif ("(" in token.text) or (")" in token.text):
                txt = token.text
                txt = re.sub(parenthese, "", txt)
                if(i+1 < len(phrase)) and (phrase[i+1].text == ")"):
                    if(mot_avant == txt): #Gestion de répétition avec anomalie
                        resultat.write("        <repetition original=" + '"' + token.text + ')">' + txt + "</repetition>\n")
                    else :
                        resultat.write("        <mot original=" + '"' + token.text + ')">' + txt + "</mot>\n")
                elif(phrase[i-1].text == "("):
                    if(mot_avant == txt): #Gestion de répétition avec anomalie
                        resultat.write("        <repetition original=" + '"(' + token.text + '">' + txt + "</repetition>\n")
                    else :
                        resultat.write("        <mot original=" + '"(' + token.text + '">' + txt + "</mot>\n")
                else :
                    if(mot_avant == txt): #Gestion de répétition avec anomalie
                        resultat.write("        <repetition original=" + '"' + token.text + '">' + txt + "</repetition>\n")
                    else :
                        resultat.write("        <mot original=" + '"' + token.text + '">' + txt + "</mot>\n")
                mot_avant = txt
            #Gestion des parenthèse de c() et e()
            elif(i+2 < len(phrase)) and (phrase[i+1].text == "(") and (phrase[i+2].text == ")"):
                mot = token.text + "()"
                if(mot == "e()"):
                    resultat.write("        <hesitation original=" + '"' + mot + '">heu</hesitation>\n')
                    mot_avant = "heu"
                elif(mot == "c()"):
                    if(mot_avant == "ça"): #Gestion de répétition avec anomalie
                        resultat.write("        <repetition original=" + '"' + mot + '">ça</repetition>\n')
                    else:
                        resultat.write("        <mot original=" + '"' + mot + '">ça</mot>\n')
                    mot_avant = "ça"
            #Extraction des - dans les tokens
            elif (token.text[0] == "-"):
                resultat.write("        <mot>" + "-" + "</mot>\n")
                resultat.write("        <mot>" + token.text[1:] + "</mot>\n")
                mot_avant = token.text[1:]
            #Gestion des répétitions
            elif (mot_avant == token.text):
                resultat.write("        <repetition>" + token.text + "</repetition>\n")
                mot_avant = token.text
            #Gestion des descriptions d'ambiance
            elif (est_dans_p or token.text == "["):
                if (token.text == "]"):
                    resultat.write("        <ambiance>" + texte_dans_p + "]" + "</ambiance>\n")
                    mot_avant = texte_dans_p
                    est_dans_p = False
                    texte_dans_p = ""
                else:
                    texte_dans_p += token.text
                    est_dans_p = True
            #Gestion des mots sans anomalie
            else :
                if (token.text != " "):
                    resultat.write("        <mot>" + token.text + "</mot>\n")
                    mot_avant = token.text
            
        resultat.write("    </tour>\n")
    resultat.write("</entretient>\n")

#Chargement du fichier XML tokenisé
fichier2 = etree.parse(titre2)

#Création du fichier texte avec les données brut
with open(titre_brut, 'w') as brut:
    for phrase in fichier.xpath("/TEXT/S/FORM"):
        brut.write(phrase.text + "\n")

#Création du fichier texte avec les données tokenisées
with open(titre_clear, 'w') as clear:
    for tour in fichier2.xpath("/entretient/tour"):
        vide = False
        mots = tour.xpath("mot")
        for i in range(len(mots)):
            mot = mots[i]
            if mot.text != "":
                # Vérification pour les contractions et le mot suivant
                if mot.text[-1] == "'" or mot.text == "-"or (i + 1 < len(mots) and mots[i + 1].text == "-"):
                    clear.write(mot.text)
                else:
                    clear.write(mot.text + " ")
                vide = True
        if vide:  # si le tour est vide on a un \n en trop
            clear.write("\n")

print("La tokenisation est terminée, vous retrouverez le résultat dans le fichier :", titre2, "\n")
print("Le fichier texte avec le texte brut se trouve dans le fichier :", titre_brut, "\n")
print("Le fichier texte avec le texte tokenisé se trouve dans le fichier :", titre_clear)
