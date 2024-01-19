def multMatrice (matrice1, matrice2):
	matrice_final = []
	ab = []
	cd = []
	
	a = (matrice1[0][0] * matrice2[0][0]) + (matrice1[0][1] * matrice2[1][0])
	b = (matrice1[0][0] * matrice2[0][1]) + (matrice1[0][1] * matrice2[1][1])
	c = (matrice1[1][0] * matrice2[0][0]) + (matrice1[1][1] * matrice2[1][0])
	d = (matrice1[1][0] * matrice2[0][1]) + (matrice1[1][1] * matrice2[1][1])
	
	ab.append(a)
	ab.append(b)
	cd.append(c)
	cd.append(d)
	
	matrice_final.append(ab)
	matrice_final.append(cd)
	
	return matrice_final
	
def multMatriceVect(matrice, vecteur):
	vecteur_final = []
	
	x = (matrice[0][0] * vecteur[0]) + (matrice[0][1] * vecteur[1])
	y = (matrice[1][0] * vecteur[0]) + (matrice[1][1] * vecteur[1])
	
	vecteur_final.append(x)
	vecteur_final.append(y)
	
	return vecteur_final

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
	
def sommeVect(vecteur1, vecteur2):
	vecteur_final = []
	
	x = vecteur1[0] + vecteur2[0]
	y = vecteur1[1] + vecteur2[1]
	
	vecteur_final.append(x)
	vecteur_final.append(y)
	
	return vecteur_final

#créer les matrices	

lst1 = [2,5] #a b
lst2 = [4,3] #c d

lst3 = [4,9] #a b
lst4 = [2,7] #c d

matrice1 = []

matrice1.append(lst1)
matrice1.append(lst2)

matrice2 = []

matrice2.append(lst3)
matrice2.append(lst4)

#créer les vecteurs

vecteur1 = [3,8]
vecteur2 = [6,4]

#appel des fonctions

print(multMatrice(matrice1, matrice2))

print(multMatriceVect(matrice1, vecteur1))

print(multMatriceCoeff(matrice2, 7))

print(sommeVect(vecteur1, vecteur2))

