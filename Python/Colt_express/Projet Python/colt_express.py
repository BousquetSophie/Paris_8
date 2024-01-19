from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from PIL import Image, ImageTk
from random import *
import pygame
import liste

class Jeu(Tk) :
	def __init__(self):
		super().__init__()
		
		#images du jeu
        #image fond
		self.fond=Image.open("Fond.jpg")
		resized = self.fond.resize((1916,1075))
		self.fond=ImageTk.PhotoImage(resized)

		self.page1 = Label(self, image=self.fond)
		self.page1.place(x=0,y=0)

		#image wagon
#		self.wagon=Image.open("train.jpg")
#		resized = self.wagon.resize((1700,400))
#		self.wagon=ImageTk.PhotoImage(resized)

#		self.page2 = Label(self, image= self.wagon)
#		self.page2.place(x=100,y=580)
		
		#Planification
		Planification = Label(self, text="PLANIFICATION :")
		Planification.place(x=100,y=20)
		
		#Planification tours
		
		planification_tour = Label(self, text="Nb de tour :")
		planification_tour.place(x=20,y=50)
		
		self.nb_joueurs = 4
		self.nb_wagons = 4
		self.nb_actions = 4
		self.nb_tours = 5
		
		#Actions stockées
		self.actions_joueur1=[]
		self.actions_joueur2=[]
		self.actions_joueur3=[]
		self.actions_joueur4=[]
		
		self.joueur_actuel = 1
		self.tour_actuel = 1
		
		#wagon stockées
		self.wagon_actuel_joueur1 = 1
		self.wagon_actuel_joueur2 = 1
		self.wagon_actuel_joueur3 = 1
		self.wagon_actuel_joueur4 = 1
		self.wagon_actuel_marshall = 9
		
		self.magot = 1000 #Magot (1000): a l'interieur de la locomotive avec le marchall
		self.bijou = 500 #bijoux (500) : auprès des passagers
		self.bourse = 100 #bourse (100 ou 200) : auprès des passagers
		
		e_tour = Entry(self).place(x=100,y=50)
		
