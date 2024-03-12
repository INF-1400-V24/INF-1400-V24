
class A:

    def __init__(self, num):
        self._num = num

    @property
    def num(self):
        return self._num
    
    @num.setter
    def num(self, num):
        if num < 0 or num > 100:
            raise ValueError("Illegal num")
        self._num = num


if __name__ == "__main__":
    a = A(10)
    a.num = 5
    print(a.num)
    a.num = 1000
    print(a.num)