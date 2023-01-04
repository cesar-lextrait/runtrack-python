def reverse(mot):
    if len(mot) <= 1: #si le mot n'est qu'une lettre ou le retourne directement
        return mot
    return reverse(mot[1:]) + mot[0] #on utilise le slicing pour inverser les lettres en se servant aussi de la la fonction reverse
mot = "anakin"
rev = reverse(mot)
print(rev)  