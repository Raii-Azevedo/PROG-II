def converte_dec_txt(d, num):
    parte_int = int(num)
    parte_dec = num - parte_int
    
    parte_int_txt = (converte_2_txt(parte_int))

    if parte_dec == 0:
        return parte_int_txt
    elif parte_dec >= 0.1: