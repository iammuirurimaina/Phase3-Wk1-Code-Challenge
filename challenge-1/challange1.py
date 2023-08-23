def convert_to_24_hour(hour, minute, meridian):
    # condition for when it is pm and not noon
    if meridian == "pm" and hour != 12:
        # add 12 
        hour += 12
    
    # condition for if it's midnight (12:00 am)
    if meridian == "am" and hour == 12:
        hour = 0
    #convert the hour and minute to strings and add zeros at the begining
    hours = str(hour).zfill(2)
    minutes = str(minute).zfill(2)
    

    time_24_hour = hours + minutes
    
    return time_24_hour


print(convert_to_24_hour(11, 30, "am"))  
print(convert_to_24_hour(12, 00, "pm"))  
print(convert_to_24_hour(12, 0, "am"))  