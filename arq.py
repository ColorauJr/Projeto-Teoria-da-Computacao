with open('Arquivo Automato.txt', 'r') as arquivo:
    
    totalLinhas = arquivo.readlines()
    
    def comprimentoLinha(x):
        return len(totalLinhas[x]) - 1#subtrai-se 1 para não contar com o \n

    def lerLinha(x):
        return totalLinhas[x]
    
    def lerAlfabeto():
        n = 0
        c = 0
        for i in range(9, comprimentoLinha(0)):
        
            alfabeto.append(linha[9+n])
            if alfabeto[c] == linha[comprimentoLinha(0)-1]:
                break
            n = n + 2
            c = c + 1

    def lerEstados():
        n = 0
        c = 0
        for i in range(8, comprimentoLinha(1)-1):
            estados.append(linha[8+n]+linha[8+n+1])
            if estados[c] == linha[(comprimentoLinha(1)-2)] + linha[+(comprimentoLinha(1)-1)]:
                break
            n = n + 3
            c = c + 1
            
    def lerFinais():
        n = 0
        c = 0
        for i in range(7, comprimentoLinha(3)-1):
            finais.append(linha[7+n]+linha[7+n+1])
            if finais[c] == linha[(comprimentoLinha(3)-2)] + linha[+(comprimentoLinha(3)-1)]:
                break
            n = n + 3
            c = c + 1


    alfabeto = []
    linha = lerLinha(0)
    lerAlfabeto()

    estados = []
    linha = lerLinha(1)
    lerEstados()

    inicial = linha[(comprimentoLinha(2)-2)] + linha[+(comprimentoLinha(2)-1)]

    finais = []
    linha = lerLinha(3)
    lerFinais()


    #teste
    print("---------------------------------------")
    for i in range(0, len(alfabeto)):
        print(alfabeto[i])
    print("--------")
    for i in range(0, len(estados)):
        print(estados[i])
    print("--------")
    print(inicial)
    print("--------")
    for i in range(0, len(finais)):
        print(finais[i])
    print("--------")
    print("acabou essa mizera")
    #teste