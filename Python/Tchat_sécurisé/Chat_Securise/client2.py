import socket
import threading
import tkinter as tk
import projet
from PIL import ImageTk, Image
from Crypto.Util import number
import chiffrement

#Charger l'interface depuis client
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

clef_session = [0,0]

message_envoyer = 0

v = 141

def gen_rsa_keypair(taille):

    p = number.getPrime(taille//2)
    q = number.getPrime(taille//2)

    n = p*q
    phiN = (p-1)*(q-1)

    e = 65537
    assert(phiN%e!=0)

    d = pow(e, -1, phiN)
    
    return ([e,n], [d,n])

public, privee = gen_rsa_keypair(512)

def rsa(message, clef):
    return pow(message, clef[0], clef[1])

# Fonction qui permet d'envoyer les messages au serveur
def envoyer_message(message):
    global message_envoyer
    global clef_session
    global v
    
    if message_envoyer == 0:
        client_socket.send(message.encode())
    else :
        print("Client 2 :", message)
        message = chiffrement.enc_texte_cbc(clef_session, message, v)
        client_socket.send(message.encode())
        #message = input("Entrez votre message : ")
        #client_socket.send(message.encode())

#instance de chatInterface afin de récupérer le message    
chat_interface = projet.ChatInterface(root, envoyer_message) 


# Fonction qui permet de recevoir les messages du serveur
def recevoir_messages():
    global message_envoyer
    global clef_session
    
    while True:
        message = client_socket.recv(1024).decode()

        if(message_envoyer == 1) :
            mess = message.strip('()')
            mess = mess.split(',')
            clef_session[0] = rsa(int(mess[0]), privee)
            clef_session[1] = rsa(int(mess[1]), privee)
            message_envoyer = 2
            #print("c2 session:", clef_session)

        else :
            message = chiffrement.dec_texte_cbc(clef_session, message, v)
            print("Client 1 :", message)
            chat_interface.nouveau_message(message) #envoie le message reçus a projet
            if message == "quitter":
                chat_interface.quitte_chat() #lance quitte_chat de projet
                client_socket.close()
                break


# Création des threads pour l'envoi et la réception de messages
recevoir_thread = threading.Thread(target=recevoir_messages)

# Démarrage des threads
recevoir_thread.start()

# Envoie de la clef publique
if message_envoyer == 0:
    mess = "(" + str(public[0]) + "," + str(public[1]) + ")"
    envoyer_message(mess)
    message_envoyer = 1

# Attente de la fin des threads
root.mainloop()
recevoir_thread.join()

