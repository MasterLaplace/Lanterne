import random
from random import randint

global liste_pnj
liste_pnj = {}

print("test1")

class Mineur:
    def __init__(self):
        self.prix_cailloux = randint(1, 4)
        self.prix_cuivre = randint(5, 10)

    def vt_cailloux(self):
        #print("cailloux vendue !")
        prix = randint(1, 4)
        return prix

    def vt_cuivre(self):
        #print("cuivre vendue !")
        prix = random.randint(5, 10)
        return prix

    def who(self, id_pnj):
        for key, values in liste_pnj.items():
            if id_pnj == values.__id:
                return values

    def rencontre_metier(self, current_pnj, dico_pnj):
        for keys, values in liste_pnj.items():
            for key, value in dico_pnj.items():
                print(current_pnj.__id)
                if key == values.__id and current_pnj.class_metier == values.class_metier and key != current_pnj.__id:
                    dico_pnj({value: dico_pnj[value] + 1})
                else:
                    dico_pnj[values.__id] = 1
        return dico_pnj

    def minage(self, faim_pnj, soif_pnj):
        #print("j'ai cassé du cailloux")
        caill_miner = randint(1, 10)
        if caill_miner >= 3:
            #print("cailloux miner")
            faim_pnj -= 2
            soif_pnj -= 4
            return [self.vt_cailloux(self), faim_pnj, soif_pnj]
        elif caill_miner < 3:
            #print("cuivre miner")
            faim_pnj -= 5
            soif_pnj -= 8
            return [self.vt_cuivre(self), faim_pnj, soif_pnj]

    # action produire
    def metier_mineur(self, faim_pnj, soif_pnj, dico_pnj, id_pnj):
        liste = self.minage(self, faim_pnj, soif_pnj)
        liste.append(self.rencontre_metier(self, self.who(self, id_pnj), dico_pnj))
        return liste
