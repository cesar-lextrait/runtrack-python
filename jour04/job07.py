def multiple3():
    liste = [8, 24, 48, 2, 16]
    compteur = 0 
    for i in liste:
        if i % 3 == 0:
            compteur += 1 
    print(compteur)
multiple3()