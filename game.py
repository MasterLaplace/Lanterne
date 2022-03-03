from main import PNJ
#from main import liste_pnj

print("test3")

def init_pnj(nbr_pnj, liste_pnj, id):
    for x in range(0, nbr_pnj):
        liste_pnj["test{0}".format(x)] = PNJ(id)
        id += 1
    return liste_pnj

def loop_game(nbr_pnj):
    while nbr_pnj != 0:
        for key, value in liste_pnj.items():
            if value.game_pj(age_fin) == 0:
                del liste_pnj[key]
                nbr_pnj -= 1
                break
        #for i in range(nbr_pnj):
            #print('|', end='')
        #print('')
    print("fin de la session, tout le monde est mort ...")

nbr_pnj = 4
age_fin = 40
id = 1
liste_pnj = {}

liste_pnj = init_pnj(nbr_pnj, liste_pnj, id)
loop_game(nbr_pnj)

#ok, pl, mk, ji
