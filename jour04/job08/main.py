L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

def addition_valeur(L):
    sum =0
    # somme initialisé a 0
    for valeur in L :
     if valeur % 2 == 0:
        sum += valeur
        #boucle for pour analyser chaque nombre de la liste, si la valeur %2==0 alors le nombre est pair et additionné avec les autres nombre pair
    return sum
# on retourne la somme

print("Valeur totale des nombres pair :", addition_valeur(L))
#affichage de la valeur totale


    