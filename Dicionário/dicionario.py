def converte_2_txt(dic, n):

    if n in dic:
        return dic[n]
    
    else:
        aux = n
        n = -1 * n
        dezena = n // 10 * 10
        unidade = n % 10
        
        if aux < 0:
            txtdezena = (f'menos {dic[dezena]} e {dic[unidade]}')
        else:
            txtdezena = (f'{dic[dezena]} e {dic[unidade]}')


        return txtdezena
    

def main():
    d = {0:'zero', 1:'um', 2:'dois', 3:'tres', 4:'quatro', 5:'cinco', 6:'seis', 7: 'sete', 8:'oito',
         9:'nove', 10:'dez', 11:'omze', 12:'doze', 13:'treze', 14:'quatorze', 15:'quinze', 16:'dezesseis', 17:'dezessete',18:'dezoito',
         19:'dezenove', 20:'vinte', 30:'trinta', 40:'quarenta', 50:'cinquenta', 60:'sessenta', 70:'setenta', 80:'oitenta', 90:'noventa', 
         100:'cem', 200:'duzentos', 300:'trezentos', 400:'quatrocentos', 500:'quinhentos', 600:'seicentos', 700:'setecentos', 800:'oitocentos', 
         900:'novecentos'}
    
    num = int(input('Digite um número inteiro positivo: '))
    print(converte_2_txt(d, num))

if __name__ == '__main__':
    main()