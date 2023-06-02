import tadretangulo as tret

def main():

    divs_l = 3
    divs_c = 4
    larg_rua = 2
    
    print('TERRENOS E LOTES')
    larg_t = float(input('Entre com a largura do terreno: '))
    comp_t = float(input('Entre com o comprimento do terreno: '))

    # Calculando Largura e Comprimento de cada lote
    # Em relação a coordenada de origem do terreno
    larg_l = (larg_t - (divs_l +1) * larg_rua)/divs_l
    comp_l = (comp_t - (divs_c + 1) * larg_rua)/divs_c

    t1 = tret.cria_lh(1 * larg_rua + 0 * larg_l, 2, larg_l,  comp_l)
    t2 = tret.cria_lh(2 * larg_rua + 1 * larg_l, 2, larg_l,  comp_l)
    t3 = tret.cria_lh(3 * larg_rua + 2 * larg_l, 2, larg_l,  comp_l)

    t4 = tret.cria_lh(1 * larg_rua + 0 * larg_l, 2 * larg_rua + 1 * comp_t, larg_l,  comp_l)
    t5 = tret.cria_lh(1 * larg_rua + 0 * larg_l, 2 * larg_rua + 1 * comp_t, larg_l,  comp_l)
    t6 = tret.cria_lh(1 * larg_rua + 0 * larg_l, 2 * larg_rua + 1 * comp_t, larg_l,  comp_l)

    # Criar uma fórmula que permita que um Loop substitua esse padrão


if __name__ == '__main__':
    main()
