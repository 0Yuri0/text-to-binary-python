print("***Conversor de frases para codigo binário***")
frase = str(input("Digite uma frase: "))
resultado = "null"
num_caracteres = len(frase)
caracter = list(frase)
cont = 0
final=""

print("\nResultado: ")

while (cont<num_caracteres):
    match caracter[cont]:
        case ' ':
            resultado = "00100000"
        case "'":
            resultado = "00100111"
        case '!':
            resultado = "00100001"
        case '"':
            resultado = "00100010"
        case '#':
            resultado = "00100011"
        case '$':
            resultado = "00100100"
        case '%':
            resultado = "00100101"
        case '&':
            resultado = "00100110"
        case '(':
            resultado = "00101000"
        case ')':
            resultado = "00101001"
        case '*':
            resultado = "00101010"
        case '+':
            resultado = "00101011"
        case ',':
            resultado = "00101100"
        case '-':
            resultado = "00101101"
        case '.':
            resultado = "00101110"
        case '/':
            resultado = "00101111"
        case ':':
            resultado = "00111010"
        case ';':
            resultado = "00111011"
        case '<':
            resultado = "00111100"
        case '=':
            resultado = "00111101"
        case '>':
            resultado = "00111110"
        case '?':
            resultado = "00111111"
        case '@':
            resultado = "01000000"
        case '[':
            resultado = "01011011"
        case ']':
            resultado = "01011101"
        case '^':
            resultado = "01011110"
        case '_':
            resultado = "01011111"
        case '`':
            resultado = "01100000"
        #Números
        case '0':
            resultado = "00110000"
        case '1':
            resultado = "00110001"
        case '2':
            resultado = "00110010"
        case '3':
            resultado = "00110011"
        case '4':
            resultado = "00110100"
        case '5':
            resultado = "00110101"
        case '6':
            resultado = "00110110"
        case '7':
            resultado = "00110111"
        case '8':
            resultado = "00111000"
        case '9':
            resultado = "00111001"
        #Letras minúsculas
        case 'a':
            resultado = "01100001"
        case 'b':
            resultado = "01100010"
        case 'c':
            resultado = "01100011"
        case 'd':
            resultado = "01100100"
        case 'e':
            resultado = "01100101"
        case 'f':
            resultado = "01100110"
        case 'g':
            resultado = "01100111"
        case 'h':
            resultado = "01101000"
        case 'i':
            resultado = "01101001"
        case 'j':
            resultado = "01101010"
        case 'k':
            resultado = "01101011"
        case 'l':
            resultado = "01101100"
        case 'm':
            resultado = "01101101"
        case 'n':
            resultado = "01101110"
        case 'o':
            resultado = "01101111"
        case 'p':
            resultado = "01110000"
        case 'q':
            resultado = "01110001"
        case 'r':
            resultado = "01110010"
        case 's':
            resultado = "01100001"
        case 't':
            resultado = "01110100"
        case 'u':
            resultado = "01110101"
        case 'v':
            resultado = "01110110"
        case 'w':
            resultado = "01110111"
        case 'x':
            resultado = "01111000"
        case 'y':
            resultado = "01111001"
        case 'z':
            resultado = "01111010"
        #Letras maiúsculas
        case 'A':
            resultado = "01000001"
        case 'B':
            resultado = "01000010"
        case 'C':
            resultado = "01000011"
        case 'D':
            resultado = "01000100"
        case 'E':
            resultado = "01000101"
        case 'F':
            resultado = "01000110"
        case 'G':
            resultado = "01000111"
        case 'H':
            resultado = "01001000"
        case 'I':
            resultado = "01001001"
        case 'J':
            resultado = "01001010"
        case 'K':
            resultado = "01001011"
        case 'L':
            resultado = "01001100"
        case 'M':
            resultado = "01001101"
        case 'N':
            resultado = "01001110"
        case 'O':
            resultado = "01001111"
        case 'P':
            resultado = "01010000"
        case 'Q':
            resultado = "01010001"
        case 'R':
            resultado = "01010010"
        case 'S':
            resultado = "01010011"
        case 'T':
            resultado = "01010100"
        case 'U':
            resultado = "01010101"
        case 'V':
            resultado = "01010110"
        case 'W':
            resultado = "01010111"
        case 'X':
            resultado = "01011000"
        case 'Y':
            resultado = "01011001"
        case 'Z':
            resultado = "01011010"
        #Símbolos
        case 'Ç':
            resultado = "10000000"
        case 'ü':
            resultado = "10000001"
        case 'é':
            resultado = "10000010"
        case 'â':
            resultado = "10000011"
        case 'ä':
            resultado = "10000100"
        case 'à':
            resultado = "10000101"
        case 'å':
            resultado = "10000110"
        case 'ç':
            resultado = "10000111"
        case 'ê':
            resultado = "10001000"
        case 'ë':
            resultado = "10001001"
        case 'è':
            resultado = "10001010"
        case 'ï':
            resultado = "10001011"
        case 'î':
            resultado = "10001100"
        case 'ì':
            resultado = "10001101"
        case 'Ä':
            resultado = "10001110"
        case 'Å':
            resultado = "10001111"
        case 'É':
            resultado = "10010000"
        case 'æ':
            resultado = "10010001"
        case 'Æ':
            resultado = "10010010"
        case 'ô':
            resultado = "10010011"
        case 'ö':
            resultado = "10010100"
        case 'ò':
            resultado = "10010101"
        case 'û':
            resultado = "10010110"
        case 'ù':
            resultado = "10010111"
        case 'ÿ':
            resultado = "10011000"
        case 'Ö':
            resultado = "10011001"
        case 'Ü':
            resultado = "10011010"
        case 'ø':
            resultado = "10011011"
        case '£':
            resultado = "10011100"
        case 'Ø':
            resultado = "10011101"
        case '×':
            resultado = "10011110"
        case 'ƒ':
            resultado = "10011111"
        case 'á':
            resultado = "10100000"
        case 'ù':
            resultado = "10100001"
        case 'ó':
            resultado = "10100010"
        case 'ú':
            resultado = "10100011"
        case 'ñ':
            resultado = "10100100"
        case 'Ñ':
            resultado = "10100101"
        case 'ª':
            resultado = "10100110"
        case 'º':
            resultado = "10100111"
        case '¿':
            resultado = "10101000"
        case '®':
            resultado = "10101001"
        case '¬':
            resultado = "10101010"
        case '½':
            resultado = "10101011"
        case '¼':
            resultado = "10101100"
        case '¡':
            resultado = "10101101"
        case '«':
            resultado = "10101110"
        case '»':
            resultado = "10101111"
        case '░':
            resultado = "10110000"
        case '▒':
            resultado = "10110001"
        case '▓':
            resultado = "10110010"
        case '│':
            resultado = "10110011"
        case '┤':
            resultado = "10110100"
        case 'Á':
            resultado = "10110101"
        case 'Â':
            resultado = "10110110"
        case 'À':
            resultado = "10110111"
        case '©':
            resultado = "10111000"
        case '╣':
            resultado = "10111001"
        case '║':
            resultado = "10111010"
        case '╗':
            resultado = "10111011"
        case '╝':
            resultado = "10111100"
        case '¢':
            resultado = "10111101"
        case '¥':
            resultado = "10111110"
        case '┐':
            resultado = "10111111"
        case '└':
            resultado = "11000000"
        case '┴':
            resultado = "11000001"
        case '┬':
            resultado = "11000010"
        case '├':
            resultado = "11000011"
        case '─':
            resultado = "11000100"
        case '┼':
            resultado = "11000101"
        case 'ã':
            resultado = "11000110"
        case 'Ã':
            resultado = "11000111"
        case '╚':
            resultado = "11001000"
        case '╔':
            resultado = "11001001"
        case '╩':
            resultado = "11001010"
        case '╦':
            resultado = "11001011"
        case '╠':
            resultado = "11001100"
        case '═':
            resultado = "11001101"
        case '╬':
            resultado = "11001110"
        case '¤':
            resultado = "11001111"
        case 'ð':
            resultado = "11010000"
        case 'Ð':
            resultado = "11010001"
        case 'Ê':
            resultado = "11010010"
        case 'Ë':
            resultado = "11010011"
        case 'È':
            resultado = "11010100"
        case 'ı':
            resultado = "11010101"
        case 'Í':
            resultado = "11010110"
        case 'Î':
            resultado = "11010111"
        case 'Ï':
            resultado = "11011000"
        case '┘':
            resultado = "11011001"
        case '┌':
            resultado = "11011010"
        case '█':
            resultado = "11011011"
        case '▄':
            resultado = "11011100"
        case '¦':
            resultado = "11011101"
        case 'Ì':
            resultado = "11011110"
        case '▀':
            resultado = "11011111"
        case 'Ó':
            resultado = "11100000"
        case 'ß':
            resultado = "11100001"
        case 'Ô':
            resultado = "11100010"
        case 'Ò':
            resultado = "11100011"
        case 'õ':
            resultado = "11100100"
        case 'Õ':
            resultado = "11100101"
        case 'µ':
            resultado = "11100110"
        case 'þ':
            resultado = "11100111"
        case 'Þ':
            resultado = "11101000"
        case 'Ú':
            resultado = "11101001"
        case 'Û':
            resultado = "11101010"
        case 'Ù':
            resultado = "11101011"
        case 'ý':
            resultado = "11101100"
        case 'Ý':
            resultado = "11101101"
        case '¯':
            resultado = "11101110"
        case '´':
            resultado = "11101111"
        case '±':
            resultado = "11110001"
        case '‗':
            resultado = "11110010"
        case '¾':
            resultado = "11110011"
        case '¶':
            resultado = "11110100"
        case '§':
            resultado = "11110101"
        case '÷':
            resultado = "11110110"
        case '¸':
            resultado = "11110111"
        case '°':
            resultado = "11111000"
        case '¨':
            resultado = "11111001"
        case '·':
            resultado = "11111010"
        case '¹':
            resultado = "11111011"
        case '³':
            resultado = "11111100"
        case '²':
            resultado = "11111101"
        case '■':
            resultado = "11111110"

        case _:
            print("?")
    final = final + " " + str(resultado)
    cont = cont+1
print(final)
print("\nFim do programa.")
