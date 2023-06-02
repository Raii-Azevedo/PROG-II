import tadretangulo as tret

def main():
  divs_l = 3
  divs_c = 4
  larg_rua = 2
  
  print("EXERCÍCIO TERRENOS E LOTES V. 1.0")
  print("=================================\n")
  larg_t = float(input("Entre com a largura do terreno: "))
  comp_t = float(input("Entre com o comprimento do terreno do terreno: "))

  # CALCULANDO LARG E COMP DE CADA LOTE
  larg_l = (larg_t - (divs_l + 1) * larg_rua)/divs_l
  comp_l = (comp_t - (divs_c + 1) * larg_rua)/divs_c

  t1 = tret.cria_lh(2,2,larg_l,comp_l)
  t2 = tret.cria_lh(?, ?,larg_l,comp_l)
  t3 = tret.cria_lh(?, ?,larg_l,comp_l)
  t4 = tret.cria_lh(?, ?,larg_l,comp_l)
  t5 = tret.cria_lh(?, ?,larg_l,comp_l)

  



# fim main

main()