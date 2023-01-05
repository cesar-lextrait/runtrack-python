def intervall():
    liste = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
    somme = 0
    for i in liste:
        if i >= 25 and i <= 90: 
            somme = somme + i
    print(somme)
intervall()