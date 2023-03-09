# Construa uma função que recebe uma string contendo um texto qualquer e retorne uma lista das palavras encontradas no texto.
# Limpar a sujeira no meio da palavra
# Remover palavras repetidas - Contar essas palavras e indicar!

def faxina(palavra):
    if palavra.isalnum():
        return palavra
    else: # Utilizar fatiamento para eliminar o caractere que está no final
        return palavra[:-1]
    
def faxina2(palavra):
    while not palavra[-1].isalnum():  # Utilizar fatiamento para eliminar o caractere que está no final. O palavra[-1] indica que quero eliminar só a sujeira do final da palavra, não no meio
        palavra = palavra[:-1]
    return palavra
    
def print_palavras(lista):
    for palavra in lista:
        print(palavra)

def separa(txt):
    lst = txt.split() # Assume que o separador é o espaço, 1 caractere espaço.

    for i in range(len(lst)):
        lst[i] = faxina2(lst[i])
    return lst

def main():
    s = '''De forma geral, o Chat GPT é um chatbot voltado para desenvolver diálogos reais com os usuários..... 
    A ferramenta possui mais de 1 milhão de participantes e se tornou muito popular nos últimos tempos 
    devido à modernidade, à simplicidade, à capacidade de desempenhar grande variedade de ações e à 
    automação de tarefas. Uma inteligência artificial possui o objetivo de replicar uma série de 
    comportamentos humanos. Essa ferramenta é destaque entre muitos especialistas em tecnologia. 
    Continue lendo este artigo para compreender sobre as diversas funções do software do ex-secretário.'''
    
    lst_palavras = separa(s)

    print_palavras(lst_palavras)

    print(f' Foram encontradas {len(lst_palavras)} palavras na lista')


if __name__ == "__main__":
    main()
