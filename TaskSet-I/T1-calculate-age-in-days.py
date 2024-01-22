def calculate_age(age):
    if age <= 0:
        raise Exception('Age cannot be less than 0')
    year_days = 365

    return age * year_days


def prompt_age():
    # accept age
    age = int(input("Please enter age: "))
    age_in_days = calculate_age(age)
    print("{} {}".format("Age in days is", age_in_days))


prompt_age()
