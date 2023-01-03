def triangle(a, b, c):

    #on vérifie si triangle possible
    if a + b <= c or a + c <= b or b + c <= a:
        return "impossible de faire un triangle"

    #pour savoir si il équilatéral 
    if a == b and b == c:
        return "triangle equilatéral"

    #pour savoir si il est a la fois isocèle et rectangle, il est important de mettre cette condition avant les suivantes pour qu'elle soit bien prise en compte
    if a == b or a == c or b == c and (a*a + b*b  == c*c or c*c + b*b == a*a or a*a + c*c == b*b):
        return "triangle isocèle et rectangle "

    #si le triangle est rectangle
    if a*a + b*b  == c*c or c*c + b*b == a*a or a*a + c*c == b*b:
        return "triangle rectangle"
   
    #si il est  seulement isocèle
    if a == b or a == c or b == c:
        return "triangle isocèle"

    #autres triangles 
    else:
        return "triangle quelconque"



print(triangle(2, 3, 3)) # "triangle isocèle "
print(triangle(5, 5, 7)) # "triangle isocèle et rectangle"
print(triangle(3, 4, 5)) # "triangle rectangle"
print(triangle(3, 3, 3)) # "triangle equilatéral"
print(triangle(2, 3, 4)) # "triangle quelconque"
print(triangle(1, 2, 3)) # "impossible de faire un triangle"
