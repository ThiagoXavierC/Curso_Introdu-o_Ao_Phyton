minha_lista = ["abacaxi", "melancia", "banana"]
minha_lista_2 = [1,2,3,4,5]
minha_lista_3 = ["abacaxi", 2, 9.98, True]

#imprime os valores da lista escolhida
for item in minha_lista_2:
	print(item)

#---------------------------------------------------

minha_lista = ["abacaxi", "melancia", "banana"]
minha_lista_2 = [1,2,3,4,5]
minha_lista_3 = ["abacaxi", 2, 9.98, True]

#adiciona novo item a lista
minha_lista.append("limão")

print(minha_lista)

#----------------------------------------------------

minha_lista = ["abacaxi", "melancia", "banana"]
minha_lista_2 = [1,2,3,4,5]
minha_lista_3 = ["abacaxi", 2, 9.98, True]

minha_lista.append("limão")

if 3 in minha_lista_2:
	print("O numero 3 esta na lista")

#-----------------------------------------------------

minha_lista = ["abacaxi", "melancia", "banana"]
minha_lista_2 = [1,2,3,4,5]
minha_lista_3 = ["abacaxi", 2, 9.98, True]

minha_lista.append("limão")

#apaga os valores
del minha_lista[2:]
	print(minha_lista) 

#-----------------------------------------------------

lista = [124, 5, 546, 2, 6, 1,8,500,550,600]

#ordena a lista de numeros  de forma crescente
lista.sort()

print(lista)

#-----------------------------------------------------

lista = [124, 5, 546, 2, 6, 1,8,500,550,600]

#imprime a lista de forma decrescente
lista.sort(reverse = True)

print(lista)

#------------------------------------------------------

lista2 = ["bola", "abacate", "limao"]

#imprime as palavras 
lista2.sort(reverse = True)

print(lista2)

