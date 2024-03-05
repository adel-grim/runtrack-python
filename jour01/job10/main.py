montant_initial_de_l_investissement = 15000
taux_de_rendement_annuel= 5

gain_annuel = ( montant_initial_de_l_investissement * taux_de_rendement_annuel) /100
print(f"Gain annuel est de : {gain_annuel} euros")

montant_initial_de_l_investissement += 5000
taux_de_rendement_annuel += 2

nouveau_gain_annuel = (montant_initial_de_l_investissement +  taux_de_rendement_annuel)
print(f"Nouveau gain annuel est de : {nouveau_gain_annuel} euros")

retrait = montant_initial_de_l_investissement * 0.10
montant_initial_de_l_investissement -= retrait
taux_de_rendement_annuel -=1

montant_final = montant_initial_de_l_investissement + nouveau_gain_annuel
print(f"Montant final de l'investissement apres retrait :{montant_final} euros")