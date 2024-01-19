import tkinter as tk
from datetime import datetime
from PIL import ImageTk, Image

class ChatInterface:
    def __init__(self, master, envoyer_callback, ):
        self.envoyer_callback = envoyer_callback #créer connexion entre client et projet
        self.master = master  # Définition de la fenêtre principale de l'interface

        master.title("Chat")  # Titre de la fenêtre principale
        master.geometry("470x400")


        # Zone d'affichage
        self.affichage_box = tk.Text(master, state='disabled', width=50, height=15)
        self.affichage_box.place(x=25, y=40)

        # Création de la zone de saisie
        self.entree_box = tk.Entry(master, width=65)
        self.entree_box.place(x=25, y=325)

        # Chargement de l'image pour le bouton "Envoyer"
        self.image_envoyer = Image.open("image.png")
        self.image_envoyer = self.image_envoyer.resize((15, 15), Image.ANTIALIAS)
        self.image_envoyer = ImageTk.PhotoImage(self.image_envoyer)

        # Création du bouton "envoyer" avec l'image chargée et redimensionnée
        self.envoie_button = tk.Button(master, image=self.image_envoyer, command=self.envoie_message)
        self.envoie_button.place(x=400, y=325)

        # Bouton "quitter"
        self.quitte_button = tk.Button(master, text="Quitter", command=self.quitte_chat)
        self.quitte_button.grid(row=2, column=0, padx=5, pady=5)
        self.quitte_button.place(x=210, y=360)


        # Lorsque l'utilisateur appuie sur "entrée", le message est envoyé
        self.entree_box.bind('<Return>', self.envoie_message)


    def envoie_message(self, event=None):
        # Récupération du message saisi par l'utilisateur
        message = self.entree_box.get()

        # Suppression du message saisi par l'utilisateur
        self.entree_box.delete(0, 'end')

        # Récupération de la date et l'heure courante
        now = datetime.now()
        timestamp = now.strftime("%d-%m-%Y %H:%M:%S")

        # Affichage du message envoyé dans la zone d'affichage
        self.affichage_box.configure(state='normal')  # Activation de la zone d'affichage
        self.affichage_box.insert('end', f"{timestamp} : {message}\n")  # Affichage du message
        self.affichage_box.configure(state='disabled')  # Désactivation de la zone d'affichage
        self.envoyer_callback(message) #permet de récupérer message dans client

    def nouveau_message(self, message): #permet d'afficher les messages reçus
        now = datetime.now()
        timestamp = now.strftime("%d-%m-%Y %H:%M:%S")

        # Affichage du message envoyé dans la zone d'affichage
        self.affichage_box.configure(state='normal')  # Activation de la zone d'affichage
        self.affichage_box.insert('end', f"{timestamp} : {message}\n")  # Affichage du message
    
    
    def quitte_chat(self):
        # Désactivation de la saisie de nouveaux messages
        self.entree_box.config(state='disabled')
        # Désactivation du bouton "quitter"
        self.quitte_button.config(state='disabled')

        self.envoyer_callback("quitter") #envoie le message quitter a client

        # Affichage d'un message pour indiquer que l'utilisateur a quitté la discussion
        self.affichage_box.configure(state='normal')  # Activation de la zone d'affichage
        self.affichage_box.insert('end', "Le client a quitté la discussion.\n")  # Affichage du message
        self.affichage_box.configure(state='disabled')  # Désactivation de la zone d'affichage

