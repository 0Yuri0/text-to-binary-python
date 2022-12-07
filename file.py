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
        case _:
            print("?")
    final = final + " " + str(resultado)
    cont = cont+1
print(final)
print("\nFim do programa.")
