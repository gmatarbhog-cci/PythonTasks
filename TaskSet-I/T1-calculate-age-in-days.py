def calculate_age():
    # accept age
    age = int(input("Please enter age: "))

    year_days = 365

    age_in_days = age * year_days
    print("{} {}".format("Age in days is", age_in_days))


calculate_age()
