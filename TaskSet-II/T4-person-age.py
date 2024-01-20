import datetime


class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob

    def calculate_age(self):
        year, month, day = map(int, self.dob.split("-"))
        current_year = datetime.date.today().year
        print("{}'s age is: {}".format(self.name, current_year - year))


Person('Girish', 'Ind', '1993-01-03').calculate_age()
