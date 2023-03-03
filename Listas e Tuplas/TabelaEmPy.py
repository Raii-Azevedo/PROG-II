# COMO TRANSFORMAR UM TABELA EM PYTHON
def main():
    tabela = [
        ['Janeiro', 56, 'a', 3, 'Pronto', 4, 2],
        ['Fevereiro', 7, 'f', 4, 'Pronto', 5, 5],
        ['Março', 400, 'g', 2, 'Pronto', 6, 7],
        ['Abril', 6, 'p', 3, 'Pronto', 8, 3]
    ]

    for linha in tabela:
        print("%-12s%8d%4s%5d%18s%5d%5d" % (linha[0], linha[1], linha[2], linha[4], linha[5], linha[6]))


if __name__ == '__main__':
    main()
