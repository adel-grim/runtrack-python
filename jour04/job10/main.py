L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

produit = 1
#produit initialiser à 1

for valeur in L:
    if 25 <= valeur <= 90:
        #verification que la valeur est entre 25 et 90
        produit *= valeur 
        #multiplie par 1 avec "produit" initialisé a 1

print(produit)