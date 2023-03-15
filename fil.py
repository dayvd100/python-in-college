def leitura1():
    print('\nabrindo arquivo desordenado')
    print('-----')
    arquivo = open("arquivo.txt", "r")
    linha = "."
    while linha != "":
        linha = arquivo.readline()
        print(linha)
    print('\nfim do arquivo')
    arquivo.close()


def leitura2():
    arquivo = open('arquivo.txt', 'r')
    linhas = arquivo.readlines()
    for linha in linhas:
        print(linha)
    print('n\t\t Fim do arquivo')
    arquivo.close()

def mudandoNome(text):
    with open("arquivo.txt", "w") as meuArquivo:
        meuArquivo.write(text)

    with open("arquivo.txt", "r") as meuArquivo:
        print(meuArquivo.readline())    
      
def juntandoTexto():
    with open("arquivo.txt", "w") as arquivo:
        linhas = ["Titulo\n", "Descrição\n", "footer\n"]
        arquivo.writelines(linhas)

