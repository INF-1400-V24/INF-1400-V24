from abc import ABC, abstractmethod
import matplotlib.pyplot as plt

class Function:

    def __init__(self, interval):
        self.interval = interval

    @abstractmethod
    def __call__(self, x):
        pass

    @abstractmethod
    def __str__(self):
        pass

    def plot(self, step):
        start = self.interval[0]
        end = self.interval[1]
        x = start
        x_values = []
        y_values = []
        while x <= end:
            x += step
            x_values.append(x)
            y_values.append(self(x))
        plt.plot(x_values, y_values)
        plt.grid()
        plt.axhline(0, color="black")
        plt.axvline(0, color="black")
        plt.show()
        


class Polynomial(Function):

    def __init__(self, coeffs, interval):
        super().__init__(interval)
        self.coeffs = coeffs

    def evaluate(self, x):
        value = 0
        for i in range(len(self.coeffs)):
            value += self.coeffs[i] * x**i
        return value

    def __call__(self, x):
        return self.evaluate(x)

    def __str__(self):
        poly = ""
        for i in range(len(self.coeffs)):
            poly += str(self.coeffs[i]) + f"x^{i} + "
        poly = poly[:-3]
        return poly


class Exponential(Function):
    
    def __init__(self, base, exp, interval):
        super().__init__(interval)
        self.base = base
        self.exp = exp

    def evaluate(self, x):
        return self.base * x**self.exp
    
    def __call__(self, x):
        return self.evaluate(x)
    
    def __str__(self):
        info = f"{self.base} * x^{self.exp}"
        return info


if __name__ == "__main__":
    a = Polynomial([0, 2, 2, 5], [-3, 3])
    print(a.evaluate(2))
    print(a)
    a.plot(0.01)

    b = Exponential(1, 2, [0, 2])
    print(b.evaluate(2))
    print(b)