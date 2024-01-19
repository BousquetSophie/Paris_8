# -*- coding: utf-8 -*-

import tkinter as tk
import basic_functions as bf

class calculatrice :
    
    def __init__(self):
        
        self.fen = tk.Tk()
        self.fen.title("Calculatrice")
        self.fen.geometry("370x315")
        self.fen["bg"]= "SkyBlue2" # Coleur de la fenêtre
        self.fen["relief"] = "raised" # Profondeur de la fenêtre
        self.entry = tk.StringVar()
        self.entry.set("Write your equation :")
        
        self.calcul = ""
        
        self.ecran = tk.Entry(self.fen, width=28, textvariable=self.entry, bg ="black", fg="white", relief="sunken", bd=5).place(x=9, y=8)
        
        self.zero = tk.Button(self.fen, text="0", command=self.button0, width=3, height=2, bg="grey", fg="white").place(x=50, y=190)
        self.one = tk.Button(self.fen, text="1", command=self.button1, width=3, height=2, bg="grey", fg="white").place(x=10, y=40)
        self.two = tk.Button(self.fen, text="2", command=self.button2, width=3, height=2, bg="grey", fg="white").place(x=50, y=40)
        self.three = tk.Button(self.fen, text="3", command=self.button3, width=3, height=2, bg="grey", fg="white").place(x=90, y=40)
        self.four = tk.Button(self.fen, text="4", command=self.button4, width=3, height=2, bg="grey", fg="white").place(x=10, y=90)
        self.five = tk.Button(self.fen, text="5", command=self.button5, width=3, height=2, bg="grey", fg="white").place(x=50, y=90)
        self.six = tk.Button(self.fen, text="6", command=self.button6, width=3, height=2, bg="grey", fg="white").place(x=90, y=90)
        self.seven = tk.Button(self.fen, text="7", command=self.button7, width=3, height=2, bg="grey", fg="white").place(x=10, y=140)
        self.eight = tk.Button(self.fen, text="8", command=self.button8, width=3, height=2, bg="grey", fg="white").place(x=50, y=140)
        self.nine = tk.Button(self.fen, text="9", command=self.button9, width=3, height=2, bg="grey", fg="white").place(x=90, y=140)
        self.point = tk.Button(self.fen, text=".", command=self.buttonPoint, width=3, height=2, bg="grey", fg="white").place(x=10, y=190)
        
        self.plus = tk.Button(self.fen, text="+", command=self.buttonPlus, width=3, height=2, bg="grey", fg="white").place(x=130, y=40)
        self.minus = tk.Button(self.fen, text="-", command=self.buttonMinus, width=3, height=2, bg="grey", fg="white").place(x=130, y=90)
        self.multi = tk.Button(self.fen, text="x", command=self.buttonMult, width=3, height=2, bg="grey", fg="white").place(x=130, y=140)
        self.divide = tk.Button(self.fen, text="/", command=self.buttonDiv, width=3, height=2, bg="grey", fg="white").place(x=130, y=190)
        self.power = tk.Button(self.fen, text="pow", command=self.buttonPow, width=3, height=2, bg="grey", fg="white").place(x=130, y=240)
        self.racine2 = tk.Button(self.fen, text="sqr", command=self.buttonPow, width=3, height=2, bg="grey", fg="white").place(x=90, y=240)
        
        self.equal = tk.Button(self.fen, text="=", command=self.equalize, width=3, height=2, bg="grey", fg="white").place(x=90, y=190)
        self.clear = tk.Button(self.fen, text="C", command=self.clear, width=3, height=2, bg="grey", fg="white").place(x=10, y=240)
        
        self.fen.mainloop()
        
    def button0(self):
        self.calcul += "0"
        self.entry.set(self.calcul)
    
    def button1(self):
        self.calcul += "1"
        self.entry.set(self.calcul)
        
    def button2(self):
        self.calcul += "2"
        self.entry.set(self.calcul)
     
    def button3(self):
        self.calcul += "3"
        self.entry.set(self.calcul)
      
    def button4(self):
        self.calcul += "4"
        self.entry.set(self.calcul)
        
    def button5(self):
        self.calcul += "5"
        self.entry.set(self.calcul)
     
    def button6(self):
       self.calcul += "6"
       self.entry.set(self.calcul)
       
    def button7(self):
        self.calcul += "7"
        self.entry.set(self.calcul)
        
    def button8(self):
        self.calcul += "8"
        self.entry.set(self.calcul)
     
    def button9(self):
       self.calcul += "9"
       self.entry.set(self.calcul)
       
    def buttonPoint(self):
        self.calcul += "."
        self.entry.set(self.calcul)
       
    def buttonPlus(self):
       self.calcul += "+"
       self.entry.set(self.calcul)
       
    def buttonMinus(self):
        self.calcul += "-"
        self.entry.set(self.calcul)
        
    def buttonMult(self):
        self.calcul += "x"
        self.entry.set(self.calcul)
     
    def buttonDiv(self):
       self.calcul += "/"
       self.entry.set(self.calcul)
    
    def buttonPow(self):
        self.calcul += "^"
        self.entry.set(self.calcul)
        
    def buttonSqr(self):
        self.calcul += "sqr("
        self.entry.set(self.calcul)
    
    def equalize(self):
        result = bf.operation(self.calcul)
        self.entry.set(result)
        self.calcul = result
    
    def clear(self):
        self.calcul = ""
        self.entry.set("Write your equation :")
        