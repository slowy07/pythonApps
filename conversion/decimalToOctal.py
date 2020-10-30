import math

def decimalToOctal(num: int)->str:
    octal = 0
    counter = 0
    while num > 0:
        remainder = num % 8
        octal = octal + (remainder * math.pow(10, counter))
        counter += 1
        num = math.floor(num / 8)

    return (f"0o{int(octal)}")

def main():
    print("\n2 in octal is:")
    print(decimalToOctal(2))  # = 2
    print("\n8 in octal is:")
    print(decimalToOctal(8))  # = 10
    print("\n65 in octal is:")
    print(decimalToOctal(65))  # = 101
    print("\n216 in octal is:")
    print(decimalToOctal(216))  # = 330
    print("\n512 in octal is:")
    print(decimalToOctal(512))  # = 1000
    print("\n")

if __name__ == '__main__':
    main()
