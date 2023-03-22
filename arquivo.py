# r = somente leitura
# w = escrita (Caso o arquivo ja exista, ele será apagado e um novo arquivo vazio será criado)
# a = leitura e escrita (Adiciona o novo conteúdo ao fim do arquivo)
# r+ = leitura e escrita
# w+ = escrita (O modo w+, assim como o w, também apaga o conteúdo anterior do arquivo)
# a+ = leitura e escrita (Abre o arquivo para atualização)

# read() = Lê um arquivo inteiro
# readline() = Lê uma linha 
# readlines() = Lê arquivo e o armazena em uma lista 

#abre um arquivo de texto
w = open("arq2.txt", "w")

#texto que vem dentro do arquivo
w.write("Esse é o arquivo")

