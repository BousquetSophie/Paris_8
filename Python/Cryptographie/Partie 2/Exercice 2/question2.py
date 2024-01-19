def chiffrer_aff(a,b,m) :
	alphabet = [" ","a","b","c","d","e","f","g","h","i",
"j","k","l","m","n","o","p","q","r","s","t","u","v",
"w","x","y","z",",","."]
	
	message_chiffree = ""	
	
	for i in range (len(m)):
		indice = alphabet.index(m[i])
		indice_chiffree = (a*indice+b)%29
		message_chiffree = message_chiffree + alphabet[indice_chiffree]		

	return message_chiffree

a = 4
b = 21
message = "la clef est dans le coffre"

print(chiffrer_aff(a,b,message))
