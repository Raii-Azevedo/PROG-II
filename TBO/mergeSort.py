def mergeSort(D):


def lst_2_dict(lst):
    D = []
    # Range de 0 ao Tamanha da lista de 4 em 4 items.
    for i in range(0, len(lst), 4):
        item = lst[i:i+4]

        V = {
            "placa": item[0].strip(),
            "modelo": item[1].strip(),
            "marca": item[2].strip(),
            "Km": item[3].strip(),
        }

        D.append(V)

    return D


def txt_2_lst():
    lst = []
    with open('bdveiculos.txt', 'rt') as file:
        linha = file.readline().strip()

        while linha != '':
            lst.append(linha)
            linha = file.readline().strip()

    return lst


def print_lst(D):
    for i in D:
        print(i["marca"], i["modelo"], i["placa"], i["Km"],)

def main():
    lst = txt_2_lst()

    D = lst_2_dict(lst)
    print_lst(D)

    mergeSort(D)
    print_lst(D)

    
if __name__ == '__main__':
    main()
