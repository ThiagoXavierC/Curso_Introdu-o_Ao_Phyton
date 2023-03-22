x = [1, 2, 3, 4, 5]
y = [] 


#Sinal ** (elevado), logo faz os numeros serem elevados a 2 
for i in x:
	y.append(i**2)

print(x)
print(y)

#-------------------------------------------------------------------------

#printa novamente os numeros sendo elevados a 2 com list comprehension
x = [1, 2, 3, 4, 5]
y = [i**2 for i in x]

print (x)
print(y) 

#--------------------------------------------------------------------------

#imprime numeros impares
x = [1, 2, 3, 4, 5]
y = [i**2 for i in x]
z = [ i for i in x if i%2 == 1]

print (z)