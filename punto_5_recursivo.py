def mcd(num_1:int,num_2:int) -> int:
    if num_1 >= num_2 : 
        dividendo = num_1 
        divisor = num_2
    else: 
        dividendo = num_2
        divisor = num_1

    if divisor == 0:
        return num_1
    return  mcd(divisor, dividendo % divisor)

def mcm(num_1, num_2) -> int:
    return (num_1 * num_2) // (mcd(num_1, num_2))

if __name__ == "__main__":
    try:
        a = int(input("Ingrese el primer número: "))
        b = int(input("Ingrese el segundo número: "))
        mcm_ = mcm(a, b)
        print(f"el MCM entre {a} y {b} es {mcm_}")
    except ValueError:
        print("el caracter ingresado no es un numero entero...")