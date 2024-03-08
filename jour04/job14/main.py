def my_long_word(longueur_min, chaine):
    mots = chaine.split()  
    #pour separer la chaine en mots disticts
    
   
    mots_long = []
    #liste vide pour y mettre les mots de plus de 3lettres
    for mot in mots:
        #boucle pour parcourir chaqur mot de "mots"
        longueur_mot = 0
        #initialisation de la longueur du mot a 0
        for _ in mot:
            longueur_mot += 1
        if mot and longueur_mot > longueur_min:
            mots_long.append(mot)
    return mots_long


# Appel de la fonction avec les arguments ( 3 mot minimum + la phrase a decouper)
resultat = my_long_word(3, "La peur est le chemin vers le côté obscure, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance")

# Affichage du résultat
print(resultat)




#realisé avec l'aide de chat GPT en m'expliquant chaque ligne de code
