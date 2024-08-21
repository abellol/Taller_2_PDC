def imprimir_matriz(mat):

  for i in mat:
      print (i)
      
    
def matriz_magica(matriz_1) -> str:

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