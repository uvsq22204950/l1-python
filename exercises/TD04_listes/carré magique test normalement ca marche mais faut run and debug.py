
carre_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 3, 13]] # liste avec comme élément des liste je crois
 #carré magique = ligne = a colonne = diago   inverse pour pas magique.
carre_pas_mag=[]

for ligne in carre_mag :
    carre_pas_mag.append(ligne.copy)
carre_pas_mag=[ligne[:] for ligne in carre_mag]
carre_pas_mag[3][2]=7
print(carre_pas_mag)
print(carre_mag)

def afficheCarre(carre):
    """ Affiche la liste à 2 dimensions carre comme un carré"""
    for ligne in carre :
        print(ligne)
    print()
afficheCarre(carre_mag)

print(" \n")

afficheCarre(carre_pas_mag)

def testLignesEgales(carre):

    somme = sum(carre[0])

    for somme_ligne in carre :
        if somme != sum(somme_ligne) :
            return -1
    return somme

print(testLignesEgales(carre_mag))
print(testLignesEgales(carre_pas_mag))


def testColonnesEgales(carre):
   c1=[ligne[0] for ligne in carre]
   s1=sum(c1)
   for nc in range(1,len(carre)):
        c2=[ligne[nc]for ligne in carre]
        if s1!=sum(c2):
            return -1
        return s1
print(testColonnesEgales(carre_mag))
print(testColonnesEgales(carre_pas_mag))


def testDiagonalesEgales(carre):
    d1=[carre[i][i]for i in range (len(carre))]
    d2=[carre[i][len(carre)-i-1]for i in range(len(carre))]
    s1=sum(d1)
    if s1!=sum(d2):
        return -1
    return s1

print(testDiagonalesEgales(carre_mag))
print(testDiagonalesEgales(carre_pas_mag))


def estCarreMagique(carre):
    return testDiagonalesEgales(carre)==testColonnesEgales(carre) and testLignesEgales(carre)== testDiagonalesEgales(carre) and testLignesEgales!=-1


print(estCarreMagique(carre_mag))
print(estCarreMagique(carre_pas_mag))



def estNormal(carre):
    liste=[]
    for ligne in carre :
       liste.extend(ligne)
    for i in range(1,len(carre)*len(carre)+1):
        if i not in liste:
            return False
    return True 

print(estNormal(carre_mag))
print(estNormal(carre_pas_mag))