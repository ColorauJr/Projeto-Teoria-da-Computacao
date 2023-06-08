
from DFA import DFA
# from DFA import minimize

with open('Arquivo Automato.txt', 'r') as arquivo:
    totalLinhas = arquivo.readlines()
    
def comprimentoLinha(x):
    return len(totalLinhas[x]) - 1 #subtrai-se 1 para desconsiderar o \n

def lerLinha(x):
    return totalLinhas[x]

#A EXPLICACAO DESTA FUNÇÃO TAMBÉM É VÁLIDA PARA lerEstados() E lerFinais() 
def lerAlfabeto():
    n = 0 #variável usada para fazer a leitura correta dos caracteres necessários
    c = 0 #variável usada para comparar a última string lida ao último elemento da linha do arquivo selecionada, para finalizar o loop
    
    for i in range(9, comprimentoLinha(0)): #o valor inicial de "i" é este pois é a posição onde se inicia os dígitos necessários a serem lidos na linha do arquivo
    
        alfabeto.append(linha[9+n])
        if alfabeto[c] == linha[comprimentoLinha(0)-1]: #verifica se chegou ao final da linha
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

def lerInicial():
    return linha[(comprimentoLinha(2)-2)] + linha[+(comprimentoLinha(2)-1)]
        
def lerFinais():
    n = 0
    c = 0
    for i in range(7, comprimentoLinha(3)-1):
        finais.append(linha[7+n]+linha[7+n+1])
        if finais[c] == linha[(comprimentoLinha(3)-2)] + linha[(comprimentoLinha(3)-1)]:
            break
        n = n + 3
        c = c + 1

#a função lerá da quinta linha em diante, pois são as linhas relativas às transições
def lerTransicoes():
    for i in range(5, len(totalLinhas)):
        transicoes.append(totalLinhas[i])


#esta função verifica se o número de estado inicial é diferente de 1, e se todos os estados finais descritos estão na lista de estados
def verificarInicialFinal():
    countInicial = 0
    countFinal = 0

    for i in range(0, len(finais)):#loop responsável pela definição do estado final a ser verificado
        for j in range(0, len(estados)):#loop responsável por percorrer a lista de estados para verificar se os estados finais e inicial são válidos
            if inicial == estados[j] and countInicial == 0:
                countInicial = countInicial + 1        
            if finais[i] == estados[j]:
                countFinal = countFinal + 1

            #ao comparar todos os estados com o estado final atual da lista, se o contador estiver zerado, significa que o estado final não existe na lista, logo é inválido
            if j == len(estados)-1 and countFinal == 0:
                print("Automato invalido: um dos estados finais nao existe na lista de estados.")
                exit()
    if countInicial != 1: #como só um estado inicial é permitido, se o contador der um número diferente de um, significa que não há estado inicial válido
        print("Automato invalido: quantidade de estado inicial incorreta.")
        exit()




#esta função verifica a quantidade de transições, quantidade de transições por estado e quantidade de transições por estado para cada caractere
def verificarTransicoes():
    
    #o número válido de transicoes é alfabeto*estados. Se a quantidade de transicoes for diferente, o autômato é inválido
    if len(transicoes) != (len(alfabeto) * len(estados)):
        print("Automato invalido: quantidade de transicoes do automato incorreta.")
        exit()
    
    for i in range(0, len(estados)):#loop para percorrer todos os estados a fim de analisar as transições do arquivo
        
        verificadorTransicao = [] #recebe os caracteres do alfabeto de cada transição do estado atual a fim de usar os caracteres e o comprimento da lista pra validação
        
        #neste loop, é verificada a quantidade de transicoes que o estado "estados[i]" possui. Quando verificada, se a transição pertence ao estado, a lista
        #verificadorTransicao[] recebe o caractere do alfabeto que corresponde á transição
        for j in range(0, len(transicoes)):
            transicaoAtual = transicoes[j]
            if estados[i] == (transicaoAtual[0]+transicaoAtual[1]):
                verificadorTransicao.append(transicaoAtual[len(transicaoAtual)-2])

        #se os números não batem, quer dizer que a quantidade de transições do estado "estados[i]" é incorreta, invalidando o autômato
        if len(verificadorTransicao) != len(alfabeto):
            print("Automato invalido: quantidade de transicoes para o estado " + estados[i] + " incorreta.")
            exit()
        
        #neste loop, será verificado se a quantidade de transições de estados[i] para cada caractere está correta
        for j in range(0, len(alfabeto)):
            count = 0 #variável para verificação

            #neste loop, são contadas as transições de estados[i] para cada caractere do alfabeto
            for k in range(0, len(verificadorTransicao)):
                if alfabeto[j] == verificadorTransicao[k]:
                    count = count + 1

            #se o número de transições de estrados[i] para cada caractere for diferente de 1, o autômato é invalidado
            if count != 1:
                print("Automato invalido: " + estados[i] + " possui um numero incorreto de transicoes pra um caractere do alfabeto.")
                exit()

    #Se o autômato passar por todas as verificações, ele é dado como válido
    print("Automato valido.")

    #Tem que fazer a passagem aqui para o DFA depois de verificar tudo tou me comunicando com você
    #passar para o DFA


def printarInfo(): #função para printar as informações do DFA
    print("Minimized DFA:")
    print("States:", dfa.states) 
    print("Alphabet:",dfa.alphabet) 
    print("Transitions:", dfa.transitions)
    print("Initial State:", dfa.initial_state)
    print("Accepting States:", dfa.accepting_states)




alfabeto = [] #lista que armazena o alfabeto
linha = lerLinha(0) #função que lê a primeira linha do arquivo e a armazena na lista linha[]
lerAlfabeto() #função que lê o alfabeto e o armazena na lista alfabeto[]

estados = [] #lista que armazena os estados
linha = lerLinha(1) #função que lê a segunda linha do arquivo e a armazena na lista linha[]
lerEstados() #função que lê os estados e os armazena na lista estados[]

inicial = lerInicial() #função que lê o estado inicial e o armazena na variável inicial

finais = [] #lista que armazena os estados finais
linha = lerLinha(3) #função que lê a quarta linha do arquivo e a armazena na lista linha[]
lerFinais() #função que lê os estados finais e os armazena na lista finais[]
verificarInicialFinal() #função que verifica se o estado inicial e os estados finais são válidos

transicoes = [] #lista que armazena as transições
lerTransicoes() 
verificarTransicoes() #função que verifica se as transições são válidas

dfa = DFA(alfabeto, estados, inicial, finais, transicoes) #criar o DFA estanciado
dfa = DFA.minimize() #minimizar o DFA show
printarInfo() #printar as informações do DFA