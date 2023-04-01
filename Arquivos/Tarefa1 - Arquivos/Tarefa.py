def loadmat(nomearq, arquivo):
    # Leitura do Arquivo
    ma = []
    mb = []

    arq = open(f'{nomearq}.txt', "rt")
    linha = arq.readline()

    while linha != '':
        if nomearq == arquivo[0]:
            ma.append(linha)
            linha = arq.readline()
        else:
            mb.append(linha)
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

    print(ma)
    print(mb)


if __name__ == '__main__':
    main()
