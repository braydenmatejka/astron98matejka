# defining a function that takes an input of a year as an integer
# and performs the proper operations on it to test if it is a leap year
# and returns a boolean value

def leapyear(year):
    if year % 4 == 0 and year % 400 == 0: # using the mod operator (%) to test if the year is divisible by various values
        return True
    elif year % 4 == 0:
        if year % 100 != 0:
            return True
        else:
            return False
    else:
        return False