#		nb_tour= e_tour.get()
		
		if self.tour_actuel > self.nb_tours :
			print("Fin du Jeu")
			#afficher les résultats 
			
		self.profil()
		
		#image joueur
		
		self.personnage1=Image.open("perso1.png")
		perso1 = self.personnage1.resize((50,50))
		self.personnage1=ImageTk.PhotoImage(perso1)
		
		self.personnage2=Image.open("perso2.jpeg")
		perso2 = self.personnage2.resize((50,50))
		self.personnage2=ImageTk.PhotoImage(perso2)
		
		self.personnage3=Image.open("perso3.png")
		perso3 = self.personnage3.resize((50,50))
		self.personnage3=ImageTk.PhotoImage(perso3)
		
		self.personnage4=Image.open("perso4.jpeg")
		perso4 = self.personnage4.resize((50,50))
		self.personnage4=ImageTk.PhotoImage(perso4)
		
		self.marshall=Image.open("marshall.jpg")
		marsh = self.marshall.resize((50,50))
		self.marshall=ImageTk.PhotoImage(marsh)
		
		self.p1 = Label(self, image = self.personnage1)
		self.p1.place(x=70, y=950)
		
		self.p2 = Label(self, image = self.personnage2)
		self.p2.place(x=120, y=950)
		
		self.p3 = Label(self, image = self.personnage3)
		self.p3.place(x=170, y=950)
		
		self.p4 = Label(self, image = self.personnage4)
		self.p4.place(x=220, y=950)
		
		self.p5 = Label(self, image = self.marshall)
		self.p5.place(x=1680, y=850)
				
		# Boutton valider
		
		btn_valider = Button(self,text = "Valider", command=self.valider)
		btn_valider.place(x=100, y=200)
		
		# Bouton action
		
		self.btn_action = Button(self, text="Actions", command=self.action_exe)
		self.btn_action.place(x=100, y=230)
		
	
	def valider(self):
		
		self.recup_action()
		self.action_joueur()
		
		
		if self.joueur_actuel >= self.nb_joueurs :
			# cacher planification
			self.joueur_actuel = 1
		else :
			self.joueur_actuel +=1
			
		#image du joueur actuel
		self.profil()
			
		listeCombo1.current(0)
		listeCombo2.current(0)
		listeCombo3.current(0)
		listeCombo4.current(0)

	def profil(self):
		
		#profil joueurs
		self.joueur1=Image.open("joueur1.jpg")
		resized = self.joueur1.resize((100,100))
		self.joueur1=ImageTk.PhotoImage(resized)
		
		self.joueur2=Image.open("joueur2.jpg")
		resized = self.joueur2.resize((100,100))
		self.joueur2=ImageTk.PhotoImage(resized)
		
		self.joueur3=Image.open("joueur3.jpg")
		resized = self.joueur3.resize((100,100))
		self.joueur3=ImageTk.PhotoImage(resized)
		
		self.joueur4=Image.open("joueur4.jpg")
		resized = self.joueur4.resize((100,100))
		self.joueur4=ImageTk.PhotoImage(resized)
		
		self.img = self.joueur1
		
		if self.joueur_actuel ==1:
			self.img = self.joueur1
		elif self.joueur_actuel ==2:
			self.img = self.joueur2
		elif self.joueur_actuel ==3:
			self.img = self.joueur3
		elif self.joueur_actuel ==4:
			self.img = self.joueur4
		
		self.page2 = Label(self, image=self.img)
		self.page2.place(x=300,y=0)
		
			
	def pos_joueur(self):
		#positionnement image joueur
		
		if self.joueur_actuel == 1:
			if self.wagon_actuel_joueur1 == 1:
				self.p1.place(x=70, y=950)
			elif self.wagon_actuel_joueur1 == 2:
				self.p1.place(x=400, y=950)
			elif self.wagon_actuel_joueur1 == 3:
				self.p1.place(x=720, y=950)
			elif self.wagon_actuel_joueur1 == 4:
				self.p1.place(x=1060, y=950)
			elif self.wagon_actuel_joueur1 == 5:
				self.p1.place(x=70, y=780)
			elif self.wagon_actuel_joueur1 == 6:
				self.p1.place(x=400, y=780)
			elif self.wagon_actuel_joueur1 == 7:
				self.p1.place(x=720, y=780)
			elif self.wagon_actuel_joueur1 == 8:
				self.p1.place(x=1060, y=780)
			elif self.wagon_actuel_joueur1 == 9:
				self.p1.place(x=1400, y=850)
				
		elif self.joueur_actuel == 2:
			if self.wagon_actuel_joueur2 == 1:
				self.p2.place(x=120, y=950)
			elif self.wagon_actuel_joueur2 == 2:
				self.p2.place(x=450, y=950)
			elif self.wagon_actuel_joueur2 == 3:
				self.p2.place(x=770, y=950)
			elif self.wagon_actuel_joueur2 == 4:
				self.p2.place(x=1110, y=950)
			elif self.wagon_actuel_joueur2 == 5:
				self.p2.place(x=120, y=780)
			elif self.wagon_actuel_joueur2 == 6:
				self.p2.place(x=400, y=780)
			elif self.wagon_actuel_joueur2 == 7:
				self.p2.place(x=770, y=780)
			elif self.wagon_actuel_joueur2 == 8:
				self.p2.place(x=1110, y=780)
			elif self.wagon_actuel_joueur2 == 9:
				self.p2.place(x=1450, y=850)
				
		elif self.joueur_actuel == 3:
			if self.wagon_actuel_joueur3 == 1:
				self.p3.place(x=170, y=950)
			elif self.wagon_actuel_joueur3 == 2:
				self.p3.place(x=500, y=950)
			elif self.wagon_actuel_joueur3 == 3:
				self.p3.place(x=820, y=950)
			elif self.wagon_actuel_joueur3 == 4:
				self.p3.place(x=1160, y=950)
			elif self.wagon_actuel_joueur3 == 5:
				self.p3.place(x=170, y=780)
			elif self.wagon_actuel_joueur3 == 6:
				self.p3.place(x=450, y=780)
			elif self.wagon_actuel_joueur3 == 7:
				self.p3.place(x=820, y=780)
			elif self.wagon_actuel_joueur3 == 8:
				self.p3.place(x=1160, y=780)
			elif self.wagon_actuel_joueur3 == 9:
				self.p3.place(x=1500, y=850)
		
		elif self.joueur_actuel == 4:
			if self.wagon_actuel_joueur4 == 1:
				self.p4.place(x=220, y=950)
			elif self.wagon_actuel_joueur4 == 2:
				self.p4.place(x=550, y=950)
			elif self.wagon_actuel_joueur4 == 3:
				self.p4.place(x=870, y=950)
			elif self.wagon_actuel_joueur4 == 4:
				self.p4.place(x=1210, y=950)
			elif self.wagon_actuel_joueur4 == 5:
				self.p4.place(x=220, y=780)
			elif self.wagon_actuel_joueur4 == 6:
				self.p4.place(x=500, y=780)
			elif self.wagon_actuel_joueur4 == 7:
				self.p4.place(x=870, y=780)
			elif self.wagon_actuel_joueur4 == 8:
				self.p4.place(x=1210, y=780)
			elif self.wagon_actuel_joueur4 == 9:
				self.p4.place(x=1650, y=850)
				
	def pos_marshall(self):
		#position marshall	
		if self.wagon_actuel_marshall == 1:
				self.p5.place(x=250, y=950)
		elif self.wagon_actuel_marshall == 2:
				self.p5.place(x=530, y=950)
		elif self.wagon_actuel_marshall == 3:
				self.p5.place(x=900, y=950)
		elif self.wagon_actuel_marshall == 4:
				self.p5.place(x=1220, y=950)
		elif self.wagon_actuel_marshall == 9:
				self.p5.place(x=1700, y=850)
				
	def recup_action(event):
	
		liste.Actions = []

		Choix1 = listeCombo1.get()
		liste.Actions.append(Choix1)
