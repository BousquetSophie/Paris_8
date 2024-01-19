def dechiffrer_hill(texte, matrice, vecteur):
	alphabet = [" ","a","b","c","d","e","f","g","h","i",
"j","k","l","m","n","o","p","q","r","s","t","u","v",
"w","x","y","z",",","."]
	
	message_chiffree = ""
	texte_decoup = decouper_texte(texte)
	texte_rass = rassembler_texte(texte_decoup)
	
	indice = []
	lst_final = []
	
	matrice = inverse_mod(matrice)
	
	for i in range (len(texte_rass)):
		indice0 = alphabet.index(texte_rass[i][0])
		indice1 = alphabet.index(texte_rass[i][1])
		
		indice.append(indice0)
		indice.append(indice1)
		
		lettre_chiff = sousVect(indice, vecteur)
		lettre_chiff = multMatriceVect(matrice, lettre_chiff)
		
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
	
def sousVect(vecteur1, vecteur2):
	vecteur_final = []
	
	x = vecteur1[0] - vecteur2[0]
	y = vecteur1[1] - vecteur2[1]
	
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
	
def det(matrice):
	
	d = (((matrice[0][0])*(matrice[1][1]))-((matrice[0][1])*(matrice[1][0])))
	
	return d%29
	
def inverse_mod(matrice):
	
	a = [matrice[1][1]%29,(-matrice[0][1])%29]
	b = [(-matrice[1][0])%29,matrice[0][0]%29]
	
	matrice1 = []
	matrice1.append(a)
	matrice1.append(b)
	
	inv_det = pow(det(matrice),-1,29)
	
	a1 = multMatriceCoeff(matrice1,inv_det)
	
	for i in range(len(a1)):
		a1[i][0] = a1[i][0]%29
		a1[i][1] = a1[i][1]%29
	
	return a1
	
def multMatriceCoeff(matrice, x):
	matrice_final = []
	ab = []
	cd = []
	
	a = matrice[0][0] * x
	b = matrice[0][1] * x
	c = matrice[1][0] * x
	d = matrice[1][1] * x
	
	ab.append(a)
	ab.append(b)
	cd.append(c)
	cd.append(d)
	
	matrice_final.append(ab)
	matrice_final.append(cd)
	
	return matrice_final
	
	
texte = "tststs"
ab = [5,7]
cd = [1,15]
a = []
a.append(ab)
a.append(cd)


b = [1,2]


print(dechiffrer_hill(texte, a, b))
