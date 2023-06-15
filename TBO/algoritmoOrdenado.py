def lst_2_dict(lista):
    

def txt_2_lst():
    lst = []
    with open ('bdveiculos.txt', 'rt') as file:
        linha = file.readline().strip()

        while linha != '':
            lst.append(linha)
            linha = file.readline().strip()

    return lst

def main():
    lst = txt_2_lst()

    D = lst_2_dict(lst)

    print (lst)

if __name__ == '__main__':
    main()