#		print("Première action : ", Choix1)
		
		Choix2 = listeCombo2.get()
		liste.Actions.append(Choix2)
#		print("Deuxième action : ", Choix2)
		
		Choix3 = listeCombo3.get()
		liste.Actions.append(Choix3)
#		print("Troisième action : ", Choix3)
		
		Choix4 = listeCombo4.get()
		liste.Actions.append(Choix4)
#		print("Quatrième action : ", Choix4)
	
	def action_joueur(self):
		
		if self.joueur_actuel == 1:
			self.action_joueur1 = liste.Actions
#			print("1")
#			print(self.action_joueur1)
		
		elif self.joueur_actuel == 2:
			self.action_joueur2 = liste.Actions
#			print("2")
#			print(self.action_joueur2)
		
		elif self.joueur_actuel == 3:
			self.action_joueur3 = liste.Actions
#			print("3")
#			print(self.action_joueur3)
			
		elif self.joueur_actuel == 4:
			self.action_joueur4 = liste.Actions
#			print("4")
#			print(self.action_joueur4)
			
		else:
			print("Erreur")

	def action_exe(self):				
			
		if self.joueur_actuel == 1 :
			if self.action_joueur1[0] == "Avancer" :
				self.avancer()
			elif self.action_joueur1[0] == "Reculer" :
				self.reculer()
			elif self.action_joueur1[0] == "Haut" :
				self.haut()
			elif self.action_joueur1[0] == "Bas" :
				self.bas()
			elif self.action_joueur1[0] == "Tir" :
				self.tir()
			elif self.action_joueur1[0] == "Braquer" :
				self.braquer()
				
			del self.action_joueur1[0]
			
		elif self.joueur_actuel == 2 :
			if self.action_joueur2[0] == "Avancer" :
				self.avancer()
			elif self.action_joueur2[0] == "Reculer" :
				self.reculer()
			elif self.action_joueur2[0] == "Haut" :
				self.haut()
			elif self.action_joueur2[0] == "Bas" :
				self.bas()
			elif self.action_joueur2[0] == "Tir" :
				self.tir()
			elif self.action_joueur2[0] == "Braquer" :
				self.braquer()
			
			del self.action_joueur2[0]
				
		elif self.joueur_actuel == 3 :
			if self.action_joueur3[0] == "Avancer" :
				self.avancer()
			elif self.action_joueur3[0] == "Reculer" :
				self.reculer()
			elif self.action_joueur3[0] == "Haut" :
				self.haut()
			elif self.action_joueur3[0] == "Bas" :
				self.bas()
			elif self.action_joueur3[0] == "Tir" :
				self.tir()
			elif self.action_joueur3[0] == "Braquer" :
				self.braquer()
				
			del self.action_joueur3[0]
			
		elif self.joueur_actuel == 4 :
			if self.action_joueur4[0] == "Avancer" :
				self.avancer()
			elif self.action_joueur4[0] == "Reculer" :
				self.reculer()
			elif self.action_joueur4[0] == "Haut" :
				self.haut()
			elif self.action_joueur4[0] == "Bas" :
				self.bas()
			elif self.action_joueur4[0] == "Tir" :
				self.tir()
			elif self.action_joueur4[0] == "Braquer" :
				self.braquer()
				
			del self.action_joueur4[0]
			
