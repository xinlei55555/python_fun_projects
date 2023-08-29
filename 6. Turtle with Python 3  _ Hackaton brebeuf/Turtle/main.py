import turtle
import random

name = turtle.Turtle()

#changes the background color
turtle.Screen().bgcolor('black')



#changes his speed
name.speed(0)


#changes the color of the turtle itself
name.color('white')

#makes him move in the direction
name.forward(150)

couleur = ('white', 'yellow', 'orange', 'red', 'green', 'blue', 'purple', 'grey', 'black') # couleurs possibles
nombre_couleur = len(couleur) # donne le nombre d'éléments dans la liste couleur


for o in range(0,1000):
  c = random.randint(0,nombre_couleur-1) # on choisit un nombre aléatoire entre 0 et le len(nombre_couleur)
 
  name.color(couleur[c]) # on modifie le crayon pour la couleur aléatoire

  #we should give an angle here, il faut toujours tourner de l'angle exterieur, a.k.a l'angle teta en sciences
  name.left(91)
    #we must give a number of pixels
  name.forward(150)
  
  print(o)