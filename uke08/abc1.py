from abc import ABC, abstractmethod

class A(ABC):

    def __init__(self, tall):
        self.tall = tall

    @abstractmethod
    def endre_tall(self):
        pass

    def print_tall(self):
        print(self.tall)

class B(A):

    def __init__(self, tall):
        super().__init__(tall)

    def endre_tall(self):
        self.tall += 1

class C(A):

    def __init__(self, tall):
        super().__init__(tall)

    def endre_tall(self):
        self.tall -= 1

b1 = B(5)
b1.endre_tall()
b1.print_tall()

