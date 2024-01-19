def chiffrer_hill(texte, matrice, vecteur):
	alphabet = [" ","a","b","c","d","e","f","g","h","i",
"j","k","l","m","n","o","p","q","r","s","t","u","v",
"w","x","y","z",",","."]
	
	message_chiffree = ""
	texte_decoup = decouper_texte(texte)
	texte_rass = rassembler_texte(texte_decoup)
	
	indice = []
	lst_final = []
	
	for i in range (len(texte_rass)):
		indice0 = alphabet.index(texte_rass[i][0])
		indice1 = alphabet.index(texte_rass[i][1])
		
		indice.append(indice0)
		indice.append(indice1)
		
		lettre_chiff = multMatriceVect(matrice, indice)
		lettre_chiff = sommeVect(lettre_chiff, vecteur)
		
		lst_final.append(alphabet[lettre_chiff[0]%29])
		lst_final.append(alphabet[lettre_chiff[1]%29])
		indice=[]
		
	return lst_final
	
	
def multMatriceVect(matrice, vecteur):
	vecteur_final = []
	
	x = (matrice[0][0] * vecteur[0]) + (matrice[0][1] * vecteur[1])
	y = (matrice[1][0] * vecteur[0]) + (matrice[1][1] * vecteur[1])
	
	vecteur_final.append(x)
	vecteur_final.append(y)
	
	return vecteur_final
	
def sommeVect(vecteur1, vecteur2):
	vecteur_final = []
	
	x = vecteur1[0] + vecteur2[0]
	y = vecteur1[1] + vecteur2[1]
	
	vecteur_final.append(x)
	vecteur_final.append(y)
	
	return vecteur_final
	
def decouper_texte(texte):
	lst_final = []
	lst = []
	a = len(texte)-1
	
	if (len(texte)%2) == 0:
		for i in range((len(texte))//2):
			for j in range(2):
				lst.append(texte[a])
				a = a - 1
			lst_final.append(lst)
			lst = []
			
	elif len(texte)%2 == 1:
		for i in range(len(texte)//2):
			for j in range(2):
				lst.append(texte[a])
				a = a - 1
			lst_final.append(lst)
			lst = []
		lst.append(texte[0])
		lst.append(" ")
		lst_final.append(lst)
	
	return lst_final

def rassembler_texte(texte):
	lst = []
	texte_final = []
	
	for i in range(len(texte)-1, -1, -1):
		lst.append(texte[i][1])
		lst.append(texte[i][0])
		
		texte_final.append(lst)
		lst = []
		
	return texte_final
	
	
texte = "exexexex"
ab = [5,7]
cd = [1,15]
a = []
a.append(ab)
a.append(cd)


b = [1,2]


print(chiffrer_hill(texte, a, b))
