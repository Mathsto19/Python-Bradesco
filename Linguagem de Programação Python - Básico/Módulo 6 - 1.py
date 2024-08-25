arquivo = open('arquivo.txt', 'w')

arquivo.write('Curso Python \n')
arquivo.write('Aula prática')
arquivo.close()

#leitura do arquivo texto
leitura = open('arquivo.txt', 'r')
print(leitura.read())
leitura.close()