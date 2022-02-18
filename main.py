import random
from random import randint
import time


class PNJ:
    def __init__(self):
        self.name = str(input("Name ? : "))
        self.sexe = random.choice(['homme', 'femme'])
        # vie
        self.HP_pnj = 50
        self.Stamina_pnj = 20
        self.temp = 0
        # survie
        self.faim_pnj = 100
        self.soif_pnj = 100
        self.Gold_pnj = 0
        self.metier = ["Mineur","Bucheront"] #str(input("Quel est votre classe de combat ? Forgeron/Mineur/Bucheront/Agriculteur/Pecheur/Commercant/Tavernier/Aventurier : "))
        self.class_metier = random.choice(self.metier)
        # personalitys
        self.pecher = ['colere', 'luxure', 'envie', 'paresse', 'orgueil', 'gourmandise', 'avarice']
        self.vertue = ['patience', 'purete', 'charite', 'diligence', 'humilite', 'temperance', 'desinteressement']
        #self.personalitys()
        self.dico_pnj = {}
        # self.nourriture = ['pomme', 'pain', 'soupe']
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

    # vente metier
    def vt_cailloux(self):
        #print("cailloux vendue !")
        x = randint(1, 4)
        return self.more_gold_pnj(x)

    def vt_cuivre(self):
        #print("cuivre vendue !")
        z = randint(5, 10)
        return self.more_gold_pnj(z)

    def vt_chene(self):
        #print("chene vendue !")
        return self.more_gold_pnj(3)

    def vt_epicia(self):
        #print("epicua vendue !")
        return self.more_gold_pnj(5)

    # personalite du pnj
    def personalitys(self):
        for i in range(7):
            self.pcher = randint(0, 100)
            self.vrtue = 100 - self.pcher
            self.x = self.pecher.pop()
            self.z = self.vertue.pop()  # self.dico = {self.z: self.vrtue, self.x: self.pcher}
            self.dico_pnj[self.z] = self.vrtue
            self.dico_pnj[self.x] = self.pcher
            print(f"{self.z} : {self.vrtue} / {self.x} : {self.pcher} %")  # return self.dico

    def show_personality(self):
        for cle, valeur in self.dico_pnj.items():
            print("l'élément de clé", cle, "vaut", valeur)

    # quotidien du pnj
    def vivre_pnj(self):
        # self.metier_mineur()
        self.class_test()
        self.faim_pj()  # boir / #produire /#vendre /#acheter
        self.soif_pj()
        return

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

    # action produire
    def metier_mineur(self):
        return self.minage()

    def minage(self):
        #print("j'ai cassé du cailloux")
        caill_miner = randint(1, 10)
        if caill_miner >= 3:
            #print("cailloux miner")
            self.faim_pnj -= 2
            self.soif_pnj -= 4
            return self.vt_cailloux(), self.faim_pnj, self.soif_pnj
        elif caill_miner < 3:
            #print("cuivre miner")
            self.faim_pnj -= 5
            self.soif_pnj -= 8
            return self.vt_cuivre(), self.faim_pnj, self.soif_pnj
        print("faim - 5 & soif - 10")
        self.faim_pnj -= 5
        self.soif_pnj -= 10
        return self.faim_pnj, self.soif_pnj

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
            return self.metier_mineur()
        elif self.class_metier == "Bucheront":
            return self.metier_bucheront()
        elif self.class_metier == "Forgeron":
            return self.metier_forgeron()

    def class_metiers(self):
        print(f"Metier : {self.class_metier} | Gold : {self.Gold_pnj}")
        print(f"PV : {self.HP_pnj} | Stamina : {self.Stamina_pnj}")
        print(f"Faim : {self.faim_pnj} | Soif : {self.soif_pnj} | Temps : {self.temp}")
        #print(f"Historique des transaction : {self.transaction}")

    def game_pj(self, age_fin):
        if not self.temp == age_fin:
            self.vivre_pnj()
            self.faim_pnj -= 8
            self.soif_pnj -= 10
            self.class_metiers()
            print("")
            if self.give_faim_pnj() <= 0 or self.give_soif_pnj() <= 0:
                print(f"{self.name} mort de faim ou de soif a {self.temp} ans")
                return 0
            self.temp += 1
            print(f"ans {self.temp}")
            time.sleep(0.1)
            return 1
        print(f"{self.name} mort de vielleisse !")
        return 0
