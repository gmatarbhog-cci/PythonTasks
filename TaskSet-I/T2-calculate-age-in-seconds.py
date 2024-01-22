def calculate_age_in_seconds(age):
    days_per_year = 365
    seconds_per_day = 86400
    age_in_days = age * days_per_year
    return seconds_per_day * age_in_days


print(calculate_age_in_seconds(30))
