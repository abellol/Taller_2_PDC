# Taller_2_PDC
#### Somos Alejandro Bello, Malcom Carrillo y Rafael Chirivi y somos el grupo de "Fenomenoides", aquí les presentamos nuestro logo: 

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
def separar_digitos(num:int) -> list:	# se define la funcion "separar_digitos"
    digits = []				# se establece una lista en donde registrar los digitos del numero
    while num > 0:			# condicion para que el numero tenga al menos 1 digito
        digit = num % 10		# se obtiene el residuo de dividir entre 10 al numero, dandonos asi el ultimo digito
        digits.insert(0, digit)		# se inserta en la primera posicion de la lista el digito obtenido
        num //= 10			# se remueve ese ultimo digito haciendo division exacta entre 10 
    return digits
if __name__ == "__main__":
    try: 							# limite para ingreso de valores
        num = abs(int(input("ingrese un numero entero:  ")))	# ingreso del numero entero, con funcion de absoluto para incluir numeros positivos o negativos
        digitos = separar_digitos(num)				# llamada a la funcion sobre la variable recien ingresada
        print(digitos)						# impresion de la lista de digitos 
    except ValueError:						# en caso de ingreso de datos diferente al de numeros enteros
        print("no se ha ingresado un numero entero...")
```
### 2. Desarrollar un programa que ingrese un número flotante n y separe su parte entera de la parte decimal, y luego entregue los dígitos tanto de la parte entera como de la decimal.
```python
def separar_digitos(numero) -> list:
    """
	Esta función separa los digitos de un numero en un arreglo en el que cada elemento es uno de los digitos
  
  Args:
    Esta función toma como entrada un número entero y de manera iterativa opera el numero hasta remover los digitos del numero
	agregandolos a un arreglo 
  
  Returns:
    La función retorna un arreglo en el que los elementos son cada digito del numero ingresado en orden
	"""

    digitos = [] 
    while numero > 0:
        digito = numero % 10
        digitos.insert(0, digito) #Inserta digito como el primer elemento del arreglo  
        numero = numero // 10 
    return digitos

def parts(number:float) -> str:

    """
	La función parts separa la parte entera de un numero real de su parte decimal
  
  Args:
    La función toma un numero real o flotante como su entrada, separando primero la parte entera del numero para posteriormente operar la decimal y convertirla en entera
	antes de aplicar la función separar_digitos a ambas partes
  
  Returns:
    La función retorna un string que muestra los arreglos de la parte entera y la parte decimal del numero
	"""

    integer = int(number)
    decimal = number - integer
    while decimal != int(decimal): #Iterar hasta que todos los digitos de la parte decimal hagan parte del entero 
        decimal *= 10
    decimals = separar_digitos(int(decimal))
    integers = separar_digitos(integer)
    return f"La parte entera es {integers} y la decimal es {decimals}"

if __name__ == "__main__":
    try:
	# se pide ingresar un numero real y se asegura que la variable almacene la entrada como un flotante positivo
        num = abs(float(input("ingrese un numero real:  ")))
        digits = parts(num)
        print(digits)
    except ValueError: #Evaluar si ocurre error debido a que lo ingresado era diferente a un numero
        print("no ha ingresado un numero real...")
