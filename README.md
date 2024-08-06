# Taller_2_PDC
#### Somos Alejandro Bello, Malcom Carrillo y Rafael Chirivi y somos el grupo de "Fenomenoides", adjunto nuestro logo: 

<details>
  <summary>Preparense para ver el grandioso logo:</summary>
  <div style="text-align: center;">
    <img src="https://i.postimg.cc/NMtWfYg8/logo-def.png" alt="Logo grandioso" width="400" height="auto"/>
    <div style="text-align: center;"><b>"somos programadores, no diseñadores"</b></div>
  </div>
</details>

#### A continuación presentaremos la solución propuesta para cada numeral del taller:
### 1. Desarrollar un programa que ingrese un número entero n y separe todos los digitos que componen el número.


```python
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
```
### 2. Desarrollar un programa que ingrese un número flotante n y separe su parte entera de la parte decimal, y luego entregue los dígitos tanto de la parte entera como de la decimal.
```python
def separar_digitos(numero) -> list:
    digitos = []
    while numero > 0:
        digito = numero % 10
        digitos.insert(0, digito)  
        numero = numero // 10
    return digitos

def parts(number:float) -> str:
    integer = int(number)
    decimal = number - integer
    while decimal != int(decimal):
        decimal *= 10
    decimals = separar_digitos(int(decimal))
    integers = separar_digitos(integer)
    return f"La parte entera es {integers} y la decimal es {decimals}"

if __name__ == "__main__":
    try:
        num = abs(float(input("ingrese un numero real:  ")))
        digits = parts(num)
        print(digits)
    except ValueError:
        print("no ha ingresado un numero real...")
```
### 3. Desarrollar un programa que permita ingresar dos números enteros y determinar si se tratan de números espejos, definiendo números espejos como dos números a y b tales que a se lee de izquierda a derecha igual que se lee b de derecha a izquierda, y viceversa.
```python
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
```
### 4. Diseñar una función que permita calcular una aproximación de la función coseno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Taylor. nota: use math para traer la función coseno y mostrar la diferencia entre el valor real y la aproximación. Calcule con cuántos términos de la serie (i.e: cuáles valores de n), se tienen errores del 10%, 1%, 0.1% y 0.001%. 
```math
cos(x) \approx cos(x,n) \approx \sum_{i=0}^{n} (-1)^i \frac{x^{2i}}{(2i)!}
```

```python
import math
def cos_aproximada(x : float, n : int) -> float:
    suma : float = 0
    for i in range (0,n+1):
        arg = 2 * i
        num = (-1)**i *(x**(arg))
        deno = 1
        for j in range (1, arg + 1):
            deno *= j
        termino = num/ deno
        suma += termino
    return suma

def margen_error(real : float, aprox : float) -> float:
    if real == 0:
        return 0
    numerador = (abs(real - aprox))
    denominador = real
    error : float = numerador / denominador * 100
    if denominador > 0:
        return error
    else:
       return -error
    
def calcular_terminos(x:float, porcentaje_error:float) -> str:
    real = math.cos(x)
    i = 1
    error = float(100) # el error inicia en el 100%
    while  error >= porcentaje_error:
        aprox = cos_aproximada(x, i)
        error = margen_error(real, aprox)
        i+=1
    info = f"""
	El valor estimado de la función cos({x}) = {aprox}
	El valor real de la función cos({x}) = {real}
	Al sumar {i} términos de la serie, el error es del {error}% y es menor al {porcentaje_error}%
					"""
    i+=1
    return info
    
if __name__ == "__main__":   
    try: 
        x = float(input("Ingrese un numero real para calcular la función:  "))
        porcentaje_errores = [10, 1, 0.1, 0.001]

        for porcentaje_error in porcentaje_errores:
            print(calcular_terminos(x, porcentaje_error))
            
    except ValueError:
        print("no has ingresado un numero real...")
```
### 5. Desarrollar un programa que permita determinar el Minimo Comun Multiplo de dos numeros enteros. Abordar el problema desde una perpectiva tanto iterativa como recursiva.
```python
def mcm(num_1:int,num_2:int) -> float:
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
    return(num_1 * num_2)/(divisor)


if __name__ == "__main__":
    try:
        a = int(input("Ingrese el primer número: "))
        b = int(input("Ingrese el segundo número: "))
        mcm_ = mcm(a, b)
        print(f"el MCM entre {a} y {b} es {mcm_}")
    except ValueError:
        print("el caracter ingresado no es un numero entero...")
```
### 6. Desarrollar un programa que determine si en una lista existen o no elementos repetidos.
```python
def elementos_repetidos(lista:list) -> bool:
    x = 1
    equal : bool = False
    for n in lista:
        for i in range(x, len(lista)):
            if n == (lista[i]):
                equal = True
                break
            else:
                continue
        x += 1
    return equal

if __name__ == "__main__": 
    try:
        a : list = [1, 2, 3, 4, "4", "c"]
        b : list = [5, 9, "agua", 9, "g", "h"]
        ejemplo_1 = elementos_repetidos(a)
        ejemplo_2 = elementos_repetidos(b)
        print(ejemplo_1)
        print(ejemplo_2)
    except ValueError:
        print("algun caracter ingresado no es valido...")

```
### 7. Desarrollar un programa que determine si en una lista se encuentra una cadena de caracteres con dos o más vocales. Si la cadena existe debe imprimirla y si no existe debe imprimir 'No existe'.
```python

```
### 8. Desarrollar un programa que dadas dos listas determine que elementos tiene la primer lista que no tenga la segunda lista.
```python
def no_repetidos(lista_1:list, lista_2:list):
    c = lista_1.copy()
    for element in lista_1:
        for i in range(len(lista_2)):
            if element == lista_2[i]:
                c.remove(element)
                break
            else:
                continue
    return (f"los elementos que estan en {lista_1} y no en {lista_2} son: {c}")

if __name__ == "__main__":
    try:
        A = [1, "a", 34, "14"]
        B = ["a", 34, 128, 14]
        no_repeat = no_repetidos(A, B)
        print(no_repeat)
    except ValueError:
        print("algun caracter ingresado no es valido...")
```

