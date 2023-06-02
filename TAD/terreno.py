import tadretangulo as tret

def cria_lst_lotes(lt, ct, divl, divc):
    # Calculando Largura e Comprimento de cada lote
    # Em relação a coordenada de origem do terreno
    larg_l = (larg_t - (divs_l +1) * larg_rua)/divs_l
    comp_l = (comp_t - (divs_c + 1) * larg_rua)/divs_c


    lotes = []
    
    # Criar uma fórmula que permita que um Loop substitua esse padrão
    for i in range (1, divs_c + 1):
        for j in range(divs_l):
            lote = tret.cria_lh(j * larg_rua + (j-1) * larg_l, i * larg_rua + (i-1) * comp_t, larg_l, comp_l)
            lotes.append(lote)

    return lotes

def printListaLotes(lstlotes):
    cont = 1
    for lote in lstlotes:
        xy  = tret.getES(lote) # getES = Coordenada superior
        l = tret.getL(lote)
        c = tret.getA(lote)
        a = tret.area(lote)
        p = tret.perimetro(lote)
        print("%4d%5.2f%5.2f%10.2f%10.2f%10.2f%10.2f" % (cont, xy[0], xy[1], l , c, a, p))
        cont += 1

def main():

    divs_l = 3
    divs_c = 4
    larg_rua = 2
    
    print('TERRENOS E LOTES')
    larg_t = float(input('Entre com a largura do terreno: '))
    comp_t = float(input('Entre com o comprimento do terreno: '))

    # Base do loop em (sobrasTerreno) Exibir esses dados na tela e salvar no arquivo.

    lista_lotes = cria_lst_lotes(larg_t, comp_t, divs_l, divs_c, larg_rua)

if __name__ == '__main__':
    main()
