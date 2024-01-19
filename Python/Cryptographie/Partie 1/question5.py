import random
import math

def chiffrer_rsa(m):
	global d
	global n
	
	c = pow(m, d, n)
	print("message chiffrer  :", c)
	return c
	
p = 11
q = 23
n = p*q
d = 7
message = 100

print("d =", d)
print("p =", p, ", q =", q)
print("message =", message)

chiffrer_rsa(message)

