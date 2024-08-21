def num_espejo(num_1:int, num_2:int) -> str:
    txt_1 = str(num_1)
    txt_2 = str(num_2)
    espejo : bool = True
    if len(txt_1) == len(txt_2):
        for n in range (1, len(txt_1)+1):
            if (txt_1[n-1]) != (txt_2[-n]):
                espejo = False
                break
            else:
                espejo = True
    else:
        espejo = False
    
    if espejo == True:
        return(f"los numeros {num_1} y {num_2} son espejos!")
    else:
        return(f"los numeros {num_1} y {num_2} no son espejos...")  

if __name__ == "__main__":
    try:
        num_1 = int(input("ingrese un numero entero:  "))
        num_2 = int(input("ingrese un numero entero:  "))
        espejos= num_espejo(num_1, num_2)
        print(espejos)
    except ValueError:
        print("No has ingresado un numero entero...") 