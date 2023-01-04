#!/usr/bin/env python3
def pyramid():
  chaine = "abcdefghijklmnopqrstuvwxyz" * 10
  compteur = 0
  for i in range(len(chaine)):  # On parcourt chaque ligne de la pyramide
    for j in range(i + 1): # On parcourt chaque caractère de la ligne courante
      if compteur >= len(chaine): # si le compteur est supérieur à la longueur de la chaîne, on arrête
        break

      
      print(chaine[compteur], end="")# Sinon, on imprime le caractère correspondant à la position du compteur dans la chaîne
     
      compteur += 1 # On incrémente le compteur pour passer au caractère suivant
    print()
pyramid()

