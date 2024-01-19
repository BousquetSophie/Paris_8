def determiner_cle(chaine_charactere):
	alphabet = [" ","a","b","c","d","e","f","g","h","i",
"j","k","l","m","n","o","p","q","r","s","t","u","v",
"w","x","y","z",",","."]
	
	lst = freq_lettres(chaine_charactere)
	
	#va ranger la liste par ordre décroissant
	lst_decroissant = sorted(lst, key=lst.get, reverse=True)
	#key=lst.get permet de trier les éléments de la liste en utilisant leur
	# fréquence d'apparition, au lieu de leur ordre alphabétique.
	
	lst_lettre = [f[0] for f in lst_decroissant] #sert a garder que les lettres
	
	e1 = alphabet.index(lst_lettre[0])
	espace1 = alphabet.index(lst_lettre[1])
	
	
	e2 = alphabet.index(lst_lettre[1])
	espace2 = alphabet.index(lst_lettre[0])
	
	b1 = espace1

	b2 = espace2
	
	a1 = ((e1-b1)*inverse_mod(5,29))%29
	a2 = ((e2-b2)*inverse_mod(5,29))%29
			
	message1 = dechiffrer_aff(chaine_charactere, a1, b1)
	message2 = dechiffrer_aff(chaine_charactere, a2, b2)
	
	print("a1 =", a1, "b1 =", b1)
	print(message1)
	print()
	print("a2 =", a2, "b2 =", b2)
	print(message2)
	
	
	
	return a1,b1,message1,a2,b2,message2
	
def freq_lettres(texte):
	lst = {}
	for l in texte:
		if l not in lst:
			lst[l] = 1
		else:
			lst[l] += 1
	return lst

def inverse_mod(n, modulo):
	
	if pgcd(n,modulo) != 1 :
		print(n, " modulo ", modulo, " n'est pas inversible")
		return
	
	i = bezout(n,modulo)
	
	return i
	
def pgcd (a,b):
	if b ==0:
		return a
	else:
		r= a % b
	return pgcd(b,r)
	
def bezout(a,b):
	x=1
	y=0
	u=0
	v=1
	while b != 0:
		q=a//b
		r=a%b
		m=x-u*q
		n=y-v*q
		a=b
		b=r
		x=u
		y=v
		u=m
		v=n
	return x
	
def dechiffrer_aff(m,a,b) :
	alphabet = [" ","a","b","c","d","e","f","g","h","i",
"j","k","l","m","n","o","p","q","r","s","t","u","v",
"w","x","y","z",",","."]
	
	message_dechiffree = ""	
	a_inverse = inverse_mod(a,29)
	for i in range (len(m)):
		indice = alphabet.index(m[i])
		indice_dechiffree = (a_inverse * (indice - b))%29
		message_dechiffree = message_dechiffree + alphabet[indice_dechiffree]		

	return message_dechiffree
		
message = "akdyne.vxnk bijdju.dfodjoujhrajdcjd.jyboigfjudgfid jnhj..jo.dcjdybiqqnjndj.dcjdcjybiqqnjndfodhjuukxjsdcvo.dajdyvo.jofdojdcvi.dj.njdyvoofdgfjdcjduvodj, jci.jfndj.dcjduvodcju.iok.kinjz"

determiner_cle(message)





