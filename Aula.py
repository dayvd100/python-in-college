#Escreve
arquivo = open("arquivo.txt", "x")
arquivo.write("asdhasjdkf")
arquivo.close()

#Lê
arquivo = open("arquivo.txt", "r")
print(arquivo.read())