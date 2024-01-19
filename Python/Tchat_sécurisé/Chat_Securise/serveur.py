import socket
import threading

def communication(connexion, address):
	mess_deco = "Le client s'est déconnecter"
	while True:
		client_msg = connexion.recv(1024) #Recevoir des données du client
		
		if str(client_msg, 'utf-8') == 'quitter':
			print("Le client s'est déconnecté")
			# Envoyer le message à tous les autres clients connectés
			for other_client_socket in clients: 
				# permet de ne pas envoyer le message au client qui l'a envoyé
				if other_client_socket != connexion:
					other_client_socket.sendall(mess_deco.encode())
			clients.remove(connexion) #supprime le client de la liste des clients connecter
			connexion.close() #Ferme la connexion avec le client
			break
			
		message = client_msg.decode()
        
		#nom du client
		if clients[0] == connexion:
			nom_client = "Client 1"
		else :
			nom_client = "Client 2"
        	
		print(f"{nom_client} : {str(client_msg,'utf-8')}")
        
		# Envoyer le message à tous les autres clients connectés
		for other_client_socket in clients:
			# permet de ne pas envoyer le message au client qui l'a envoyé
			if other_client_socket != connexion:
				other_client_socket.sendall(message.encode())

# Adresse IP et numéro de port du serveur
HOST = '127.0.0.1'
PORT = 18023

# Création de la socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Association de l'adresse et du numéro de port à la socket
server_socket.bind((HOST,PORT))

print("Socket créée")

server_socket.listen(2) #nombre de connexion max

# Liste des clients connectés
clients = []

print("Reception des appels")

while True:

	connexion, address = server_socket.accept()
	print(f"Connecté à {address}")
	
	# Ajouter les clients à la liste des clients connectés
	clients.append(connexion)
	client_thread = threading.Thread(target=communication, args=(connexion, address))
	client_thread.start()
	
	
	if not clients:
		print("Socket Fermé")
		break
		
server_socket.close() #Ferme la socket du serveur
