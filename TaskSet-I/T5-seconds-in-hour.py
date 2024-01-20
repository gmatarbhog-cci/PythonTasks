def get_seconds_in_hour(hours):
    seconds_in_minute = 60
    minutes_in_hour = 60
    total_minutes = minutes_in_hour * hours
    seconds_in_hour = seconds_in_minute * total_minutes
    return seconds_in_hour


print(get_seconds_in_hour(24))
