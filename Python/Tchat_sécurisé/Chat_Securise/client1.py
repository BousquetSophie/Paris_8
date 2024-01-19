import socket
import threading
import tkinter as tk
import projet
from PIL import ImageTk, Image
import random
import chiffrement

# Charger l'interface depuis client
root = tk.Tk()

# chargement de l'image de fond
img = Image.open("fond.jpg")
img = img.resize((500, 400), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)

# création du widget d'image de fond
fond_label = tk.Label(root, image=img)
fond_label.place(x=0, y=0, relwidth=1, relheight=1)


# Adresse IP et numéro de port du serveur
HOST = '127.0.0.1'
PORT = 18023

# Création de la socket du client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Demande de connexion au serveur
client_socket.connect((HOST, PORT))

clef_session = [random.randint(0, 15), random.randint(0, 15)]
rsa_p = [0,0]

message_recu = 0

v = 141

def rsa(message, clef):
    return pow(message, clef[0], clef[1])

# Fonction qui permet d'envoyer les messages au serveur
def envoyer_message(message):
    global message_recu
    global clef_session
    global v
    
    if message_recu == 1:
        client_socket.send(message.encode())
        message_recu = 2
    else :
        print("Client 1 :", message)
        message = chiffrement.enc_texte_cbc(clef_session, message, v)
        client_socket.send(message.encode())
        #message = input("Entrez votre message : ")
        #client_socket.send(message.encode())
        
#initialisation de chatInterface afin de récupérer le message
chat_interface = projet.ChatInterface(root, envoyer_message)


# Fonction qui permet de recevoir les messages du serveur
def recevoir_messages():
    global message_recu
    global rsa_p
    global clef_session
    global v

    while True:
        message = client_socket.recv(1024).decode()

        message_recu += 1

        if message_recu == 1:
            mess = message.strip('()')
            mess = mess.split(',')
            rsa_p[0] = int(mess[0])
            rsa_p[1] = int(mess[1])
            mess = "(" + str(rsa(clef_session[0], rsa_p)) + "," + str(rsa(clef_session[1], rsa_p)) + ")"
            envoyer_message(mess)
            #print("c1 session:", clef_session)

        else :
            message = chiffrement.dec_texte_cbc(clef_session, message, v)
            print("Client 2 :", message)
            chat_interface.nouveau_message(message) #envoie le message reçus a projet
            if message == "quitter":
                chat_interface.quitte_chat() #lance quitte_chat de projet
                client_socket.close()
                break


# Création des threads pour l'envoi et la réception de messages
recevoir_thread = threading.Thread(target=recevoir_messages)

# Démarrage des threads
recevoir_thread.start()

# Attente de la fin des threads
root.mainloop()
recevoir_thread.join()


