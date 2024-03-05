
def pyramid(chaine):
    length = len(chaine)
    for i in range(1, length + 1):
        chars = chaine[:i]
        print(chars + chars[-2::-1])

chaine = "abcdefghijklmnopqrstuvwxyz" * 10
pyramid(chaine)