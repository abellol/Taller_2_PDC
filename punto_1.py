def separar_digitos(num:int) -> list:
    digits = []
    while num > 0:
        digit = num % 10
        digits.insert(0, digit)
        num //= 10
    return digits
if __name__ == "__main__":
    try: 
        num = abs(int(input("ingrese un numero entero:  ")))
        digitos = separar_digitos(num)
        print(digitos)
    except ValueError:
        print("no se ha ingresado un numero entero...")