```
### 3. Desarrollar un programa que permita ingresar dos números enteros y determinar si se tratan de números espejos, definiendo números espejos como dos números a y b tales que a se lee de izquierda a derecha igual que se lee b de derecha a izquierda, y viceversa.
```python
def num_espejo(num_1:int, num_2:int) -> str:			# se define la funcion "num_espejo"
    txt_1 = str(num_1)						# se convierte a texto el primer numero y se asigna a txt_1
    txt_2 = str(num_2)						# se convierte a texto el segundo numero y se asigna a txt_2
    espejo : bool = True					# se establece una variable de tipo booleano para la comparacion de los numeros
    if len(txt_1) == len(txt_2):				# condicion para que la longitud de la cadena (numero de digitos) sea la misma
        for n in range (1, len(txt_1)+1):			# recorrido para los digitos de los numeros
            if (txt_1[n-1]) != (txt_2[-n]):			# comparacion de los digitos (primero con ultimo, segundo con penultimo...)
                espejo = False					# si se cumple que alguno de los numeros no es igual, se declara el booleano como falso
                break
            else:						# caso contrario, donde todos los numeros coinciden en sus posiciones contrarias, booleano como verdadero
                espejo = True
    else:							# si se determina que los numeros no tienen la misma cantidad de digitos, el booleano tambien es falso
        espejo = False
    
    if espejo == True:
        return(f"los numeros {num_1} y {num_2} son espejos!")	# retorno para booleano verdadero
    else:
        return(f"los numeros {num_1} y {num_2} no son espejos...")  # retorno para booleano falso

if __name__ == "__main__":
    try:							# limite para ingreso de valores
        num_1 = int(input("ingrese un numero entero:  "))	# ingreso del primer numero
        num_2 = int(input("ingrese un numero entero:  "))	# ingreso del segundo numero
        espejos= num_espejo(num_1, num_2)			# se asigna a una variable la aplicacion de la funcion sobre los numeros ingresados
        print(espejos)						# impresion del resultado de la funcion
    except ValueError:						# en caso de ingreso de datos diferente al de numeros enteros
        print("No has ingresado un numero entero...") 
```
### 4. Diseñar una función que permita calcular una aproximación de la función coseno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Taylor. nota: use math para traer la función coseno y mostrar la diferencia entre el valor real y la aproximación. Calcule con cuántos términos de la serie (i.e: cuáles valores de n), se tienen errores del 10%, 1%, 0.1% y 0.001%. 
```math
cos(x) \approx cos(x,n) \approx \sum_{i=0}^{n} (-1)^i \frac{x^{2i}}{(2i)!}
```

```python
import math # Se importa el modulo math para la función de coseno
def cos_aproximada(x : float, n : int) -> float:
 """
	La función cos_aproximada calcula una aproximación al coseno usando la serie de Taylor
  
  Args:
    Las entradas de la función son x como el numero real del cual se obtendrá el coseno y un numero n entero que representa el n termino o iteración de la serie de Taylor 
  
  Returns:
    La función retorna el resultado de la operación de la sumatoria en esta iteración de la serie
	"""

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
 """
	Esta función calcula el margen de error del coseno obtenido por el aproximado con la serie de Taylor
  
  Args:
    Los argumentos recibidos son real, que es el coseno real obtenido por el modulo math, y aprox el coseno
	 obtenido de la función cos_aproximada ambos como flotantes
  
  Returns:
    Retorna el error calculado
	"""
    if real == 0:
        return 0
    numerador = (abs(real - aprox)) # Se calcula la diferencia entre el valor real y el aproximado
    denominador = real
    error : float = numerador / denominador * 100
    if denominador > 0: #confirmar output positivo
        return error
    else:
       return -error
    
def calcular_terminos(x:float, porcentaje_error:float) -> str:
"""
	La función calcular_terminos es la que obtiene todos los elementos de la respuesta que se le da al usuario
  
  Args:
    A la función entra x que es el numero del cual se va a calcular el seno y el porcentaje de error con el que lo está calculando
  
  Returns:
    La función retorna un texto con el valor real, estimado, numero de iteraciones y porcentaje de error del coseno del numero x ingresado
	"""
    real = math.cos(x)
    i = 1
    error = float(100) # el error inicia en el 100%
    while  error >= porcentaje_error: #Repetir hasta alcanzar el porcentaje de error ingresado como argumento
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
            
    except ValueError: #Prevenir la entrada de un dato no numerico
        print("no has ingresado un numero real...")
