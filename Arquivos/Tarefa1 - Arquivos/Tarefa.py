def matriz(soma):
    saida = input('\nDigite o nome de arquivo de saída: ')
    with open(f'{saida}.txt', 'wt') as file:
        s = ""
        for i in range(len(soma)):
            for j in range(len(soma[0])):
                s = s + ("%5d" % soma[i][j])
            s = s + "\n"
        file.write(s)

    file.close()
    print('\nPROCESSAMENTO CONCLUÍDO')
    

def somaMat(ma,mb):
    linhas = len(ma)
    colunas = len(ma[0])  

    soma = [[0] * colunas for linha in range(linhas)]

    for i in range(linhas):
        for j in range(colunas):
            soma[i][j] = ma[i][j] + mb[i][j]

    return soma


def loadmat(nomearq, arquivo):
    # Leitura do Arquivo
    ma = []
    mb = []

    arq = open(f'{nomearq}.txt', "rt")
    linha = arq.readline()

    while linha != '':
        valores = linha.strip().split()
        if nomearq == arquivo[0]:
            ma.append([int(valor) for valor in valores])
            linha = arq.readline()
        else:
            mb.append([int(valor) for valor in valores])
            linha = arq.readline()

    arq.close()

    return ma, mb


def main():
    ma = []
    mb = []

    print('PROCESSAMENTO DE MATRIZ')
    arquivo = []
    quant = int(input('\nQuantas matrizes irá somar? '))

    # Loop para leitura de matrizes
    for i in range(quant):
        nomearq = input('\nDigite o nome do arquivo para leitura: ')
        arquivo.append(nomearq)
        ma_arq, mb_arq = loadmat(nomearq, arquivo)
        ma += ma_arq
        mb += mb_arq

    soma = somaMat(ma, mb)

    matriz(soma)

    

if __name__ == '__main__':
    main()
