print('''Construa uma programa Python que transforme a base de dados "bdcepruas.txt" em um arquivo JSON,
A estrutura do arquivo JSON de saída seque a ordem dos campos do artigo original. Nomeie o arquivo
de saída como "saidaexec.json" ''')

def txt_2_json():
    with open ('bdcepsruas.txt', 'rt') as file:
        linha = file.readline()
        
        with open ('saidaexec.json', 'w') as arq:
            
            while linha != '':
                arq.write(linha)
                linha = file.readline()
        arq.close()
    file.close()


def main():
    J = txt_2_json()

    print('Processamento concluído')

if __name__ =='__main__':
    main()