```
### 5. Desarrollar un programa que permita determinar el Minimo Comun Multiplo de dos numeros enteros. Abordar el problema desde una perpectiva tanto iterativa como recursiva.
#### Iterativa:
```python
def mcm(num_1:int,num_2:int) -> int:	# se define la funcion "mcm" iterativa
    if num_1 >= num_2 : 		# condicion para establecer al dividendo y divisor en donde el primer numero es mayor al segundo
        dividendo = num_1 
        divisor = num_2
    else: 				# condicion para establecer al dividendo y divisor en donde el segundo numero es mayor al primero
        dividendo = num_2
        divisor = num_1
    residuo = dividendo % divisor	# asignacion del residuo para los valores
    while residuo != 0:			# condicion de bucle mientras el residuo no sea 0
        dividendo = divisor		# reemplazo de dividendo con divisor
        divisor = residuo		# reemplazo de divisor con residuo
        residuo = dividendo % divisor	# recalcular el residuo para evaluar el bucle una vez mas
    print(divisor)			# se imprime el divisor con el cual se calculara el mcm (n1 * n2)//(mcd)
    return(num_1 * num_2)//(divisor)	# se retorna el valor del mcm calculado

if __name__ == "__main__":				
    try:						# limite para ingreso de valores
        a = int(input("Ingrese el primer número: "))	# ingreso del primer numero
        b = int(input("Ingrese el segundo número: "))	# ingreso del segundo numero
        mcm_ = mcm(a, b)				# se añade a una variable la aplicacion de la funcion sobre los numeros ingresados
        print(f"el MCM entre {a} y {b} es {mcm_}")	# se imprime el mcm de ambos numeros ingresados
    except ValueError:					# en caso de ingreso de datos diferente al de numeros enteros
        print("el caracter ingresado no es un numero entero...")
```
#### Recursiva
```python
def mcd(num_1:int,num_2:int) -> int:		# se define la funcion "mcd" recursiva
    if num_1 >= num_2 : 			# condicion para establecer al dividendo y divisor en donde el primer numero es mayor al segundo y aplicar la funcion recursiva
        dividendo = num_1 
        divisor = num_2
    else: 					# condicion para establecer al dividendo y divisor en donde el segundo numero es mayor al primero y aplicar la funcion recursiva
        dividendo = num_2
        divisor = num_1

    if divisor == 0:				# caso base en donde el divisor es 0
        return num_1
    return  mcd(divisor, dividendo % divisor)	# retorno de funcion recusriva tomando al divisor anterior y el residuo obtenido, para asi llegar al caso base

def mcm(num_1, num_2) -> int:				# se define la funcion "mcm"
    return (num_1 * num_2) // (mcd(num_1, num_2))	# se retorna la operacion (n1 * n2) // (mcd)

if __name__ == "__main__":
    try:						# limite para ingreso de valores
        a = int(input("Ingrese el primer número: "))	# ingreso del primer numero
        b = int(input("Ingrese el segundo número: "))	# ingreso del segundo numero
        mcm_ = mcm(a, b)				# se asigna a una variable la aplicacion del funcion sobre los dos numeros ingresados
        print(f"el MCM entre {a} y {b} es {mcm_}")	# se imprime el mcm de ambos numeros ingresados
    except ValueError:					# en caso de ingreso de datos diferente al de numeros enteros
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
def vowel_here(lista : list):
    """
	Esta función de Python verifica cuantas vocales hay en cada elemento dentro de un arreglo.
  
  Args:
    La función vowel_here toma un arreglo como entrada y cuenta el
  	número de vocales en las palabras (cadenas de caracteres). Las vocales se definen en la variable "vowels"
  
  Returns:
    La función vowel_here devuelve una cadena que indica las palabras que contienen 2 o más vocales
  	encontradas en la lista de entrada. La cadena devuelta indicará las palabras que tienen 2 o más vocales
    	dentro de una lista.
	"""
    
    vowels = "aeiou" # vocales definidas
    palabras = [] # lista para palabras que cumplen la condición 
    for element in lista:
        word = str(element).lower() # se evalua todo como string y en minuscula
        contador: int = 0
        for letter in word:
          if letter in vowels:
            contador+= 1
        if contador>= 2:
            palabras.append(element)

    if len(palabras) > 0:
      return (f"en la lista {lista} \nlas palabras en la lista con 2 o mas vocales son: {palabras}\n") # String si encuentra la palabra que cumple
    else:
        return (f"en la lista {lista}\nno hay palabras con dos o mas vocales en la lista\n")   # string si ninguna palabra cumple
        
