
def paires():
    liste = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
    somme = 0
    for i in liste:
        if i % 2 == 0:
            somme = somme + i 
    return somme 
print(paires())