#		print("joueur")
#		print(self.joueur_actuel)	
#		print("")
#		print(self.wagon_actuel_joueur1)
#		print(self.wagon_actuel_joueur2)
#		print(self.wagon_actuel_joueur3)
#		print(self.wagon_actuel_joueur4)
#		print("marshall")
#		print(self.wagon_actuel_marshall)
		
		
		#position des joueur
		self.pos_joueur()
		
		# a chaque action d'un joueur, le marshall ce déplace
		self.deplacement_marshall()
		
		#position du marshall
		self.pos_marshall()
		
		# si le joueur croise le marshall
		self.lacheButtin()
		
		if self.joueur_actuel >= self.nb_joueurs :
			self.joueur_actuel = 1
			
		else:
			self.joueur_actuel+=1
		
		#image du joueur actuel
		self.profil()
		
		if self.action_joueur4 == [] and self.action_joueur3 == [] and self.action_joueur2 == [] and self.action_joueur1 == [] :
		
			self.tour_actuel +=1

		
# Fonction des actions :
	# fonctionnement des déplacements :
		#1,2,3,4 pour l'interrieur des wagons
		#5,6,7,8 pour le toit 
		#9 pour la locomotive

	def avancer (self):
		if self.joueur_actuel == 1 :
			if self.wagon_actuel_joueur1 == 4:
				self.wagon_actuel_joueur1 = 9
			elif self.wagon_actuel_joueur1 == 8:
				pass
			elif self.wagon_actuel_joueur1 == 9:
				pass
			else : 
				self.wagon_actuel_joueur1 +=1
		
		elif self.joueur_actuel == 2 :
			if self.wagon_actuel_joueur2 == 4:
				self.wagon_actuel_joueur2 = 9
			elif self.wagon_actuel_joueur2 == 8:
				pass
			elif self.wagon_actuel_joueur2 == 9:
				pass
			else : 
				self.wagon_actuel_joueur2 +=1
		
		elif self.joueur_actuel == 3 :
			if self.wagon_actuel_joueur3 == 4:
				self.wagon_actuel_joueur3 = 9
			elif self.wagon_actuel_joueur3 == 8:
				pass
			elif self.wagon_actuel_joueur3 == 9:
				pass
			else : 
				self.wagon_actuel_joueur3 +=1
		
		elif self.joueur_actuel == 4 :
			if self.wagon_actuel_joueur4 == 4:
				self.wagon_actuel_joueur4 = 9
			elif self.wagon_actuel_joueur4 == 8:
				pass
			elif self.wagon_actuel_joueur4 == 9:
				pass
			else : 
				self.wagon_actuel_joueur4 +=1
		else:
			pass
	
	def reculer (self):
		if self.joueur_actuel == 1 :
			if self.wagon_actuel_joueur1 == 1:
				pass
			elif self.wagon_actuel_joueur1 == 5:
				pass
			elif self.wagon_actuel_joueur1 == 9:
				self.wagon_actuel_joueur1 = 4
			else:
				self.wagon_actuel_joueur1 -=1
			
		elif self.joueur_actuel == 2 :
			if self.wagon_actuel_joueur2 == 1:
				pass
			elif self.wagon_actuel_joueur2 == 5:
				pass
			elif self.wagon_actuel_joueur2 == 9:
				self.wagon_actuel_joueur2 = 4
			else:
				self.wagon_actuel_joueur2 -=1
			
		elif self.joueur_actuel == 3 :
			if self.wagon_actuel_joueur3 == 1:
				pass
			elif self.wagon_actuel_joueur3 == 5:
				pass
			elif self.wagon_actuel_joueur3 == 9:
				self.wagon_actuel_joueur3 = 4
			else:
				self.wagon_actuel_joueur3 -=1
				
		elif self.joueur_actuel == 4 :
			if self.wagon_actuel_joueur4 == 1:
				pass
			elif self.wagon_actuel_joueur4 == 5:
				pass
			elif self.wagon_actuel_joueur4 == 9:
				self.wagon_actuel_joueur4 = 4
			else:
				self.wagon_actuel_joueur4 -=1
		else:
			pass
		
	def haut (self):
		if self.joueur_actuel == 1 :
			if self.wagon_actuel_joueur1 == 1:
				self.wagon_actuel_joueur1 = 5
			
			elif self.wagon_actuel_joueur1 == 2:
				self.wagon_actuel_joueur1 = 6
			
			elif self.wagon_actuel_joueur1 == 3:
				self.wagon_actuel_joueur1 = 7
			
			elif self.wagon_actuel_joueur1 == 4:
				self.wagon_actuel_joueur1 = 8
			else:
				pass
		elif self.joueur_actuel == 2 :
			if self.wagon_actuel_joueur2 == 1:
				self.wagon_actuel_joueur2 = 5
			
			elif self.wagon_actuel_joueur2 == 2:
				self.wagon_actuel_joueur2 = 6
			
			elif self.wagon_actuel_joueur2 == 3:
				self.wagon_actuel_joueur2 = 7
			
			elif self.wagon_actuel_joueur2 == 4:
				self.wagon_actuel_joueur2 = 8
			else:
				pass
			
		elif self.joueur_actuel == 3 :
			if self.wagon_actuel_joueur3 == 1:
				self.wagon_actuel_joueur3 = 5
			
			elif self.wagon_actuel_joueur3 == 2:
				self.wagon_actuel_joueur3 = 6
			
			elif self.wagon_actuel_joueur3 == 3:
				self.wagon_actuel_joueur3 = 7
			
			elif self.wagon_actuel_joueur3 == 4:
				self.wagon_actuel_joueur3 = 8
			else:
				pass
		
		elif self.joueur_actuel == 4 :
			if self.wagon_actuel_joueur4 == 1:
				self.wagon_actuel_joueur4 = 5
			
			elif self.wagon_actuel_joueur4 == 2:
				self.wagon_actuel_joueur4 = 6
			
			elif self.wagon_actuel_joueur4 == 3:
				self.wagon_actuel_joueur4 = 7
			
			elif self.wagon_actuel_joueur4 == 4:
				self.wagon_actuel_joueur4 = 8
			else:
				pass
		
	def bas (self):
		if self.joueur_actuel == 1 :
			if self.wagon_actuel_joueur1 == 5:
				self.wagon_actuel_joueur1 = 1
			
			elif self.wagon_actuel_joueur1 == 6:
				self.wagon_actuel_joueur1 = 2
			
			elif self.wagon_actuel_joueur1 == 7:
				self.wagon_actuel_joueur1 = 3
			
			elif self.wagon_actuel_joueur1 == 8:
				self.wagon_actuel_joueur1 = 4
			else:
				pass
		elif self.joueur_actuel == 2 :
			if self.wagon_actuel_joueur2 == 5:
				self.wagon_actuel_joueur2 = 1
			
			elif self.wagon_actuel_joueur2 == 6:
				self.wagon_actuel_joueur2 = 2
			
			elif self.wagon_actuel_joueur2 == 7:
				self.wagon_actuel_joueur2 = 3
			
			elif self.wagon_actuel_joueur2 == 8:
				self.wagon_actuel_joueur2 = 4
			else:
				pass
			
		elif self.joueur_actuel == 3 :
			if self.wagon_actuel_joueur3 == 5:
				self.wagon_actuel_joueur3 = 1
			
			elif self.wagon_actuel_joueur3 == 6:
				self.wagon_actuel_joueur3 = 2
			
			elif self.wagon_actuel_joueur3 == 7:
				self.wagon_actuel_joueur3 = 3
			
			elif self.wagon_actuel_joueur3 == 8:
				self.wagon_actuel_joueur3 = 4
			else:
				pass
		
		elif self.joueur_actuel == 4 :
			if self.wagon_actuel_joueur4 == 5:
				self.wagon_actuel_joueur4 = 1
			
			elif self.wagon_actuel_joueur4 == 6:
				self.wagon_actuel_joueur4 = 2
			
			elif self.wagon_actuel_joueur4 == 7:
				self.wagon_actuel_joueur4 = 3
			
			elif self.wagon_actuel_joueur4 == 8:
				self.wagon_actuel_joueur4 = 4
			else:
				pass
		
	def tir(self): #si un joueur est dans le wagon il lui tire dessu pour récup un de ses magot
		print("tir")
		pass
		
