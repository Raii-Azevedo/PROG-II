def achacontador(lstf, totalv):
    salario = 200 + totalv * 0.09

    for i in range(len(lstf)):
        t = lstf[i]
        if salario >= t[0] and salario <= t[1]:
            return i

def main():
    lst = [(200, 299), (300, 399), (400, 499), (500, 599), (600, 699), (700, 799), (800, 899), (900, 999), (1000, 8000)]

    contador = [0] * 9

    # SUPOR QUE A EMPRESA POSSUI 10 FUNCIONÁRIOS

    for i in range(10):
        totalvendas = float(input(f'Entre com o total de vendas do {i+1} funcionário: '))
        posicao = achacontador(lst, totalvendas)
        contador[posicao] = contador[posicao] + 1


if __name__ == '__main__':
    main()