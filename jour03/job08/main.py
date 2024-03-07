def food(type,saison):
    if type == "fruits" and saison == "hiver":
        return("orange, mandarine et kiwi")
    elif type == "fruits" and saison == "été":
        return("Poire, fraise, cassis")
    elif type == "legume" and saison == "hiver":
        return("carotte, topinambour, endive")
    elif type == "legume" and saison == "été":
        return("artichaut, aubergine,navet")
    
cmd=food("legume","hiver")
print(cmd)