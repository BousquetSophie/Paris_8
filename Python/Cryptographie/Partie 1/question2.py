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

def nbPremier_alea(minn,maxx):
	while True:
		nb = random.randint(minn, maxx)
		if est_premier(nb) == True :
			print(nb)
			return nb
            
nbPremier_alea(2,30)

	
