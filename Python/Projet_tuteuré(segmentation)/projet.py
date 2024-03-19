from lxml import etree
import spacy
import re

nlp = spacy.load("fr_core_news_sm")
fichier = etree.parse("crdo-FRA_ESLO_omelette006.xml")

hesitation = ["euh", "oh", "hm", "ben"]
parenthese = r"[()]"
texte_p = r"[A-Z]|[a-z]\([A-Z]|[a-z]"
texte_po = r"[A-Z]|[a-z]\([A-Z]|[a-z]"
texte_pf = r"[A-Z]|[a-z]\)[A-Z]|[a-z]"
est_dans_p = False
texte_dans_p = ""

with open('resultat.xml', 'w') as resultat:
    resultat.write('<?xml version="1.0" encoding="utf-8"?>' + "\n")
    resultat.write("<dialogues>\n")
    for dialogue in fichier.xpath("/TEXT/S/FORM"):
        resultat.write("    <dialogue>\n")
        phrase = nlp(dialogue.text)
        for i, token in enumerate(phrase):
            if token.text in hesitation :
                resultat.write("        <hesitation> " + token.text + " </hesitation>\n")
            elif (token.text == "(") or (token.text == ")"):
                if(re.findall(texte_po, phrase[i-1].text)) and (token.text == ")"):
                    pass
                elif(re.findall(texte_pf, phrase[i+1].text)) and (token.text == "("):
                    pass
                else:
                    resultat.write("        <annomalie> " + token.text + " </annomalie>\n")
            elif ("(" in token.text) or (")" in token.text):
                txt = token.text
                txt = re.sub(parenthese, "", txt)
                if(phrase[i+1].text == ")"):
                    resultat.write("        <annomalie original=" + '"' + token.text + ')"> ' + txt + " </annomalie>\n")
                elif(phrase[i-1].text == "("):
                    resultat.write("        <annomalie original=" + '"(' + token.text + ')"> ' + txt + " </annomalie>\n")
                else :
                    resultat.write("        <annomalie original=" + '"' + token.text + '"> ' + txt + " </annomalie>\n")
            elif (token.text[0] == "-"):
                resultat.write("        <mot> " + "-" + " </mot>\n")
                resultat.write("        <mot> " + token.text[1:] + " </mot>\n")
            elif (phrase[i-1].text == token.text):
                resultat.write("        <repetition> " + token.text + " </repetition>\n")

            elif (est_dans_p or token.text == "["):
                if (token.text == "]"):
                    resultat.write("        <ambiance> " + texte_dans_p + "]" + " </ambiance>\n")
                    est_dans_p = False
                    texte_dans_p = ""
                else:
                    texte_dans_p += token.text + " "
                    est_dans_p = True
                

            else :
                resultat.write("        <mot> " + token.text + " </mot>\n")
        resultat.write("    </dialogue>\n")
    resultat.write("</dialogues>\n")