if __name__ == "__main__":
    try:       
        # Se declaran e inicializan dos listas con elementos heterogeneos como ejemplo
        A : list = ["hola", 15, "hell0", "CHAos"]
        C : list = [18, "14", "hells", "CH4os"]
        
        vocales = vowel_here(A)
        print(vocales) # encuentra palabras con dos o mas vocales

        vocales_2 = vowel_here(C)
        print(vocales_2) # no encuentra ninguna palabra con tales propiedades
        
    except ValueError:
        print("algun caracter ingresado no es valido...")

```
### 8. Desarrollar un programa que dadas dos listas determine que elementos tiene la primer lista que no tenga la segunda lista.
```python
def no_repetidos(lista_1:list, lista_2:list):
"""
	Esta función identifica los elementos repetidos entre listas
  
  Args:
    Como entradas la función recibe las 2 listas que van a ser operadas 
  
  Returns:
    la función retorna un texto con formato que incluye las 2 listas y los elementos no repetidos
	"""
    c = lista_1.copy() #Crea una copia de la lista para conservar solo los elementos que no estene en la otra lista
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
def promedio(lista:list) -> float:				# se define la funcion "promedio"
  suma : float = 0						# se establece una variable de tipo flotante (decimal) donde se acumularan la suma de los datos del vector
  for n in lista:						# se recorre los datos de la lista
    suma += n							# se suman los datos a la variable
  prom = suma / len(lista)					# se calcula el promedio como la sumatoria de los datos dividido el numero de datos 
  return (f"El promedio de su lista {lista} es de: {prom}")	# se retorna el promedio de la lista

