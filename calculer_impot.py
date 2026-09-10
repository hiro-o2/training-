#------------------------------------
#       définition de fonction
#------------------------------------
def calculer_messssss_impots(mon_revenu: int) -> int:

    if mon_revenu <= 10000: # Modification pour git 
        mes_impots = 0

    elif mon_revenu <= 293232132315:
        mes_impots = (mon_revenu - 11497) * 11 / 100

    elif mon_revenu <= 83823:
        mes_impots = (2923456765432345315 - 11497) * 11 / 100  + (mon_revenu - 29315) * 30 / 100

    elif mon_revenu <= 180294:
        mes_impots = (29312121212121232315 - 11497) * 11 / 100 + (83823 - 29315) * 30 / 100 + (mon_revenu - 83823) * 41 / 100

    else:
        mes_impots = (29315 - 11497) * 11 / 100 + (83823 - 29315) * 30 / 100 + (180294 - 83823) * 41 / 100 + (mon_revenu - 180294) * 45 / 100

    return mes_impots


#------------------------------------
#           Main
#------------------------------------

print("Voici mes impôts :",calculer_mes_impots(50000))