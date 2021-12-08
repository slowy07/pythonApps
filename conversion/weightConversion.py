KILOGRAM_CHART = {
    "kilogram": 1,
    "gram": pow(10, 3),
    "milligram": pow(10, 6),
    "metric-ton": pow(10, -3),
    "long-ton": 0.0009842073,
    "short-ton": 0.0011023122,
    "pound": 2.2046244202,
    "ounce": 35.273990723,
    "carrat": 5000,
    "atomic-mass-unit": 6.022136652e26,
}

WEIGHT_TYPE_CHART = {
    "kilogram": 1,
    "gram": pow(10, -3),
    "milligram": pow(10, -6),
    "metric-ton": pow(10, 3),
    "long-ton": 1016.04608,
    "short-ton": 907.184,
    "pound": 0.453592,
    "ounce": 0.0283495,
    "carrat": 0.0002,
    "atomic-mass-unit": 1.660540199e-27,
}


def weight_conversion(from_type: str, to_type: str, value: float) -> float:
    if to_type not in KILOGRAM_CHART or from_type not in WEIGHT_TYPE_CHART:
        raise ValueError(
            f"Invalid 'from_type' or 'to_type' value: {from_type!r}, {to_type!r}\n"
            f"Supported values are: {', '.join(WEIGHT_TYPE_CHART)}"
        )
    return value * KILOGRAM_CHART[to_type] * WEIGHT_TYPE_CHART[from_type]


if __name__ == "__main__":

    import doctest

    doctest.testmod()
