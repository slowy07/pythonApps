import sys

class colors:
    CYAN = '\033[36m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    RED = '\033[31m'
    ENDC = '\033[0m'

def printColor(color, message):
    print(color + message + colors.ENDC)


printColor(colors.CYAN, sys.argv[1])
printColor(colors.GREEN, sys.argv[1])
printColor(colors.YELLOW, sys.argv[1])
printColor(colors.BLUE, sys.argv[1])
printColor(colors.RED, sys.argv[1])