#		if self.joueur_actuel == 1 :
#			if self.wagon_actuel_joueur1 == self.wagon_actuel_joueur2:
#				liste.butin_joueur1.append(liste.butin_joueur2[0])
#				del liste.butin_joueur2[0]
#				print("tir")
#			elif self.wagon_actuel_joueur1 == self.wagon_actuel_joueur3:
#				liste.butin_joueur1.append(liste.butin_joueur3[0])
#				del liste.butin_joueur3[0]
#			elif self.wagon_actuel_joueur1 == self.wagon_actuel_joueur4:
#				liste.butin_joueur1.append(liste.butin_joueur4[0])
#				del liste.butin_joueur4[0]
#			else :
#				pass

#		elif self.joueur_actuel == 2 :
#			if self.wagon_actuel_joueur2 == self.wagon_actuel_joueur1:
#				liste.butin_joueur2.append(liste.butin_joueur1[0])
#				del liste.butin_joueur1[0]
#			elif self.wagon_actuel_joueur2 == self.wagon_actuel_joueur3:
#				liste.butin_joueur2.append(liste.butin_joueur3[0])
#				del liste.butin_joueur3[0]
#			elif self.wagon_actuel_joueur2 == self.wagon_actuel_joueur4:
#				liste.butin_joueur2.append(liste.butin_joueur4[0])
#				del liste.butin_joueur4[0]
#			else :
#				pass

