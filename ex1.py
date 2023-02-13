import math
print("Fazer uma função que pega o valor de um ângulo e converta pra radianos")


def fatorial(n):
    if n in [0,1]:
        return 1

    fat = 1

    for f in range(1,n+1):
        fat = fat * f
    return float(fat)

def seno(A):
    A = math.radians(A)
    senoA = A - (A**3/fatorial(3)) + (A**5/fatorial(5)) - (A**7/fatorial(7))

    return senoA



def main():
    fim = int(input("Defina o Loop: "))
    for angulo in range (fim+1):
        print('%3d%10.2f%10.2f' % (angulo,math.sin(math.radians(angulo)), seno(angulo)))
     

if __name__ == '__main__':
    main()
   


