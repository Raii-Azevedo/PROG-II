def main():
    lst = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alvo = input('Digite o nome para pesquisar na lista: ').capitalize()[0]

    # Busca Binária
    inicio = 0
    fim = len(lst) - 1
    

    while ???:
        meio = (fim - inicio)//2

        if alvo == lst[meio]:
            print(f'{alvo} = Encontrado')
        else:
            if alvo > lst[meio]:
                inicio = meio + 1 # O novo inicio começa no MEIO + 1 posição
            else:
                fim = meio - 1 # Caso o elemento esteja na 1ª metade da lista somente o fim muda











if __name__ == '__main__':
    main()