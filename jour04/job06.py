def echange(inversr):
    inversr[0], inversr[-1] = inversr[-1], inversr [0]
    return(inversr)

liste = [1, 4, 5, 'zozo']
listeinverse = echange(liste)
print(listeinverse)
