# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 09:58:59 2019

@author: Nicolas
"""

import turtle as tu
from random import *

# Initialisation du jeu
ts = tu.getscreen()
ts.clear()
ts.bgpic("champcourse2.gif")

ts.title("Bienvenue Ã  la course des tortues !")
ts.setup (width=1400, height=800, startx=0, starty=0)

# DÃ©clarez les 5 tortues et positionnez-les sur leurs hexagones respectifs

Michelangelo = tu.Turtle()
Michelangelo.color('orange')
Michelangelo.shape('turtle')
Michelangelo.penup()
Michelangelo.setposition(-650, 320)
Michelangelo.pendown()

Leonardo = tu.Turtle()
Leonardo.color('Deep Sky Blue')
Leonardo.shape('turtle')
Leonardo.penup()
Leonardo.setposition(-650, 170)
Leonardo.pendown()

Raphael = tu.Turtle()
Raphael.color('red')
Raphael.shape('turtle')
Raphael.penup()
Raphael.setposition(-650, 0)
Raphael.pendown()

Donatello = tu.Turtle()
Donatello.color('purple')
Donatello.shape('turtle')
Donatello.penup()
Donatello.setposition(-650, -150)
Donatello.pendown()

Splinter = tu.Turtle()
Splinter.color('Dark Slate Gray')
Splinter.shape('turtle')
Splinter.penup()
Splinter.setposition(-650, -300)
Splinter.pendown()


# Demander de saisir dans la console les prÃ©dictions des joeurus 1 et 2 dans le format 1,2,3

Player1Pronostics = input("Joueur1, veuillez entrer vos prédictions dans le format 1,2,3 :")
Player2Pronostics = input("Joueur2, veuillez entrer vos prédictions dans le format 1,2,3 :")



# A l'aide d'une boucle while, faire courir les tortues en tirant un nombre entre 0 et 5 qui reprÃ©sente le nombre de pixels du dÃ©placement vers la droite

def turtle_move(tu, dist):
    tu.fd(dist)


Michelangelo_nbr = 0
Leonardo_nbr = 0
Raphael_nbr = 0
Donatello_nbr = 0
Splinter_nbr = 0
Winner = 0
Finish_line = 1380


while Winner == 0:
    shuffle_michel = randint(1, 5)
    shuffle_leonardo = randint(1, 5)
    shuffle_raphael = randint(1, 5)
    shuffle_donatello = randint(1, 5)
    shuffle_splinter = randint(1, 5)
    turtle_move(Michelangelo, shuffle_michel)
    Michelangelo_nbr += shuffle_michel
    turtle_move(Leonardo, shuffle_leonardo)
    Leonardo_nbr += shuffle_leonardo
    turtle_move(Raphael, shuffle_raphael)
    Raphael_nbr += shuffle_raphael
    turtle_move(Donatello, shuffle_donatello)
    Donatello_nbr += shuffle_donatello
    turtle_move(Splinter, shuffle_splinter)
    Splinter_nbr += shuffle_splinter
    
    if(Michelangelo_nbr == Finish_line):
        Michelangelo.penup()
        Leonardo.hideturtle()
        Raphael.hideturtle()
        Donatello.hideturtle()
        Splinter.hideturtle()
        Winner = 1
        Michelangelo.home()
    if(Leonardo_nbr == Finish_line):
        Michelangelo.hideturtle()
        Leonardo.penup()
        Raphael.hideturtle()
        Donatello.hideturtle()
        Splinter.hideturtle()
        Winner = 1
        Leonardo.home()
    if(Raphael_nbr == Finish_line):
        Michelangelo.hideturtle()
        Leonardo.hideturtle()
        Raphael.penup()
        Donatello.hideturtle()
        Splinter.hideturtle()
        Winner = 1
        Raphael.home()
    if(Donatello_nbr == Finish_line):
        Michelangelo.hideturtle()
        Leonardo.hideturtle()
        Raphael.hideturtle()
        Donatello.penup()
        Splinter.hideturtle()
        Winner = 1
        Donatello.home()
    if(Splinter_nbr == Finish_line):
        Michelangelo.hideturtle()
        Leonardo.hideturtle()
        Raphael.hideturtle()
        Donatello.hideturtle()
        Splinter.penup()
        Winner = 1
        
        Splinter.home()
    


turtle_arbitre = tu.Turtle()
turtle_arbitre.goto(0,0)
turtle_arbitre.color("Black")
turtle_arbitre.write("Le joueur 1 Ã  gagnÃ©", move=True, align="left", font=("Arial", 16, "normal"))



tu.mainloop()

Michelangelo.done()
Leonardo.done()
Raphael.done()
Donatello.done()
Splinter.done()