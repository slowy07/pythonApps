from enum import Enum
from typing import Union

class SI_Unit(Enum):
    yotta = 24
    zetta = 21
    exa = 18
    peta = 15
    tera = 12
    giga = 9
    mega = 6
    kilo = 3
    hecto = 2
    deca = 1
    deci = -1
    centi = -2
    milli = -3
    micro = -6
    nano = -9
    pico = -12
    femto = -15
    atto = -18
    zepto = -21
    yocto = -24


class binaryUnit(Enum):
    yotta = 8
    zetta = 7
    exa = 6
    peta = 5
    tera = 4
    giga = 3
    mega = 2
    kilo = 1

def convertSiPrefix(
    knowAmount: float,
    knowPrefix : Union[str, SI_Unit]
    unknownPrefix: Union[str, SI_Unit]
) -> float:
    if isinstance(knowPrefix, str):
        knowPrefix: SI_Unit = SI_Unit[knowPrefix.lower()]
    if isinstance(unknownPrefix, str):
        unknownPrefix: SI_Unit = SI_Unit[unknownPrefix.lower()]
    unknownAmount = knowAmount * (10 ** (knowPrefix.value - unknownPrefix.value))
    return unknownAmount

def convertToBinaryPrefix(
    knowAmount: float,
    knowPrefix: Union[str, binaryUnit]
    unknownPrefix: Union[str, binaryUnit]
)->str:
    if isinstance(knowPrefix, str):
        knowPrefix: binaryUnit = binaryUnit[knowPrefix.lower()]
    if isinstance(unknownPrefix, str):
        unknownPrefix: binaryUnit = binaryUnit[unknownPrefix.lower()]
    unknownAmount = knowAmount *(
        2 ** ((knowPrefix.value - unknownPrefix.value) * 10)
    )
    return unknownAmount

if __name__ == '__main__':
    import doctest
    doctest.testmod()
