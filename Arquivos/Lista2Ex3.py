def main():
    valid = []
    invalid = []
    aux = []
    with open('EndIP.txt', 'rt') as file:
        arq = file.readline()

        while arq != "":
            arqsem = arq.replace('.', ' ') # Retira o "." do arquivo
            aux.append(arqsem.strip()) # Elimina o \n da lista
            arq = file.readline()
        
        file.close()
        print(aux)






        

if __name__ == '__main__':
    main()