### 9. Resolver el punto 7 del taller 1 usando operaciones con vectores.
```python
def promedio(lista:list) -> float:
  suma : float = 0
  for n in lista:
    suma += n
  prom = suma / len(lista)
  return (f"El promedio de su lista {lista} es de: {prom}")
def mediana(lista:list) -> float:
  lista.sort()
  if (len(lista) % 2) == 0:
    num = lista[len(lista)//2] + lista[(len(lista)//2) - 1]
    med = num / 2
    return (f"la mediana de su lista {lista} datos es: {med}")
  else:
    med = lista[len(lista)//2]
    return (f"la mediana de su lista {lista} datos es: {med}")
def prom_multi(lista : list) -> float:
	multi : float = 1
	for n in lista:
		multi *= n
	prom = multi ** (1/len(lista))
	return (f"el promedio multiplicativo de la lista {lista} es: {prom}")
def asce(lista:list) -> list:
	lista.sort()
	return (f"la lista ordenada de forma ascendente es: {lista}")
def desc(lista:list) -> list:
  lista.sort(reverse=True)
  return (f"la lista ordenada de forma descendente es: {lista}")
def potencia_extremos(lista:list) -> float:
  lista.sort()
  base = lista[-1]
  exponente = lista[0]
  pot = base ** exponente
  return (f"{base} ^ {exponente} = {pot}")
def raiz_menor(lista:list)->float:
	lista.sort()
	raiz = lista[0] ** (1/3)
	return (f"la raíz cubica del menor elementro dentro de la lista ({lista[0]}) es: {raiz}")
if __name__ == "__main__":
    try:
        lista = []
        for i in range(1, 7):
            x = int(input(f"Ingrese el dato {i}:  "))
            lista.append(x)
            
        print (promedio(lista))
        print (mediana(lista))
        print (prom_multi(lista))
        print (asce(lista))
        print (desc(lista))
        print (potencia_extremos(lista))
        print (raiz_menor(lista))
    except ValueError:
        print("no has ingresado un numero entero...")
```

### 10. Suponga que se tiene una lista A con ciertos números enteros. Desarrolle una función que, independientemente de los números que se encuentran en la lista A, tome aquellos números que son múltiplos de 3 y los guarde en una lista nueva, la cual debe ser retornada por la función. Implemente la perspectiva de un patrón de acumulación y también de comprensión de listas.
```python
def multiplo_3(lista:list) -> list:
    new_list = [-x if x < 0 else x for x in lista if x%3==0]
    return new_list

if __name__ == "__main__":
    A = [1, 2, 4, 8]
    B = [0, 3, 6, 9, 12, -15, 8,-999999, 10842630]

    d = multiplo_3(B)
    print(d)
``` 
```python
def separar_digitos(numero) -> list:
    digitos = []
    if numero < 0:
        numero = -numero
    while numero > 0:
        digito = numero % 10
        digitos.insert(0, digito)  
        numero = numero // 10

    return digitos

def multiplo(lista:list) -> list: # resta apenas se suman los digitos
    new_list = []
    for element in lista:
        digitos = separar_digitos(element)
        suma = 0
        for number in digitos:
            suma += number
        while suma >= 3:
            suma -= 3
            if suma == 0:
                new_list.append(element)
            
    return new_list
            
if __name__ == "__main__":
    A = [1, 2, 4, 8]
    B = [0, 3, 6, 9, 12, 15, 8, 999999]

    d = multiplo(B)
    print(d)
```


<details>
<summary>Bonus...</summary>
  11. Desarrollar un algoritmo que determine si una matriz es mágica. Se dice que una matriz cuadrada es mágica si la suma de cada una de sus filas, de cada una de sus columnas y de cada diagonal es igual.
  
```python
def imprimir_matriz(mat):
  for i in mat:
    print (i)
def matriz_magica(matriz_1):
    x = len(matriz_1) - 1
    fila= []
    columna = []
    diagonales = []
    sumad1 = 0
    sumad2 = 0
    magic = True
    for i in range (len(matriz_1)):
        sumafila = 0
        sumacolumna = 0
        sumad1 += (matriz_1[i][i])
        sumad2 += (matriz_1[i][i+x])
        x -= 2
        for j in range(len(matriz_1[0])):
            sumafila += (matriz_1[i][j])
            sumacolumna += (matriz_1[j][i])
        fila.append(sumafila)
        columna.append(sumacolumna)
    diagonales.append(sumad1)
    diagonales.append(sumad2)
    y = sumad1
    new_list = [fila, columna, diagonales]
    for element in new_list:
        for num in element:
            if num != y:
                magic = False
                break
            break
    if magic == True:
        return (f"Es una matriz magica con suma en \nfilas: {fila} \ncolumnas: {columna} \ndiagonales: {diagonales}\n")
    else:
        return (f"No es una matriz magica con suma en \nfilas: {fila} \ncolumnas: {columna} \ndiagonales: {diagonales}\n")

if __name__ == "__main__":
	matriz_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	matriz_2 = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
	imprimir_matriz(matriz_1)
	print(matriz_magica(matriz_1))
	print("-------------------------------- \n")
	imprimir_matriz(matriz_2)
	print(matriz_magica(matriz_2))
```



