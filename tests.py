from conversions import convertCelsiusToKelvin
from conversions import convertCelsiusToFahrenheit
from conversions import convertFahrenheitToCelsius
from conversions import convertFahrenheitToKelvin
from conversions import convertKelvinToCelsius
from conversions import convertKelvinToFahrenheit
from conversions_refactored import convert
import unittest

class test_temperature(unittest.TestCase):    

    
    def test_celsius_to_kelvin(self):
        
        result = convertCelsiusToKelvin(300.00)
        expected = 573.15
        self.assertEqual(result, expected)
        
        result = convertCelsiusToKelvin(0.00)
        expected = 273.15
        self.assertEqual(result, expected)
        
        result = convertCelsiusToKelvin(-40.00)
        expected = 233.15
        self.assertAlmostEqual(result, expected, places = 6)
        
        result = convertCelsiusToKelvin(10)
        expected = 283.15
        self.assertEqual(result, expected)
        
        result = convertCelsiusToKelvin(5.00)
        expected = 278.15
        self.assertEqual(result, expected)


    def test_celsius_to_fahrenheit(self):

        result = convertCelsiusToFahrenheit(300.00)
        expected = 572.00
        self.assertEqual(result, expected)
        
        result = convertCelsiusToFahrenheit(0.00)
        expected = 32.00
        self.assertEqual(result, expected)
        
        result = convertCelsiusToFahrenheit(-40.00)
        expected = -40.00
        self.assertEqual(result, expected)
        
        result = convertCelsiusToFahrenheit(10)
        expected = 50
        self.assertEqual(result, expected)
        
        result = convertCelsiusToFahrenheit(5.00)
        expected = 41.00
        self.assertEqual(result, expected)

    def test_fahrenheit_to_celsius(self):

        result = convertFahrenheitToCelsius(300.00)
        expected = 148.88888888888889
        self.assertAlmostEqual(result, expected, places = 14)
        
        result = convertFahrenheitToCelsius(0.00)
        expected = -17.77777777777778
        self.assertAlmostEqual(result, expected)
        
        result = convertFahrenheitToCelsius(-40.00)
        expected = -40.00
        self.assertEqual(result, expected)
        
        result = convertFahrenheitToCelsius(10)
        expected = -12.222222222222221
        self.assertAlmostEqual(result, expected)
        
        result = convertFahrenheitToCelsius(5.00)
        expected = -15
        self.assertEqual(result, expected)



    def test_fahrenheit_to_kelvin(self):

        result = convertFahrenheitToKelvin(300.00)
        expected = 422.0388888888889
        self.assertAlmostEqual(result, expected, places = 13)
        
        result = convertFahrenheitToKelvin(0.00)
        expected = 255.3722222222222 
        self.assertAlmostEqual(result, expected)
        
        result = convertFahrenheitToKelvin(-40.00)
        expected = 233.14999999999998
        self.assertAlmostEqual(result, expected)
        
        result = convertFahrenheitToKelvin(10)
        expected = 260.92777777777775
        self.assertAlmostEqual(result, expected)
        
        result = convertFahrenheitToKelvin(5.00)
        expected = 258.15
        self.assertEqual(result, expected)

    def test_kelvin_to_celsius(self):

        result = convertKelvinToCelsius(300.00)
        expected = 26.85
        self.assertAlmostEqual(result, expected)
        
        result = convertKelvinToCelsius(0.00)
        expected = -273.15
        self.assertEqual(result, expected)
        
        result = convertKelvinToCelsius(-40.00)
        expected = -313.15
        self.assertEqual(result, expected)
        
        result = convertKelvinToCelsius(10)
        expected = -263.15
        self.assertEqual(result, expected)
        
        result = convertKelvinToCelsius(5.00)
        expected = -268.15
        self.assertEqual(result, expected)

    def test_kelvin_to_fahrenheit(self):

        result = convertKelvinToFahrenheit(300.00)
        expected = 80.33
        self.assertAlmostEqual(result, expected)
        
        result = convertKelvinToFahrenheit(0.00)
        expected = -459.67
        self.assertAlmostEqual(result, expected)
        
        result = convertKelvinToFahrenheit(-40.00)
        expected = -531.67
        self.assertEqual(result, expected)
        
        result = convertKelvinToFahrenheit(10)
        expected = -441.67
        self.assertAlmostEqual(result, expected)
        
        result = convertKelvinToFahrenheit(5.00)
        expected = -450.67
        self.assertAlmostEqual(result, expected)

    def test_convert(self):
        celsius = 0
        result = convert("Celsius", "Kelvin", celsius)
        expected = 273.15
        self.assertEqual(result, expected)

        celsius = 0
        result = convert("Celsius", "Fahrenheit", celsius)
        expected = 32
        self.assertEqual(result, expected)

        fahrenheit = 10
        result = convert("Fahrenheit", "Celsius", fahrenheit)
        expected = -12.222222222222221
        self.assertAlmostEqual(result, expected)

        fahrenheit = 10
        result = convert("Fahrenheit", "Kelvin", fahrenheit)
        expected = 260.92777777777775
        self.assertAlmostEqual(result, expected)

        kelvin = 14
        result = convert("Kelvin", "Celsius", kelvin)
        expected = -259.15
        self.assertEqual(result, expected)

        kelvin = 14
        result = convert("Kelvin", "Fahrenheit", kelvin)
        expected = -434.46999999999997
        self.assertEqual(result, expected)

        miles= 25
        result = convert("miles", "meters", miles)
        expected = 40233.6
        self.assertEqual(result, expected)



if __name__ == '__main__':
    unittest.main()