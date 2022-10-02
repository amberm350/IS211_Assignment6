from conversions import *

class ConversionError(Exception):
    pass

def convert(from_units, to_units, value):

    from_lcase = from_units.lower()
    to_lcase = to_units.lower()

    if from_lcase == 'celsius' and to_lcase == "kelvin":
        return convertCelsiusToKelvin(value)
    elif from_lcase == 'celsius' and to_lcase == "fahrenheit":
        return convertCelsiusToFahrenheit(value)
    elif from_lcase == 'fahrenheit' and to_lcase == "celsius":
        return convertFahrenheitToCelsius(value)
    elif from_lcase == 'fahrenheit' and to_lcase == "kelvin":
        return convertFahrenheitToKelvin(value)
    elif from_lcase == 'kelvin' and to_lcase == "celsius":
        return convertKelvinToCelsius(value)
    elif from_lcase == 'kelvin' and to_lcase == "fahrenheit":
        return convertKelvinToFahrenheit(value)
    elif from_lcase == "miles" and to_lcase == "meters":
        return converMilesToMeters(value)
    else:
        raise ("Unable to process Conversion")