from Calculator import Calculator


class Child(Calculator):

    def __init__(self):
        Calculator.__init__(self, 1, 1)

    def get_all_data(self):
        return self.num1 + self.num2 + self.sum()


print(Child().get_all_data())
