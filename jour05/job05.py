def phare(nbmarche, htmarche):
    taille = htmarche * 0.01
    distance  = nbmarche*taille
    semaine = 0
    for i in range(7):
        semaine += distance 
    print("Pour", nbmarche, "marches de", htmarche, "cm, le gardien parcourt", semaine, "m par semaine")
phare(39, 25)
phare(23, 32)