#		elif self.joueur_actuel == 3 :
#			if self.wagon_actuel_joueur3 == self.wagon_actuel_joueur1:
#				liste.butin_joueur3.append(liste.butin_joueur1[0])
#				del liste.butin_joueur1[0]
#			elif self.wagon_actuel_joueur3 == self.wagon_actuel_joueur2:
#				liste.butin_joueur3.append(liste.butin_joueur2[0])
#				del liste.butin_joueur2[0]
#			elif self.wagon_actuel_joueur3 == self.wagon_actuel_joueur4:
#				liste.butin_joueur3.append(liste.butin_joueur4[0])
#				del liste.butin_joueur4[0]
#			else :
#				pass

#		elif self.joueur_actuel == 4 :
#			if self.wagon_actuel_joueur4 == self.wagon_actuel_joueur1:
#				liste.butin_joueur4.append(liste.butin_joueur1[0])
#				del liste.butin_joueur1[0]
#			elif self.wagon_actuel_joueur4 == self.wagon_actuel_joueur2:
#				liste.butin_joueur4.append(liste.butin_joueur2[0])
#				del liste.butin_joueur2[0]
#			elif self.wagon_actuel_joueur4 == self.wagon_actuel_joueur3:
#				liste.butin_joueur4.append(liste.butin_joueur3[0])
#				del liste.butin_joueur3[0]
#			else :
#				pass
	
	def braquer(self):
		print("braquer")
		#récup un butin d'une personne (pnj) parmis celle dans le wagon
	
	# action que l'on fait lorsque l'on croise le marchall
	
	def lacheButtin(self):
		pass
		
		if self.wagon_actuel_joueur1 == self.wagon_actuel_marshall:
#			liste.butin_joueur1[0]
			self.fuit()
			
		if self.wagon_actuel_joueur2 == self.wagon_actuel_marshall:
#			liste.butin_joueur2[0]
			self.fuit()
			
		if self.wagon_actuel_joueur3 == self.wagon_actuel_marshall:
#			liste.butin_joueur3[0]
			self.fuit()
			
		if self.wagon_actuel_joueur4 == self.wagon_actuel_marshall:
