import random
import math

def dechiffrer_rsa(m):
	global e
	global n
	
	c = pow(m, e, n)
	print("message dechiffrer  :", c)
	return c


def inverse_mod(n, modulo):
	
	if pgcd(n,modulo) != 1 :
		print(n, " modulo ", modulo, " n'est pas inversible")
		return 1
		
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

def indic_euler1(n):
	nb = 0
	for i in range (n) :
		if pgcd (i, n) ==1:
			nb +=1
	return nb

p = 11
q = 23

n = p*q
message = 12
d = 7
e = inverse_mod(d,indic_euler1(n))

dechiffrer_rsa(message)