def mediana(lista:list) -> float:				# se define la funcion "mediana"
  lista.sort()							# se ordena la lista de menor a mayor
  if (len(lista) % 2) == 0:					# condicion donde los datos de la lista son pares
    num = lista[len(lista)//2] + lista[(len(lista)//2) + 1]	# se realiza la suma de los datos de la mitad de la lista 
    med = num / 2						# se promedia la suma de los datos (entre 2)
    return (f"la mediana de su lista {lista} datos es: {med}")	# se retorna la mediana 
  else:								# caso donde la cantidad de datos es impar
    med = lista[(len(lista)//2)+1]				# se asigna la mediana igual al valor del dato en la mitad de la lista, misma cantidad de datos a izquierda y derecha
    return (f"la mediana de su lista {lista} datos es: {med}")	# se retorna la mediana

def prom_multi(lista : list) -> float:						# se define la funcion "prom_multi"
	multi : float = 1							# se declara una variable para poder multiplicar los valores de los datos de la lista
	for n in lista:								# se recorre la lista
		multi *= n							# se multiplica el valor del dato a la variable mult
	prom = multi ** (1/len(lista))						# se calcula el promedio como la raiz del numero de datos sobre la multiplicacion de los datos
	return (f"el promedio multiplicativo de la lista {lista} es: {prom}")	# se imprime el promedio

def asce(lista:list) -> list:						# se define la funcion "asce"
	lista.sort()							# se aplica el arreglo de orden de menor a mayor
	return (f"la lista ordenada de forma ascendente es: {lista}")	# se imprime la lista arreglada

def desc(lista:list) -> list:						# se define la funcion "desc"
  lista.sort(reverse=True)						# se aplica el arreglo de orden de mayor a menor
  return (f"la lista ordenada de forma descendente es: {lista}")	# se imprime la lista arreglada

def potencia_extremos(lista:list) -> str:	# se define la funcion "potencia_extremos" 
  lista.sort()					# se organiza la lista de menor a mayor 
  base = lista[-1]				# se toma como base el ultimo dato de la lista
  exponente = lista[0]				# se toma como exponente el primer dato de lista
  pot = base ** exponente			# se asigna a una variable el resultado del ultimo dato elevado al primer dato 
  return (f"{base} ^ {exponente} = {pot}")	# se retorna el resultado como un string que presenta la operacion base ^ exponente = potencia

def raiz_menor(lista:list)-> str:									# se define la funcion "raiz_menor"
	lista.sort()											# se organiza la lista de menor a mayor
	raiz = lista[0] ** (1/3)									# se asigna a una variable la operacion de la raiz cubica del dato mas pequeño
	return (f"la raíz cubica del menor elementro dentro de la lista ({lista[0]}) es: {raiz}")	# se retorna un string que presenta la operacion

if __name__ == "__main__":
    try:						# limite para ingreso de valores
        lista = []					# se define una lista vacia para ingresar los datos
        for i in range(1, 6):				# se repite la operacion 5 veces (de 1 a 6 excluyendo el 5)
            x = int(input(f"Ingrese el dato {i}:  "))	# se ingresa un dato para la lista
            lista.append(x)				# se añade ese dato a la lista
            
        print (promedio(lista))				# se aplica la funcion promedio a la lista generada
        print (mediana(lista))				# se aplica la funcion mediana a la lista generada
        print (prom_multi(lista))			# se aplica la funcion promedio multiplicativo a la lista generada
        print (asce(lista))				# se aplica la funcion orden ascendente a la lista generada
        print (desc(lista))				# se aplica la funcion orden descendente a la lista generada
        print (potencia_extremos(lista))		# se aplica la funcion potencia del ultimo dato elevado al primer dato a la lista generada
        print (raiz_menor(lista))			# se aplica la funcion raiz cubica del numero menor a la lista generada
    except ValueError:					# en caso de ingreso de datos diferente al de numeros enteros
        print("no has ingresado un numero entero...")
```

### 10. Suponga que se tiene una lista A con ciertos números enteros. Desarrolle una función que, independientemente de los números que se encuentran en la lista A, tome aquellos números que son múltiplos de 3 y los guarde en una lista nueva, la cual debe ser retornada por la función. Implemente la perspectiva de un patrón de acumulación y también de comprensión de listas.
#### List comprehension utilizando el operador `%` 
```python
def multiplo_3(lista:list) -> list:
    """
  La función multiplo_3 calcula que un numero  de un arreglo sea multiplo de 3 para guardarlo en otra lista.
  
  Args:
	Se ingresa el arreglo de numeros enteros, allí se verifica que el numero sea positivo (o se convierte) y luego se verifica
    que sea un multiplo de 3 para poder almacenarlo en la lista nueva.
  
  Returns:
	La función retorna la nueva lista que solo contiene los multiplos de 3 que estan en el arreglo ingresado inicialmente o un mensaje en 
    caso de no haber.
    """
    new_list = [-x if x < 0 else x for x in lista if x%3==0] # creacion de la lista con list comprehension
    return new_list if len(new_list) >= 1 else "No hay multiplos de 3 en el arreglo"

if __name__ == "__main__":
	# Se declaran dos arreglos iniciales para comprobar el funcionamiento de la función
    A = [1, 2, 4, 8]
    B = [0, 3, 6, 9, 12, -15, 8,-999999, 10842630]

    ej_A = multiplo_3(A)
    print(ej_A) # mensaje donde dice que no se encontraron multiplos de 3
    ej_B = multiplo_3(B)
    print(ej_B) # nueva lista con los multiplos de 3: [0, 3, 6, 9, 12, 15, 999999, 10842630]
```
#### Reto...
<details>
  <summary>Prueba de que no deben retarnos</summary>

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

  def multiplo(lista:list) -> list:
      """
    La función multiplo_3 calcula que un numero  de un arreglo sea multiplo de 3 utilizando la propiedad de los multiplos de 3, donde la suma de sus digitos
    también debe ser múltiplo de 3; por ellos se suman los digitos del numero inicial (para reducir el tamaño) para luego restarle 3 hasta que sea igual o menor que 3;
    asi en caso de ser multiplo llegará a 0 y se guardará.

    Args:
        Se ingresa el arreglo de numeros enteros, allí se verifica que el numero sea positivo (o se convierte) y luego se verifica
        que sea un multiplo de 3  mediante el proceso ya explicadp para poder almacenarlo en la lista nueva.

    Returns:
        La función retorna la nueva lista que solo contiene los multiplos de 3 que estan en el arreglo ingresado inicialmente o un mensaje en 
        caso de no haber.
      """
      new_list = []
      for element in lista:
          digitos : list = separar_digitos(element)
          suma : int= 0
          for number in digitos:
              suma += number
          while suma >= 3: 
              suma -= 3
              if suma == 0: 
                  new_list.append(element)

      return new_list if len(new_list) >=1 else "No hay multiplos de 3 en el arreglo"

  if __name__ == "__main__":
      A = [1, 2, 4, 8] 
      B = [0, 3, 6, 9, -12, 15, 8, 999999] 

      ej_A = multiplo(A)
      print(ej_A) 

      ej_B = multiplo(B)
      print(ej_B) 
```
</details>

#### 11. Desarrollar un algoritmo que determine si una matriz es mágica. Se dice que una matriz cuadrada es mágica si la suma de cada una de sus filas, de cada una de sus columnas y de cada diagonal es igual.
  
```python
def imprimir_matriz(mat):
  """
  La función imprime cada fila de una matriz (arreglo de arreglos de la misma dimensión).
  
  Args:
	Se ingresa el arreglo de forma lineal, luego imprime cada arreglo (fila) para hacer mas visual
    el arreglo.
  
  Returns:
	La función no retorna nada en específico.
  """
  for i in mat:
      print (i)
      
    
def matriz_magica(matriz_1) -> str:
    """
  	La función evalúa la suma de cada fila, columna y diagonal de una matriz cuadrada dada para establecer
    si es o no una matriz mágica.
  
  	Args: 
      Al inicio se declaran variables inicializadas en 0, donde se guardará la suma de los valores en cada dimensión y también un valor booleano (magic) que será el encargado de devolver
      la información en caso de que sea o no magica la matriz. Mediante bucles se acumulan las sumas siguiendo el patrón de acceso para cada dimensión mediante sus indices; el total de la suma
      en cada dimensión se guarda en una lista específica para tener el registro de los valores obtenidos.

  	Returns:
	  La función retorna un string con la información de la suma de cada dimensión, indicando si es o no mágica.
 	"""
    x = len(matriz_1) - 1 # variable auxiliar para acceder a la diagonal que tiene pendiente positiva (/)
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
        sumad2 += (matriz_1[i][i+x]) # acceder a los valores gracias a la variable auxiliar
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
        return (f"Es una matriz magica con suma en \nfilas: {fila} \ncolumnas: {columna} \ndiagonales: {diagonales}\n") # String de matriz mágica
    else:
        return (f"No es una matriz magica con suma en \nfilas: {fila} \ncolumnas: {columna} \ndiagonales: {diagonales}\n") # String matriz no magica

if __name__ == "__main__":
    # Se declaran en inicializan matrices cuadradas de ejemplo
	matriz_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	matriz_2 = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
    
	imprimir_matriz(matriz_1)
	print(matriz_magica(matriz_1)) # return string de no matriz mágica
	print("-------------------------------- \n")
	imprimir_matriz(matriz_2)
	print(matriz_magica(matriz_2)) # return String de matriz mágica
```



