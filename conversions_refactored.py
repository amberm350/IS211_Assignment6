from conversions import *

def convert(from_units, to_units, value):

    from_lcase = from_units.lower()
    to_lcase = to_units.lower()

    if from_lcase == 'celsius' and to_lcase == "kelvin":
        return convertCelsiusToKelvin(value)
    elif from_lcase == 'celsius' and to_lcase == "fahrenheit":
        return convertCelsiusToFahrenheit(value)
    elif from_lcase == 'fahrenheit' and to_lcase == "celsius":
        return convertCelsiusToFahrenheit(value)
    elif from_lcase == 'fahrenheit' and to_lcase == "kelvin":
        return convertCelsiusToFahrenheit(value)
    elif from_lcase == 'kelvin' and to_lcase == "celsius":
        return convertCelsiusToFahrenheit(value)
    elif from_lcase == 'kelvin' and to_lcase == "fahrenheit":
        return convertCelsiusToFahrenheit(value)
    elif from_lcase == "miles" and to_lcase == "meters":
        return converMilesToMeters(value)