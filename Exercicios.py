#Faça um programa que receba a idade do usuário e diga se ele é maior ou menor de idade.  

idade = int(input("Digite sua idade: "))

if idade >= 18:
	print("Você é maior de idade")

elif idade < 18:
	print("Você é menor de idade")

#-------------------------------------------------------------------------------------

#Faça um programa que receba duas notas digitadas pelo usuário. Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado. 

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 6
	print("Você foi aprovado")
else
	print("Você foi reprovado")

#---------------------------------------------------------------------------------------

#Escreva um programa que ordene uma lista numérica com três elementos. 

lista = [2,3,1]

print(sorted(lista))

#----------------------------------------------------------------------------------------

#Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal.   

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
sinal = int(input("Digite o sinal: "))

if sinal == "+":
	op = n1 + n2
elif sinal == "-":
	op = n1 - n2
elif sinal == "*":
	op = n1 * n2
elif sinal == "/"
	op = n1 / n2
else 
	print("Sinal invalido")

print(op) 