def freq_lettres(texte):
	lst = {}
	for l in texte:
		if l not in lst:
			lst[l] = 1
		else:
			lst[l] += 1
	return lst
	
texte = "Bonjours tout le monde"
print(freq_lettres(texte))
		
