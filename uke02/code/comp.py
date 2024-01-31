
class Kaffekopp:

    def __init__(self, dl):
        self._kapasitet = dl
        self._fyllingsgrad = 0

    def fyll(self):
        self.fyllingsgrad = self.kapasitet


kopp1 = Kaffekopp(2)
kopp1.fyll()