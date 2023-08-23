def time_converter(hour, minute, meridian):
    if meridian == "pm" and hour != 12:
        hour += 12
    
    if meridian == "am" and hour == 12:
        hour = 0

    hours = str(hour).zfill(2)
    minutes = str(minute).zfill(2)

    time_24_hour = hours + minutes
    
    return time_24_hour

hour_input = int(input("Enter the hour: "))
minute_input = int(input("Enter the minute: "))
meridian_input = input("Enter 'am' or 'pm': ")

result = Time_converter(hour_input, minute_input, meridian_input)
print("Time in 24-hour format:", result)

