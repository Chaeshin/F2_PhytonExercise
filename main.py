def dectobinary(dec):
    bin = ""
    while dec > 0:
        rem = dec % 2
        bin = str(rem) + bin
        dec //= 2
    print("Binary:",bin)
def binaryToN(bin, type):
    if type == 'dec':
        dec = binToDec(bin)
        print("Decimal:", dec)
    if type == 'hex':
        hexa = binToDec(bin)
        decToHex(hexa)
    if type == 'oct':
        octa = binToDec(bin)
        decToOctal(octa)
def decToOctal(dec):
    place = 1
    oct=0
    while dec > 0:
        rem = dec % 8
        oct = oct + rem * place
        dec //= 8
        place *= 10
    print("Octal:", oct)
def decToHex(dec):
    digits = "0123456789ABCDEF"
    hex = ""

    while dec > 0:
        rem = dec % 16
        hexdigit = digits[rem]
        hex = hexdigit + hex
        dec //= 16
    print("Hexadecimal:",hex)
def binToDec(bin):
    length = len(bin)
    dec = 0
    for i in range(length):
        if bin[i] != '0' and bin[i] != '1':#
            print("Invalid binary")
            return
        if bin[i] == '1':
            dec += 2 ** (length - 1 - i)
    return dec
def main():
    dectobin = int(input("Enter decimal to convert for binary:"))
    dectobinary(dectobin)
    dectooct = int(input("Enter decimal to convert for octal:"))
    decToOctal(dectooct)
    dectohex = int(input("Enter decimal to convert for hexadecimal:"))
    decToHex(dectohex)
    binton = input("Enter binary:")
    type = input("Enter type (hex,oct,dec):")
    binaryToN(binton, type)
main()
