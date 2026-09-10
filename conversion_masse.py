#------------------------------------
#       définition de fonction
#------------------------------------

def conversion_masse(masse :float, masse_depart : str, masse_fin: str):
    unite_masse = ["kg","hg","dag","g","dg","cg","mg"]
    for element in unite_masse:
        if element == masse_depart:
            indice_depart = unite_masse.index(element) + 1
        if element == masse_fin:
            indice_fin = unite_masse.index(element) + 1
    if indice_depart < indice_fin:
        dif = indice_fin - indice_depart
        return masse * 10.0**dif 
    elif indice_depart > indice_fin:
        dif = indice_depart - indice_fin
        return masse / 10.0**dif
    
#------------------------------------
#           Main
#------------------------------------

print("Voici la conversion",conversion_masse( 1, "kg", "g"))