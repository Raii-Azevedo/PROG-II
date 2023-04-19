def int2romanos(dic, valor):
    if valor in dic:
        return dic[valor]
    
    else:
        aux = ''
        aux += dic[valor]
        return aux 


def main():
    d = {'': '0', '1': 'I', '2': 'II', 'C': '100', 'CC': '200', 'CCC': '300', 'CD': '400', 'CM': '900', 'D': '500', 'DC': '600', 'DCC': '700', 
         'DCCC': '800', 'III': '3', 'IV': '4', 'IX':'9', 'L': '50', 'LX': '60', 'LXX': '70', 'LXXX': '80', 'V': '5', 'VI': '6', 'VII': '7', 'VIII': '8', 
         'X': '10', 'XC': '90', 'XI': '11', 'XII': '12', 'XIII': '13', 'XIV': '14', 'XIX': '19', 'XL': '40', 'XV': '15', 'XVI': '16', 'XVII': '17', 
         'XVIII': '18', 'XX':'20', 'XXX': '30'}

    v = input('Digite um número em Algarismos Romanos para ver em Arábico: ').upper()
    print(int2romanos(d, v))


if __name__ == '__main__':
    main()
