meu_dicionario = {"A" : "AMEIXA", "B" : "BOLA", "C" : "CACHORRO"}

#imprime o dicionario de palavras
print(meu_dicionario)

#-------------------------------------------------------------------------

meu_dicionario = {"A" : "AMEIXA", "B" : "BOLA", "C" : "CACHORRO"}

#imprime imprime a chave C
print(meu_dicionario["C"])

#-------------------------------------------------------------------------

meu_dicionario = {"A" : "AMEIXA", "B" : "BOLA", "C" : "CACHORRO"}

#imprime o valor que estao dentro das chaves
for chave in meu_dicionario:
	print(meu_dicionario[chave])

#-------------------------------------------------------------------------

meu_dicionario = {"A" : "AMEIXA", "B" : "BOLA", "C" : "CACHORRO"}

#imprime o valor das chaves e das palavras
for chave in meu_dicionario:
	print(chave + ":"meu_dicionario[chave])