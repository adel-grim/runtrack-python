#input pour rentrer un chiffre via terminal
n=int(input("Tapez un chiffre entier ayant une valeur au dessus de 0 :"))

#si "n (chiffre entier)" = 1 ou + alors "table de multi x1 2 ect.. qui s'incremente de 1" + "o (chiffre entier de 1 a 10 max)" pour multiplier de 1 a 10.
if n > 0 :
    for n in range (1, n+1):
        print(f"Table de multiplication de {n} :")
        for o  in range(1, 11):
            print(f"{n} x {o} = {n*o}")

#sinon print une erreur si le chiffre est negatif à 1 avec de nouveau un input pour rentrer un nouveau chiffre dans le terminal.
else:
    print("Erreur: Ecrire un chiffre au dessus de 0")
n=int(input("Tapez un chiffre entier ayant une valeur au dessus de 0 :"))

#repete la boucle pour pouvoir multiplier le chiffre donné de 1 a 10 max
if n > 0 :
    for n in range (1, n+1):
        print(f"Table de multiplication de {n} :")
        for o  in range(1, 11):
            print(f"{n} x {o} = {n*o}")
     
