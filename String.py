a = "Thiago"
b = "Luisa"

concatenar = a + " e " + b
print (concatenar)

# contagem de caracteres (conta os espaços)
tamanho = len(concatenar)
print (tamanho)

# ------------------------------------------- # teste 2

a = "Thiago"
b = "Luisa"

concatenar = a + " e " + b

# imprime somente as letras selecionadas por numeros 
print (a[0])
print (a[1])
print (a[2])

#---------------------------------------------# teste 3 

a = "Thiago"
b = "Luisa"

concatenar = a + " e " + b

# imprime o texto de 0 a 6 
print(concatenar[0:6])

#----------------------------------------------# teste 4

minha_string = "O rato roeu a roupa do rei de Roma"

#função split retira a palavra marcada
minha_lista = minha_string.split("a")
print(minha_lista)

#----------------------------------------------# teste 5

minha_string = "O rato roeu a roupa do rei de Roma"

#função find mostra onde a palavra marcada esta em numeros 
busca = minha_string.find("roupa")
print(busca)

#----------------------------------------------# teste 6

minha_string = "O rato roeu a roupa do rei de Roma"

#função find mostra onde a palavra marcada esta em numeros 
minha_string = minha_string.replace("o rei", "a rainha")
print(minha_string)