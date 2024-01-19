import random
import math

def est_premier(n):
	if n <= 1:
		return False
	elif n == 2:
		return True
	else:
		for i in range(2, int(math.sqrt(n)) + 1):
			if n % i == 0:
				return False
		return True

def nbPremier_alea(minn, maxx):
	while True:
		nb = random.randint(minn, maxx)
		if est_premier(nb) == True :
			return nb


p = nbPremier_alea(2,100)
q = nbPremier_alea(2,100)
while(q == p):
	q = nbPremier_alea(2,100)

n = p*q
d = 30

print("p =", p, ", q =", q, "n =", n)
print("d =", d)
