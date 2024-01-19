import math

def est_premier(n):
	if n <= 1:
		print(n, "n'est pas premier")
		return False
	elif n == 2:
		print(n, "est premier")
		return True
	else:
		for i in range(2, int(math.sqrt(n)) + 1):
			if n % i == 0:
				print(n, "n'est pas premier")
				return False
		print(n, "est premier")
		return True

est_premier(11)
est_premier(6)