#			liste.butin_joueur4[0]
			self.fuit()
		
	def fuit(self):
		if self.wagon_actuel_joueur1 == 1:
			self.wagon_actuel_joueur1 = 5
			
		elif self.wagon_actuel_joueur1 == 2:
			self.wagon_actuel_joueur1 = 6
			
		elif self.wagon_actuel_joueur1 == 3:
			self.wagon_actuel_joueur1 = 7
			
		elif self.wagon_actuel_joueur1 == 4:
			self.wagon_actuel_joueur1 = 8
		else:
				pass
				
		if self.wagon_actuel_joueur2 == 1:
			self.wagon_actuel_joueur2 = 5
			
		elif self.wagon_actuel_joueur2 == 2:
			self.wagon_actuel_joueur2 = 6
			
		elif self.wagon_actuel_joueur2 == 3:
			self.wagon_actuel_joueur2 = 7
			
		elif self.wagon_actuel_joueur2 == 4:
			self.wagon_actuel_joueur2 = 8
		else:
				pass
			
		if self.wagon_actuel_joueur3 == 1:
			self.wagon_actuel_joueur3 = 5
			
		elif self.wagon_actuel_joueur3 == 2:
			self.wagon_actuel_joueur3 = 6
			
		elif self.wagon_actuel_joueur3 == 3:
			self.wagon_actuel_joueur3 = 7
			
		elif self.wagon_actuel_joueur3 == 4:
			self.wagon_actuel_joueur3 = 8
		else:
			pass
		
		if self.wagon_actuel_joueur4 == 1:
			self.wagon_actuel_joueur4 = 5
			
		elif self.wagon_actuel_joueur4 == 2:
			self.wagon_actuel_joueur4 = 6
			
		elif self.wagon_actuel_joueur4 == 3:
			self.wagon_actuel_joueur4 = 7
			
		elif self.wagon_actuel_joueur4 == 4:
			self.wagon_actuel_joueur4 = 8
		else:
			pass
		
	def avancer_marshall(self):
	
		if self.wagon_actuel_marshall == 1:
			pass
		elif self.wagon_actuel_marshall == 9:
			self.wagon_actuel_marshall = 4
		else:
			self.wagon_actuel_marshall -=1
			
	
	def reculer_marshall(self):
	
		if self.wagon_actuel_marshall == 4:
			self.wagon_actuel_marshall = 9
		elif self.wagon_actuel_marshall == 9:
			pass
		else : 
			self.wagon_actuel_marshall +=1
		
		
	def deplacement_marshall(self):
		n = random()
		if n <= 0.5:
			self.reculer_marshall()
		else :
			self.avancer_marshall()
		
#		print(self.wagon_actuel_marshall)
#		print(n)

# Les fenêtres du jeu
#------------------------------------------------

#Son jeu
pygame.mixer.init()

serdaigle= pygame.mixer.Sound("Serdaigle.mp3")


def play1():
	serdaigle.play(-1)
	griffondor.stop()
	poufsouffle.stop()
	serpentard.stop()
    
def stop1():
	serdaigle.stop()


griffondor= pygame.mixer.Sound("Gryffondor.mp3")

def play2():
	griffondor.play(-1)
	serdaigle.stop()
	poufsouffle.stop()
	serpentard.stop()
    
def stop2():
	griffondor.stop()


poufsouffle= pygame.mixer.Sound("Poufsouffle.mp3")

def play3():
	poufsouffle.play(-1)
	serdaigle.stop()
	serpentard.stop()
	griffondor.stop()
    
def stop3():
	poufsouffle.stop()
	

serpentard= pygame.mixer.Sound("Serpentard.mp3")

def play4():
    serpentard.play(-1)
    serdaigle.stop()
    griffondor.stop()
    poufsouffle.stop()
def stop4():
    serpentard.stop()



mon_jeu = Jeu()
mon_jeu.withdraw()
mon_jeu.geometry("1000x1000")
mon_jeu.attributes('-fullscreen', True)


a= Toplevel(mon_jeu)
a.geometry("1000x1000")
a.attributes('-fullscreen', True)

b= Toplevel(mon_jeu)
b.withdraw()
b.geometry("1000x1000")
b.attributes('-fullscreen', True)

mon_jeu.title("Colt Express")
a.title("Colt Express")
b.title("Rules")

#images du jeu
#image menu

img_menu=Image.open("menu.jpeg")
resized = img_menu.resize((1916,1075))
img_menu=ImageTk.PhotoImage(resized)

page1 = Label(a, image=img_menu)
page1.place(x=0,y=0)

frame1 = Frame(a)
frame1.pack(side=RIGHT, padx=15, pady=20)#

#image rules

rules=Image.open("rulesdujeu.jpg")
resized = rules.resize((1916,1075))
rules=ImageTk.PhotoImage(resized)

page1 = Label(b, image=rules)
page1.place(x=0,y=0)

#images du jeu

