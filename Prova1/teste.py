def relatorioDomains(nomearq, lst):
    arq = open(nomearq, "wt")
    lst_count = []
    position = 0
    for x in lst:
        lst_count.append((x[0], []))
        for site in x[1]:
            dom = site.split(".")
            lst_count[position][1].append(dom[len(dom) - 2])

        position += 1

    lstContados = []
    cnt = 0
    for x in lst_count:
        arq.write(x[0] + ":")
        arq.write("\n")
        lstContados = []
        for y in x[1]:
            cnt = 0
            if y not in lstContados:
                lstContados.append(y)
                for cod in x[1]:
                    if cod == y:
                        cnt += 1
                arq.write("{}:{}\n".format(y, cnt))

        arq.write("\n\n")

    arq.close()
    return lst


def processa(nomearq):
    lst = []

    lstRepetidos = []
    arq = open(nomearq, "rt")
    linha = arq.readline().strip()

    while linha != "":
        lstLinha = linha.split(".")
        if lstLinha[len(lstLinha) - 1] in lstRepetidos:
            for x in lst:
                if lstLinha[len(lstLinha) - 1] == x[0]:
                    x[1].append(linha)
        else:
            lst.append((lstLinha[len(lstLinha) - 1], [linha]))
            lstRepetidos.append(lstLinha[len(lstLinha) - 1])

        linha = arq.readline().strip()

    arq.close
    return lst


def prova1():
    lista = processa("webdomains.txt")

    relatorioDomains("saidaprova1.txt", lista)


prova1()
