def moyenne(note1,note2,note3):
    moyenne = (note1+note2+note3) / 3
    return(moyenne)


def notes():
    note1 = float(input("Entrez la première note : "))
    note2 = float(input("Entrez la deuxième note : "))
    note3 = float(input("Entrez la troisième note : "))
    return(note1, note2, note3)

note1,note2,note3=notes()

moyenne_etudiant=moyenne(note1,note2,note3)
print("La moyenne est de" , moyenne_etudiant)

if moyenne_etudiant >= 15:
    print("Tres bon eleve")
elif moyenne_etudiant >=11  <=15:
    print("Bon eleve")
elif moyenne_etudiant >=8 <=10:
    print("Eleve moyen")
elif moyenne_etudiant >=0 <=7:
    print("Eleve devant faire des efforts")