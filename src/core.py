from random import randint, choice
from copy import deepcopy

class PNJ:
    def __init__(self, id_pnj):
        self.__id = id_pnj
        self.name = str(input("Name ? : "))
        self.sexe = choice(['homme', 'femme'])
        # vie
        self.HP_pnj = 50
        self.Stamina_pnj = 20
        self.temp = 0
        # survie
        self.faim_pnj = 100
        self.soif_pnj = 100
        self.Gold_pnj = 0
        self.job = ["Mineur"] #str(input("Quel est votre classe de combat ? Forgeron/Mineur/Bucheront/Agriculteur/Pecheur/Commercant/Tavernier/Aventurier : ")),"Bucheront"
        self.class_metier = choice(self.job)
        # personalitys
        self.pecher = {'colere':0, 'luxure':0, 'envie':0, 'paresse':0, 'orgueil':0, 'gourmandise':0, 'avarice':0}
        self.vertue = {'patience':0, 'purete':0, 'charite':0, 'diligence':0, 'humilite':0, 'temperance':0, 'desinteressement':0}
        self.personalitys()
        self.dico_pnj = {self.__id : 0}
        self.link = {}
        # self.nourriture = ['pomme', 'pain', 'soupe']
        self.inventory = {}
        self.transaction = []

    # give
    def transaction(self):
        return self.transaction

    def give_gold_pnj(self):
        return self.Gold_pnj  # affiche l'argent

    def give_faim_pnj(self):
        return self.faim_pnj  # affiche la faim

    def give_soif_pnj(self):
        return self.soif_pnj  # affiche la soif

    def give_id_pnj(self):
        return self.__id

    def give_job_pnj(self):
        return self.class_metier

    # argent
    def more_gold_pnj(self, prix):
        self.transaction.append(prix)
        self.Gold_pnj += prix
        return self.Gold_pnj

    def less_gold_pnj(self, prix):
        self.transaction.append(-prix)
        self.Gold_pnj -= prix
        return self.Gold_pnj

    # nourriture
    def nourri_pomme(self):
        #print("pomme acheté !")
        self.faim_pnj += 8
        self.soif_pnj += 1
        y = randint(2, 4)
        return self.less_gold_pnj(y), self.faim_pnj, self.soif_pnj

    def nourri_pain(self):
        #print("pain acheté !")
        self.faim_pnj += 15
        h = randint(4, 6)
        return self.less_gold_pnj(h), self.faim_pnj

    def nourri_soupe(self):
        #print("soupe acheté !")
        self.faim_pnj += 30
        self.soif_pnj += 15
        e = randint(8, 10)
        return self.less_gold_pnj(e), self.faim_pnj, self.soif_pnj

    def nourri_eau(self):
        #print("eau acheté !")
        self.soif_pnj += 30
        return self.less_gold_pnj(3), self.soif_pnj

    def vt_chene(self):
        #print("chene vendue !")
        return self.more_gold_pnj(3)

    def vt_epicia(self):
        #print("epicua vendue !")
        return self.more_gold_pnj(5)

    # personalite du pnj
    def personalitys(self):
        lst_pecher = list(self.pecher.keys())
        lst_vertue = list(self.vertue.keys())
        for i in range(7):
            pcher = randint(0, 100)
            vrtue = 100 - pcher
            self.pecher[lst_pecher[i]] = pcher
            self.vertue[lst_vertue[i]] = vrtue
            print(f"{lst_vertue[i]} : {vrtue} / {lst_pecher[i]} : {pcher} %")

    def show_personality(self):
        for cle, valeur in self.dico_personallity.items():
            #print("l'élément de clé", cle, "vaut", valeur)
            print(f"{str(cle)} : {self.dico_personallity[cle]} / {str(cle + 1)} : {self.dico_personallity[cle + 1]} %")

    def shild(self, pnj_id):
        if self.link:
            CORE.liste_pnj["test{0}".format(pnj_id)] = PNJ(pnj_id)
            pnj_id += 1
        return pnj_id

    # quotidien du pnj
    def vivre_pnj(self):
        # self.metier_mineur()
        self.class_test()
        self.shild(CORE.pnj_id)
        self.faim_pj()  # boir / #produire /#vendre /#acheter
        self.soif_pj()

    # action vivre
    def faim_pj(self):
        if self.faim_pnj <= 70:
            #print("j'ai faim")  # aller.acheter.tavernier
            if self.give_gold_pnj() >= 8:  # and self.faim >= 30:
                return self.nourri_soupe()
            elif self.give_gold_pnj() >= 4:  # and self.faim >= 15:
                return self.nourri_pain()
            elif self.give_gold_pnj() >= 2:  # and self.faim >= 8:
                return self.nourri_pain()
            else:
                return  # attendre / #produire / #vendre
        else:
            return  # on continue la journee

    def soif_pj(self):
        if self.soif_pnj <= 70:
            #print("j'ai soif")
            if self.give_gold_pnj() >= 2:
                return self.nourri_eau()
        else:
            return

    def metier_bucheront(self):
        return self.hachage()

    def hachage(self):
        boit_couper = randint(1, 10)
        if boit_couper >= 3:
            return self.vt_chene()
        elif boit_couper < 3:
            return self.vt_epicia()
        return

    def metier_forgeron(self):
        return self.forger()

    def forger(self):
        boit_couper = randint(1, 10)
        if boit_couper >= 3:
            return self.vt_chene()
        elif boit_couper < 3:
            return self.vt_epicia()
        return

    def class_test(self):  # test
        if self.class_metier == "Mineur":
            #print("Mineur")
            liste = Mineur.metier_mineur(Mineur, self.faim_pnj, self.soif_pnj, self.dico_pnj, self.__id)
            self.more_gold_pnj(liste[0])
            self.faim_pnj = liste[1]
            self.soif_pnj = liste[2]
            self.dico_pnj = deepcopy(liste[3])
            return self.faim_pnj, self.soif_pnj, self.dico_pnj
        elif self.class_metier == "Bucheront":
            return self.metier_bucheront()
        elif self.class_metier == "Forgeron":
            return self.metier_forgeron()

    def class_metiers(self):
        print(f"Metier : {self.class_metier} | Gold : {self.Gold_pnj} | id : {self.__id}")
        print(f"PV : {self.HP_pnj} | Stamina : {self.Stamina_pnj} | Sexe : {self.sexe}")
        print(f"Faim : {self.faim_pnj} | Soif : {self.soif_pnj} | Temps : {self.temp}")
        print(f"Historique des transaction : {self.transaction}")
        #self.show_personality()
        for key in self.dico_pnj.items():
            print(f"rencontre[{key}]")

    def game_pj(self, Core, age_fin):
        if not self.temp == age_fin:
            self.vivre_pnj()
            self.faim_pnj -= 8
            self.soif_pnj -= 10
            self.class_metiers()
            if self.give_faim_pnj() <= 0 or self.give_soif_pnj() <= 0:
                print(f"{self.name} mort de faim ou de soif a {self.temp} ans")
                return 0
            self.temp += 1
            #print(f"ans {self.temp}")
            return 1
        print(f"{self.name} mort de vielleisse !")
        return 0

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
        prix = randint(5, 10)
        return prix

    def who(self, id_pnj):
        #print(f"2: {id_pnj}")
        for key, values in CORE.liste_pnj.items():
            if id_pnj == values.give_id_pnj():
                return values

    def rencontre_metier(self, current_pnj, dico_pnj):
        tmp_dico = deepcopy(dico_pnj)
        for keys, values in CORE.liste_pnj.items():
            for key, value in dico_pnj.items():
                #print(f"3: {key}")
                if current_pnj.give_job_pnj() == values.give_job_pnj() and key != current_pnj.give_id_pnj():
                    tmp_dico[key] = tmp_dico[key] + 1
                elif key == current_pnj.give_id_pnj():
                    continue
                else:
                    tmp_dico[values.give_id_pnj()] = 1
        return tmp_dico

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

class Core:
    def __init__(self): 
        self.nbr_pnj = 4
        self.age_fin = 40
        self.pnj_id = 0
        self.liste_pnj = {}
        self.init_pnj()

    def init_pnj(self):
        for x in range(self.pnj_id, self.nbr_pnj):
            self.liste_pnj["test{0}".format(x)] = PNJ(self.pnj_id)
            self.pnj_id += 1
        return self.liste_pnj, self.pnj_id

    def loop_game(self):
        while self.nbr_pnj != 0:
            for key, value in self.liste_pnj.items():
                if value.game_pj(self, self.age_fin) == 0:
                    del self.liste_pnj[key]
                    self.nbr_pnj -= 1
                    break
            #for i in range(nbr_pnj):
                #print('|', end='')
            #print('')
        print("fin de la session, tout le monde est mort ...")

if __name__ == '__main__':
    CORE = Core()
    CORE.loop_game()
