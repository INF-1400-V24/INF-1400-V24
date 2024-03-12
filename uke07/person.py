from account import Account

class Person:

    def __init__(self, name):
        self._name = name
        self._accounts = []

    def new_account(self):
        self._accounts.append(Account(0))