from random import randint

pnj = "homme"
Gold_pnj = randint(10,25)
print(f"l'argent du père {Gold_pnj}")
pnj_2 = "femme"
Gold_pnj_2 = randint(8,22)
print(f"l'argent de la mère {Gold_pnj_2}")
if pnj == 'homme' and pnj_2 == 'femme':
    nbr_enfant = randint(1,6)
    print(f"nombre d'enfant {nbr_enfant}")
eritage = (Gold_pnj + Gold_pnj_2) / nbr_enfant
print(f"éritage de l'argent par enfant {eritage}")

###############################################################

lien_socio = {}

lien_socio = {}
rencontre = True
pnj_name = "ok"

def rencontre(lien_socio, pnj_name):
    for key in lien_socio.items():
        if key == pnj_name:
            return lien_socio.update({key: lien_socio[key] + 1})
    lien_socio[pnj_name] = 1
    return lien_socio

def deuil(lien_socio, pnj_name):
    del lien_socio[pnj_name]
    return lien_socio
lien_socio
rencontre(lien_socio, pnj_name)
