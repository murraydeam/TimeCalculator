"""
Main function for adding time.
#1 Clean up input for start and duration  (for better use)
#2 Convert strings to integers
#3
#4
#5

"""


def add_time(start, duration, day=""):
    # Separate clock from Cycle
    clock, cycle = start.split()
    cycle = str.upper(cycle)
    new_cycle = cycle

    # Separate hour and minute in Start time
    start_hour, start_minute = clock.split(':')

    # Separate hour and minute in Duration
    duration_hour, duration_minute = duration.split(':')

    # Hours and Minutes converted to integers for adding
    s_hour = int(start_hour)
    s_minute = int(start_minute)
    d_hour = int(duration_hour)
    d_minute = int(duration_minute)
    message = ''
    cycles = 0

    # Variable for the sum of start and duration.
    day_count = 0

    hour = s_hour + d_hour
    while hour >= 24:
        hour = hour - 24
        day_count += 1

        ###

    minute = s_minute + d_minute

    if cycle == str.upper('PM') and hour >= 12:
        new_cycle = 'AM'
        hour -= 12
        # day_count += 1
    if cycle == str.upper('AM') and hour >= 12:
        new_cycle = 'PM'
        hour -= 12

    if minute >= 60:
        hour = hour + 1
        minute = minute - 60

    if minute < 10:
        minute = '0' + str(minute)

    new_hour = str(hour)
    new_minute = str(minute)

    if new_hour == '12' and new_cycle == 'PM':
        new_cycle = 'AM'
    elif new_hour == '12' and new_cycle == 'AM':
        new_cycle = 'PM'
    if day_count != 1:
        message = '(next day)'
    elif day_count >= 2:
        message = day_count, 'days later'

    day = str.capitalize(day)

    weekdays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
    if day in weekdays:
        if day == 'Monday':
            day = (1 + day_count) % 7
            day = weekdays[day]
        if day == 'Tuesday':
            day = (2 + day_count) % 7
            day = weekdays[day]
        if day == 'Wednesday':
            day = (3 + day_count) % 7
            day = weekdays[day]
        if day == 'Thursday':
            day = (4 + day_count) % 7
            day = weekdays[day]
        if day == 'Friday':
            day = (5 + day_count) % 7
            day = weekdays[day]
        if day == 'Saturday':
            day = (6 + day_count) % 7
            day = weekdays[day]
        if day == 'Sunday':
            day = (7 + day_count) % 7
            day = weekdays[day]

    new_time = new_hour + ":" + new_minute + ' ' + new_cycle

    final = new_time + ' ' + day + message

    print(day_count)
    print(cycles)

    return final


print(add_time('10:45 PM', '2:15', 'Monday'))