def lancefen():
    a.withdraw() 
    mon_jeu.deiconify()

def lancefen2():
    a.withdraw() 
    b.deiconify()
    
def switch():
	mon_jeu.withdraw()
	a.deiconify()

def switch2():
    b.withdraw()
    a.deiconify()

#image bouton
play_picture = PhotoImage(file='play1.gif', height=60, width=100)
exit_picture= PhotoImage(file='exit1.gif', height=60, width=100)
rules_picture= PhotoImage(file='rules.gif', height=60, width=100)
menu_picture= PhotoImage(file='menu1.gif', height=60, width=100)

btn_exit = Button(frame1,image=exit_picture, command = mon_jeu.destroy)
btn_exit.pack(pady=10)#

btn_play = Button( frame1, image=play_picture, command=lancefen)
btn_play.pack(padx=20, pady=10)#

btn_rules = Button( frame1, image=rules_picture, command=lancefen2)
btn_rules.pack(pady = 10)#

btn_menu1 = Button(mon_jeu, image=menu_picture, command=switch)
btn_menu1.place(x=1810,y=0)

btn_menu2 = Button(b, image=menu_picture, command=switch2)
btn_menu2.place(x=1810,y=0)

#bouton son

frame = Frame(a)
frame.pack(side=LEFT)

ser = PhotoImage(file='serdaigle.gif', height=50, width=50)
btn_play1 = Button(frame, image=ser, command = play1, width = 30)
btn_play1.pack()

gry = PhotoImage(file='gryffondor.gif', height=50, width=50)
btn_play2 = Button(frame, image=gry, command = play2, width = 30)
btn_play2.pack()

pou = PhotoImage(file='poufsouffle.gif', height=50, width=50)
btn_play3 = Button(frame, image=pou, command = play3, width = 30)
btn_play3.pack()

serp = PhotoImage(file='serpentard.gif', height=50, width=50)
btn_play4 = Button(frame,  image=serp, command = play4, width = 30)
btn_play4.pack()

frame3 = Frame(a)
frame3.pack(side=LEFT)

arr = PhotoImage(file='arrêt.gif', height=50, width=50)
btn_stop1 = Button(frame3, image=arr, command = stop1, width = 30)
btn_stop1.pack()

btn_stop2 = Button(frame3, image=arr, command = stop2, width = 30)
btn_stop2.pack()

btn_stop3 = Button(frame3, image=arr, command = stop3, width = 30)
btn_stop3.pack()

btn_stop4 = Button(frame3, image=arr, command = stop4, width = 30)
btn_stop4.pack()

#------------------------------------------------

# Planification

listeAction=["Tir", "Braquer","Haut","Bas", "Avancer", "Reculer"]
		
# choix de l'action 1 
		
choixAction1 = Label(mon_jeu, text = "Action 1 :")
choixAction1.place(x=20,y=80)
		
listeCombo1 = ttk.Combobox(mon_jeu, values=listeAction)
listeCombo1.current(0)
listeCombo1.bind("<<ComboboxSelected>>", Jeu.recup_action)
listeCombo1.place(x=100,y=80)

# choix de l'action 2
		
choixAction2 = Label(mon_jeu, text = "Action 2 :")
choixAction2.place(x=20,y=110)
		
listeCombo2 = ttk.Combobox(mon_jeu, values=listeAction)
listeCombo2.current(0)
listeCombo2.bind("<<ComboboxSelected>>", Jeu.recup_action)
listeCombo2.place(x=100, y=110)
		
# choix de l'action 3
		
choixAction3 = Label(mon_jeu, text = "Action 3 :")
choixAction3.place(x=20,y=140)
		
listeCombo3 = ttk.Combobox(mon_jeu, values=listeAction)
listeCombo3.current(0)
listeCombo3.bind("<<ComboboxSelected>>", Jeu.recup_action)
listeCombo3.place(x=100,y=140)
		
# choix de l'action 4
		
choixAction4 = Label(mon_jeu, text = "Action 4 :")
choixAction4.place(x=20, y=170)
		
listeCombo4 = ttk.Combobox(mon_jeu, values=listeAction)
listeCombo4.current(0)
listeCombo4.bind("<<ComboboxSelected>>", Jeu.recup_action)
listeCombo4.place(x=100, y=170)

mon_jeu.mainloop()
a.mainloop()
b.mainloop()
