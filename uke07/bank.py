from person import Person

class Bank:

    def __init__(self):
        self._customers = []

    def add_customer(self, name):
        self._customers.append(Person(name))

    def add_account_to_person(self, name):
        pass


if __name__ == "__main__":

    b = Bank()
    b.add_customer("Arne")
    b.add_account_to_person("Arne")