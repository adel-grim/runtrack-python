L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
liste_sans_doublons = []
#liste vide pour y mettre les valeurs sans doublons

for valeur in L: #boucleur " valeur contenu dans la liste "L"
    if valeur not in liste_sans_doublons: # si une valeur de la liste "L" n'est PAS dans la liste sans doublons
        liste_sans_doublons.append(valeur)#alors on l'y ajoute avec "append"
#boucle pour verifier si une valeur de la liste "L" n'est pas dans la nouvelle liste qui contiendra la liste L sans ses doublons
print(liste_sans_doublons)
#on affiche la liste d'origine amputé de ses doublons 
