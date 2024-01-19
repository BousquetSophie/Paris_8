def inverse_mod(n, modulo):
	
	if pgcd(n,modulo) != 1 :
		print(n, " modulo ", modulo, " n'est pas inversible")
		return
	
	i = bezout(n,modulo)
	
	print("L'inverse de ", n, " est ", i)
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
	
inverse_mod(5,7)
