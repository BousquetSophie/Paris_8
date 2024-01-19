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

a = 4
b = 21
message = "v.vlukyu,fwtfyooyn.ws"

print(dechiffrer_aff(message,a,b))
