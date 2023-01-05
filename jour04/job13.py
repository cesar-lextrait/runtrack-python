def doublon():
    liste = [10,20,30,20,10,50,60,40,80,50,40]
    resultat = []
    parcour = []
    for i in liste:
        if i not in parcour:
            resultat = resultat + [i]
            parcour = parcour + [i]
    print(resultat)
doublon()