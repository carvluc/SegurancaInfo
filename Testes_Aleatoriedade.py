from random import randint

TAM = 20000
SPLIT = 4
POSSIBILIDADES = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']
VALIDACAO_RUN = [[2267, 2733], [1079, 1421], [502, 748], [223, 402], [90, 223], [90, 223]]

def geraVetor():
    x = []
    for i in range(0, TAM):
        x.append(str(randint(0, 1)))
    return x

def monoBitTest(list):
    result = [x for x in list if x == '1']
    if(9654 < len(result) < 10346):
        print('Passou no teste MONOBIT (' + str(len(result)) + ')')
    else:
        print('Não passou no teste MONOBIT (' + str(len(result)) + ')')

def pokerTest(list):
    somatorio = 0
    base = ["".join(list[i:i + SPLIT]) for i in range(0, len(list), SPLIT)]
    ocorrencias = dict.fromkeys(POSSIBILIDADES, 0)
    for item in base:
        ocorrencias[item] = ocorrencias[item] + 1
    
    for item in ocorrencias:
        somatorio = somatorio + ocorrencias[item] ** 2
    
    x = (16/5000.0) * somatorio - 5000

    if(1.03 < x < 57.4):
        print('Passou no teste POKER (' + str(x) + ')')
    else:
        print('Não passou no teste POKER (' + str(x) + ')')

def runTest(list):
    x = []
    qt = 0
    for i in range(8):
        x.append(0)

    for item in list:
        if (item == '0'):
            qt += 1
        else:
            if(qt > 7):
                qt = 7
            x[qt] += 1
            qt = 0

    qt = 0

    for item in list:
        if (item == '1'):
            qt += 1
        else:
            if (qt > 7):
                qt = 7
            x[qt] += 1
            qt = 0
    
    qt = 0
    
    for item in x[2:]:
        if(VALIDACAO_RUN[qt][0] <= item <= VALIDACAO_RUN[qt][1]):
            qt += 1
            continue
        else: 
            print('Não passou no teste RUN')
            return
        
    print('Passou no teste RUN ' + str(x[2:]))


def longRunTest(list):
    x = []
    qt = 0

    for i in range(33):
        x.append(0)

    for item in list:
        if (item == '0'):
            qt += 1
        else:
            if(qt > 33):
                print('Não passou no teste LONG')
                return
            x[qt] += 1
            qt = 0

    qt = 0

    for item in list:
        if (item == '1'):
            qt += 1
        else:
            if (qt > 33):
                print('Não passou no teste LONG')
                return
            x[qt] += 1
            qt = 0

    print('Passou no teste LONG, nenhuma cadeia de repetições > 33 foi encontrada')

x = geraVetor()
monoBitTest(x)
pokerTest(x)
runTest(x)
longRunTest(x)

