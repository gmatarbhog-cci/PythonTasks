class Calculator:
    num = 100

    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b

    def sum(self):
        return self.num1 + self.num2 + self.num


print(Calculator(1, 2).sum())
