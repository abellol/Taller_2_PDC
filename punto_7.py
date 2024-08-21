def vowel_here(lista : list):
    vowels = "aeiou" 
    palabras = [] 
    for element in lista:
        word = str(element).lower() 
        contador: int = 0
        for letter in word:
          if letter in vowels:
            contador+= 1
        if contador>= 2:
            palabras.append(element)

    if len(palabras) > 0:
      return (f"en la lista {lista} \nlas palabras en la lista con 2 o mas vocales son: {palabras}\n") 
    else:
        return (f"en la lista {lista}\nno hay palabras con dos o mas vocales en la lista\n")  
        
if __name__ == "__main__":
    try:       
       
        A : list = ["hola", 15, "hell0", "CHAos"]
        C : list = [18, "14", "hells", "CH4os"]
        
        vocales = vowel_here(A)
        print(vocales) 

        vocales_2 = vowel_here(C)
        print(vocales_2) 
        
    except ValueError:
        print("algun caracter ingresado no es valido...")
