def print_primes():

    #on parcourt les nombres jusqu'a 100 
    for i in range(2, 1001):
        is_prime = True #condition de vérité si premier
        #pour chaque nombre, on parcourt les nombres de deux 
        for j in range(2, i):
            if i % j == 0:
                is_prime = False # si non premier : divisible par plus que lui même et un 
                break
        if is_prime:
            print(i)
print_primes()
