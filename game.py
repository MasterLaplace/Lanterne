from main import PNJ

def init_pnj(nbr_pnj, liste_pnj):
    for x in range(0, nbr_pnj):
        liste_pnj["test{0}".format(x)] = PNJ()
    return liste_pnj

def game(nbr_pnj):
    while nbr_pnj != 0:
        for key, value in liste_pnj.items():
            if value.game_pj(age_fin) == 0:
                del liste_pnj[key]
                nbr_pnj -= 1
                break
    print("fin de la session, tout le monde est mort ...")

nbr_pnj = 4
age_fin = 40
liste_pnj = {}

init_pnj(nbr_pnj, liste_pnj)
game(nbr_pnj)

#ok, pl, mk, ji