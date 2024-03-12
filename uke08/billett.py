from abc import ABC, abstractmethod
from random import randint

class Billett(ABC):

    def __init__(self, vognnr, setenr, passasjernavn):
        self.vognnr = vognnr
        self.setenr = setenr
        self.passasjernavn = passasjernavn
        self.ant_kolli = 0
        self.totalpris = 0

    @abstractmethod
    def bestill_mat(self, rett, pris):
        pass

    @abstractmethod
    def legg_til_bagasje(self):
        pass

    def __str__(self):
        info = "Navn: " + self.passasjernavn
        info += "\nVogn, sete: " + str(self.vognnr) + ", " + str(self.setenr)
        info += "\nTotalpris: " + str(self.totalpris)
        return info


class Førsteklasse(Billett):

    def __init__(self, passasjernavn):
        super().__init__(1, randint(1, 20), passasjernavn)
        self.totalpris = 600

    def bestill_mat(self, rett, pris):
        print("Førsteklassepassasjer bestilte", rett, "for 0kr")

    def legg_til_bagasje(self):
        if self.ant_kolli >= 2:
            self.totalpris += 100
        self.ant_kolli += 1

    def endre_sete(self, setenr):
        self.setenr = setenr


class Andreklasse(Billett):

    def __init__(self, passasjernavn):
        super().__init__(randint(2, 3), randint(1, 20), passasjernavn)
        self.totalpris = 300

    def bestill_mat(self, rett, pris):
        print("Andreklassepassasjer bestilte", rett, "for", pris, "kroner")
        self.totalpris += pris

    def legg_til_bagasje(self):
        self.ant_kolli += 1
        self.totalpris += 100


if __name__ == "__main__":
    f1 = Førsteklasse("Arne")
    a1 = Andreklasse("Berit")

    f1.endre_sete(1)
    f1.legg_til_bagasje()
    f1.bestill_mat("pølse", 50)

    a1.legg_til_bagasje()
    a1.bestill_mat("biff", 250)

    print()
    print(f1)
    print()
    print(a1)
    