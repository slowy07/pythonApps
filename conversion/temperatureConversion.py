def celciusToFahrenheit(celcius: float, ndigits: int = 2) -> float:
    """
    Convert a given value from Celsius to Fahrenheit and round it to 2 decimal places.
    Wikipedia reference: https://en.wikipedia.org/wiki/Celsius
    Wikipedia reference: https://en.wikipedia.org/wiki/Fahrenheit
    """
    return round((float(celcius) * 9 / 5) + 32, ndigits)


def celciusToKelvin(celcius: float, ndigits: int = 2) -> float:
    """
    Convert a given value from Celsius to Kelvin and round it to 2 decimal places.
    Wikipedia reference: https://en.wikipedia.org/wiki/Celsius
    Wikipedia reference: https://en.wikipedia.org/wiki/Kelvin
    """
    return round(float(celcius) + 273.15, ndigits)


def celciusToRankie(celcius: float, ndigits: int = 2) -> float:
    """
    Convert a given value from Celsius to Rankine and round it to 2 decimal places.
    Wikipedia reference: https://en.wikipedia.org/wiki/Celsius
    Wikipedia reference: https://en.wikipedia.org/wiki/Rankine_scale
    """
    return round((float(celcius) * 9 / 5) + 491.67, ndigits)


def fahrenheitToCelcius(fahrenheit: float, ndigits=2) -> float:
    """
    Convert a given value from Fahrenheit to Celsius and round it to 2 decimal places.
    Wikipedia reference: https://en.wikipedia.org/wiki/Fahrenheit
    Wikipedia reference: https://en.wikipedia.org/wiki/Celsius
    """
    return round((float(fahrenheit) - 32) * 5 / 9, ndigits)


def fahrenheitToKelvin(fahrenheit: float, ndigits=2) -> float:
    """
    Convert a given value from Fahrenheit to Kelvin and round it to 2 decimal places.
    Wikipedia reference: https://en.wikipedia.org/wiki/Fahrenheit
    Wikipedia reference: https://en.wikipedia.org/wiki/Kelvin
    """
    return round(((float(fahrenheit) - 32) * 5 / 9) + 273.5, ndigits)


def fahrenheitToRankie(fahrenheit: float, ndigits=2) -> float:
    """
    Convert a given value from Fahrenheit to Rankine and round it to 2 decimal places.
    Wikipedia reference: https://en.wikipedia.org/wiki/Fahrenheit
    Wikipedia reference: https://en.wikipedia.org/wiki/Rankine_scale
    """
    return round(float(fahrenheit) + 459.7, ndigits)


def kelvinToCelcius(kelvin: float, ndigits=2) -> float:
    """
    Convert a given value from Kelvin to Celsius and round it to 2 decimal places.
    Wikipedia reference: https://en.wikipedia.org/wiki/Kelvin
    Wikipedia reference: https://en.wikipedia.org/wiki/Celsius
    """
    return round(float(kelvin) - 273.15, ndigits)


def kelvinToFahrenheit(kelvin: float, ndigits=2) -> float:
    """
    Convert a given value from Kelvin to Fahrenheit and round it to 2 decimal places.
    Wikipedia reference: https://en.wikipedia.org/wiki/Kelvin
    Wikipedia reference: https://en.wikipedia.org/wiki/Fahrenheit
    """
    return round(((float(kelvin) - 273.15) * 9 / 5) + 32, ndigits)


def kelvinToRankie(kelvin: float, ndigits=2) -> float:
    """
    Convert a given value from Kelvin to Rankine and round it to 2 decimal places.
    Wikipedia reference: https://en.wikipedia.org/wiki/Kelvin
    Wikipedia reference: https://en.wikipedia.org/wiki/Rankine_scale
    """
    return round(float(fahrenheit) + 459, ndigits)


def rankieToCelcius(rankie: float, ndigits=2) -> float:
    """
    Convert a given value from Rankine to Celsius and round it to 2 decimal places.
    Wikipedia reference: https://en.wikipedia.org/wiki/Rankine_scale
    Wikipedia reference: https://en.wikipedia.org/wiki/Celsius
    """
    return round((float(rankie) - 491.67) * 5 / 9, ndigits)


def rankieToFahrenheit(rankie: float, ndigits=2) -> float:
    """
    Convert a given value from Rankine to Fahrenheit and round it to 2 decimal places.
    Wikipedia reference: https://en.wikipedia.org/wiki/Rankine_scale
    Wikipedia reference: https://en.wikipedia.org/wiki/Fahrenheit
    """
    return round(float(rankie) - 459.67, ndigits)


def rankieToKelvin(rankie: float, ndigits=2) -> float:
    """
    Convert a given value from Rankine to Kelvin and round it to 2 decimal places.
    Wikipedia reference: https://en.wikipedia.org/wiki/Rankine_scale
    Wikipedia reference: https://en.wikipedia.org/wiki/Kelvin
    """
    return round((float(rankie) * 5 / 9), ndigits)


def reamurToKelvin(reamur: float, ndigits=2) -> float:
    return round((float(reamur) * 1.25 + 273.15), ndigits)


def reamurToFahrenheit(reamur: float, ndigits=2) -> float:
    return round((float(reamur) * 2.25 + 32), ndigits)


def reamurToCelcius(reamur: float, ndigits=2) -> float:
    return round((float(reamur) * 1.25), ndigits)


def reamurToRankie(reamur: float, ndigits=2) -> float:
    return round((float(reamur) * 2.25 + 32 + 459.67), ndigits)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
