import emne

class Person:

    def __init__(self, navn, brukernavn):
        self.navn = navn
        self.brukernavn = brukernavn

    def __str__(self):
        info = "Person: " + self.navn + " brnavn: " + self.brukernavn
        return info
    
class Student(Person):

    def __init__(self, navn, brukernavn, studnr):
        super().__init__(navn, brukernavn)
        self.studnr = studnr
        self.emne = None

    def __str__(self):
        info = "Student: " + self.navn + " brnavn: " + self.brukernavn \
               + " nummer: " + self.studnr
        return info
    
class Faglærer(Person):

    def __init__(self, navn, brukernavn, kontor):
        super().__init__(navn, brukernavn)
        self.kontor = kontor

    def finn_veien(self):
        return "Du må gå til " + self.kontor
    
    def __str__(self):
        info = "Faglærer: " + self.navn + " brnavn: " + self.brukernavn \
               + " kontor: " + self.kontor
        return info
    

p1 = Person("Arne", "a01")
print(p1)
print("Det var litt testing")
