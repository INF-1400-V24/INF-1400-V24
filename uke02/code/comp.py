
class Kaffekopp:

    def __init__(self, dl):
        self.kapasitet = dl
        self.fyllingsgrad = 0

    def fyll(self):
        self.fyllingsgrad = self.kapasitet