
carre_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 3, 13]]
carre_pas_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 7, 13]]

def afficheCarre(carre):
    """ Affiche la liste à 2 dimensions carre comme un carré"""
    for i in range(len(carre_mag)):
        for j in range(len(carre_mag[i])):
            print(carre_mag[i][j], end=' ')
        print()
afficheCarre(carre_mag)

print(" \n")

afficheCarre(carre_pas_mag)


def testLignesEgales(carre):
    """ Renvoie la somme des éléments d'une ligne de la liste 2D carre si toutes les lignes ont la même somme, et -1 sinon """
    a = sum(carre[0])

    for i in range(len(carre)) :
        if sum(carre[i]) != a :
            return -1
    return a

print(testLignesEgales(carre_mag))
print(" \n")
print(testLignesEgales(carre_pas_mag))


def testColonnesEgales(carre):
    """ Renvoie la somme des éléments d'une colonne de la liste 2D carre si toutes les colonnes ont la même somme, et -1 sinon """
    a = sum([b[0] for b in carre])

    for i in range(len(carre)) :
        if sum([b[i] for b in carre]) != a :
            return -1
    return a

print(testColonnesEgales(carre_mag))
print(testColonnesEgales(carre_pas_mag))


def testDiagonalesEgales(carre):
    """ Renvoie la somme des éléments d'une diagonale de la liste 2D carre si les 2 diagonales ont la même somme, et -1 sinon """
    a = sum([c[carre.index(c)] for c in carre])
    d = sum([c[carre.index(c) * (-1) - 1] for c in carre])  
    for i in range(len(carre[0])) :
        if sum([c[carre.index(c)] for c in carre]) != a and sum([c[carre.index(c) * (-1) - 1] for c in carre]) != a :
            return -1
    return a

print(testDiagonalesEgales(carre_mag))
print(testDiagonalesEgales(carre_pas_mag))


def estCarreMagique(carre):
    """ Renvoie True si c'est un carre magique et False sinon"""
    if testDiagonalesEgales(carre) != -1 and testLignesEgales(carre) != -1 and testColonnesEgales(carre) != -1 :
        return True
    return False

print(estCarreMagique(carre_mag))
print(estCarreMagique(carre_pas_mag))



def estNormal(carre):
    """ Retourne True si contient toutes les valeurs de 1 à n^2 où n est la taille 
        du carré, et False sinon """
    n = sum([i for i in range(1 ,len(carre) ** 2 + 1)])
    carre_sum = 0
    for i in range(len(carre)) :
        carre_sum += sum(carre[i])
    if carre_sum == n :
        return True
    return False

print(estNormal(carre_mag))
print(estNormal(carre_pas_mag))