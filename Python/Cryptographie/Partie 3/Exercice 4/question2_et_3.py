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
	texte_final = []
	
	for i in range(len(texte)-1, -1, -1):
		texte_final.append(texte[i][1])
		texte_final.append(texte[i][0])
		
	return texte_final
	
# si on veut que rassembler_texte renvoie le texte sous forme de tuples

def rassembler_texte_tuple(texte):
	lst = []
	texte_final = []
	
	for i in range(len(texte)-1, -1, -1):
		lst.append(texte[i][1])
		lst.append(texte[i][0])
		
		texte_final.append(lst)
		lst = []
		
	return texte_final
	
texte1 = "azerty"

print(decouper_texte(texte1))	
print()
print(rassembler_texte(decouper_texte(texte1)))
print()
print(rassembler_texte_tuple(decouper_texte(texte1)))	
