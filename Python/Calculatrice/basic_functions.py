# -*- coding: utf-8 -*-

import math as m

def operation(calcul):
    try :
        if "+" in calcul:
            return addition(calcul)
        elif "-" in calcul:
            return soustraction(calcul)
        elif "x" in calcul:
            return multiplication(calcul)
        elif "/" in calcul:
            return division(calcul)
        elif "^" in calcul:
            return puissance(calcul)
    except :
        return "Error"

def addition(txt):
    nb = txt.split("+")
    nb1 = float(nb[0])
    nb2 = float(nb[1])
    result = nb1 + nb2
    return str(result)

def soustraction(txt):
    nb = txt.split("-")
    nb1 = float(nb[0])
    nb2 = float(nb[1])
    result = nb1 - nb2
    return str(result)

def multiplication(txt):
    nb = txt.split("x")
    nb1 = float(nb[0])
    nb2 = float(nb[1])
    result = nb1 * nb2
    return str(result)

def division(txt):
    nb = txt.split("/")
    nb1 = float(nb[0])
    nb2 = float(nb[1])
    result = nb1 / nb2
    return str(result)

def puissance(txt):
    nb = txt.split("^")
    nombre = 1
    nombre_init = float(nb[0])
    power = int(nb[1])
    for i in range(0, power):
        nombre *= nombre_init
    return nombre

def racineCarree(txt):
    nb=txt.split("(")
    nbr=nb[1]
    nbr_init=nb[1]
    result=pow(nbr, (1/2))
    return result
