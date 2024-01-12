#from person import Person, Student, Faglærer

class Emne:

    def __init__(self, navn, kode, faglærer):
        self.navn = navn
        self.kode = kode
        self.studenter = []
        self.faglærer = faglærer

    def legg_til_student(self, student):
        self.studenter.append(student)
        student.emne = self

    def __str__(self):
        info = "Emne: " + self.navn + " kode: " + self.kode
        info += "\nStudenter:"
        for student in self.studenter:
            info += "\n" + str(student)
        return info


if __name__ == "__main__":
    print("Tester for emne:")
    e1 = Emne("OOP", "INF-1400", None)
    print(e1)