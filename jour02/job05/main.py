for nombre in range(101):
    if nombre % 3 and nombre % 5 ==0:
         print("FizzBuzz")
    elif nombre % 3 == 0:
        print("Fizz")
    elif nombre % 5 == 0:
            print("Buzz")
    
    else:
        print(nombre)

# On utilise une boucle for avec une variable "nombre" sur laquelle on utlise range pour creer une liste de nombre (1 a 100 donc 101)
    #puis on utilise une balise de condition if pour verifier si le nombre est à la fois un multiple de trois et de cinq avec un operateur modulo (%)
    #On veut que le mot fizz et buzz saffiche a la place des multiple de 3 et 5 donc on pose des conditions en plus a verifier avec elif (else-if) 
    #si aucune des conditions ecrite avec if et elif ne sont respéctés alors le terminal nous retourne le nombre sous forme de chiffre comme prevu.