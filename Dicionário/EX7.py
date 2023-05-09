print(f'''Construa um programa pyhton que receba como entrada o arquivo JSON "saidaExec.json" e gere como saída
o arquvo "exec7.json". O arquivo deve seguir a seguinte estrutura para cada dado:
''')

def txt_2_json():
    with open ('saidaexec.json', 'rt') as file:
        linha = file.readline()
        
        with open ('', 'w') as arq:
            
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