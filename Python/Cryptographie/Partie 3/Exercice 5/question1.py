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
	
matrice = []
a = [12,17]
b = [3,5]

matrice.append(a)
matrice.append(b)

print(inverse_mod(matrice))
