# Lecture notes - OOP - chapter 2-3

## Chapter 2:
- Creating classes and instantiating objects
- Access control
- Python Modules
- Python docstrings

## Chapter 3
- Basic inheritance
- Overriding and super()


### Creating classes and instantiating objects

Lage en klasse: Nøkkelord `class` 
Klassenavnet bør starte med stor forbokstav (PEP 8). 
Metoder, attributter og parametere bør starte med liten forbokstav.

Klassediagram Person-klasse:

![Person klasse](https://github.com/henrik2706/uit-inf-1400-v23/blob/main/lectures/oop-02-03-oo-concepts/Person4.png)


Kode som tilsvarer klassediagrammet over:
```python
class Person:
    
    def __init__(self,alderen,navnet):
        self.alder = alderen
        self.navn =navnet
        
    def getAlder(self):
        return self.alder
    
    def setAlder(self,alderen):
        self.alder = alderen
             
    def getNavn(self):
        return self.navn
    
    def setNavn(self,navnet):
        self.navn=navnet
```

Lage et objekt: Bruk konstruktøren til klassen dvs klassenavnet() <-- med eventuelle argumenter som konstruktøren (se `__init__()` ) sier.
Vi ønsker å lage et Person-objekt som har alder på 21 år og som heter Ola Nordmann.

```python
p1=Person(21,"Ola Nordmann")
```
Med tilsvarende objekt-diagram:

![Person objektdiagram](https://github.com/henrik2706/uit-inf-1400-v23/blob/main/lectures/oop-02-03-oo-concepts/Person-objekt.png)


### Access control
Innkapsling, private/protected/public -> Ikke i python, alt er public. Bruk underscore _ fremfor attributter/metoder for å symbolisere at man ikke vil at andre skal lese/endre verdien direkte.

```python
class Person:
    
    def __init__(self,alderen,navnet):
        self._alder = alderen
        self._navn =navnet
        
    def getAlder(self):
        return self._alder
    
    def setAlder(self,alderen):
        if self._gyldigAlder(alderen):
            self._alder = alderen
        else:
            self._alder=0
        
        
    def getNavn(self):
        return self._navn
    
    def setNavn(self,navnet):
        self._navn=navnet
        
    def _gyldigAlder(self,alderen):
        if alderen>=0:
            return True
        else:
            return False
```

### Python Modules
For å importere moduler (.py-filer) bruker vi nøkkelordet `import`, eller `from`... `import`.

```python
import math

fakultet=math.factorial(5)
```

eller 

```python
from math import factorial

fakultet=factorial(5)
```

eller bedre med alias

```python
from math import factorial as fac

fakultet=fac(5)
```

Men ikke gjør dette (vil være vanskelig å vite hvilken metode/funksjon som faktisk kjøres om du har importert flere moduler/filer):

```python
from math import *

fakultet=factorial(5)
```


### Python docstring
`"""Tekst"""` øverst i moduler/klasser/metoder for å beskrive/dokumentere hva modulen/klassen/metodene er/gjør.
Eller vi kan bruke `#` i koden for å beskrive/dokumentere (fordel/ulempe er at vi må åpne filen for å lese kommentarene) 

```python
class Person:
    """Enkel klasse som beskriver en person med 2 attributter, alder og navn"""
    
    def __init__(self,alderen,navnet):
        """Konstruktør som tar inn to argumenter. Alderen er en int og navnet er str
         returner ingen verdier"""
        self.alder = alderen
        self.navn =navnet
        
    #Standard getter/setter-metoder    
    def getAlder(self):
        return self.alder
    
    def setAlder(self,alderen):
        self.alder = alderen
        
    def getNavn(self):
        return self.navn
    
    def setNavn(self,navnet):
        self.navn=navnet
        
    def __str__(self):
        """Overriding og tilpasser utskriften til en person"""
        return "Alder er: "+str(self.alder) +" og navnet er: "\
            +self.navn
```

### Basic inheritance, overriding and super()
Innfører to subklasser til Person. En Ansatt-klasse og en Student-klasse

![subPerson-klassediagram](https://github.com/henrik2706/uit-inf-1400-v23/blob/main/lectures/oop-02-03-oo-concepts/subPerson.png)

Tilsvarende kode til diagrammet:

```python
import person


class Ansatt(person.Person):

    def __init__(self, alderen, navnet, stillingen, lonnen):
        super().__init__(alderen, navnet)
        self.stilling = stillingen
        self.lonn = lonnen

    def getStilling(self):
        return self.stilling

    def setStilling(self, stillingen):
        self.stilling = stillingen

    def getLonn(self):
        return self.lonn

    def setLonn(self, lonnen):
        self.lonn = lonnen
        
    def __str__(self):
        return super().__str__()+" stillingen er: "+self.stilling\
            +" og lønnen er: "+str(self.lonn)\
            


class Student(person.Person):

    def __init__(self, alderen, navnet, utdanningen, studentNummeret):
        person.Person.__init__(self, alderen, navnet)
        self.utdanning = utdanningen
        self.studentNummer = studentNummeret
        
    def getUtdanning(self):
        return self.utdanning
    
    def setUtdanning(self,utdanningen):
        self.utdanning = utdanningen
        
    def getStudentNummer(self):
        return self.studentNummer
    
    def setStudenNummer(self,studentNummeret):
        self.studentNummer = studentNummeret
    
    def __str__(self):
        return person.Person.__str__(self)+" utdanningen er: "+self.utdanning\
            +" og studentnummeret er: "+str(self.studentNummer)
```

Kode for å teste klassene

```python
if __name__ == "__main__":
    a1 = Ansatt(33,"Ola","lektor",500000)
    s1 = Student(21,"Kari","Informatikk",3432523)
    print(a1)
    print(s1)
```

Utskrift:

```python
Alder er: 33 og navnet er: Ola stillingen er: lektor og lønnen er: 500000
Alder er: 21 og navnet er: Kari utdanningen er: Informatikk og studentnummeret er: 3432523
```


