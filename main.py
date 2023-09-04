def dectobinary(dec):
    binary_number = ""
    while dec > 0:
        rem = dec % 2
        binary_number = str(rem) + binary_number
        dec //= 2
    print(binary_number)
# def binaryToN(bin, type):
def decToOctal(dec):
    place = 1
    oct=0
    while dec > 0:
        rem = dec % 8
        oct = oct + rem * place
        dec //= 8
        place *= 10
    print(oct)
def decToHex(dec):
    digits = "0123456789ABCDEF"
    hex = ""

    while dec > 0:
        rem = dec % 16
        hexdigit = digits[rem]
        hex = hexdigit + hex
        dec //= 16
    print(hex)
def main():
    dectobin = int(input("Enter decimal to convert for binary:"))
    dectobinary(dectobin)
#     binaryToN(bin, type)
    dectooct = int(input("Enter decimal to convert for octal:"))
    decToOctal(dectooct)
    dectohex = int(input("Enter decimal to convert for hexadecimal:"))
    decToHex(dectohex)

main()
