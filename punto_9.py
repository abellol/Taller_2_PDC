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