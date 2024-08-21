def mcm(num_1:int,num_2:int) -> int:
    if num_1 >= num_2 : 
        dividendo = num_1 
        divisor = num_2
    else: 
        dividendo = num_2
        divisor = num_1
    residuo = dividendo % divisor
    while residuo != 0:
        dividendo = divisor
        divisor = residuo
        residuo = dividendo % divisor
    print(divisor)
    return(num_1 * num_2)//(divisor)


if __name__ == "__main__":
    try:
        a = int(input("Ingrese el primer número: "))
        b = int(input("Ingrese el segundo número: "))
        mcm_ = mcm(a, b)
        print(f"el MCM entre {a} y {b} es {mcm_}")
    except ValueError:
        print("el caracter ingresado no es un numero entero...")