def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []

    for i in range(tamanho):
        if orientacao == "vertical":
            posicoes.append([linha + i, coluna])
        else:
            posicoes.append([linha, coluna + i])

    return posicoes



def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)

    if nome_navio not in frota:
        
        frota[nome_navio] = []

    frota[nome_navio].append(posicoes)

    return frota



def faz_jogada(tabuleiro, linha, coluna):
    
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'

    return tabuleiro



def posiciona_frota(frota):
    
    tabuleiro = []

    for i in range(10):
        linha_vazia = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        tabuleiro.append(linha_vazia)

    for nome_navio in frota:
        for navio in frota[nome_navio]:
            for posicao in navio:
                linha = posicao[0]
                coluna = posicao[1]
                tabuleiro[linha][coluna] = 1

    return tabuleiro



def afundados(frota, tabuleiro):
    
    quantidade = 0

    for nome_navio in frota:
        
        for navio in frota[nome_navio]:
            afundado = True
            
            for posicao in navio:
                linha = posicao[0]
                coluna = posicao[1]
                
                if tabuleiro[linha][coluna] != 'X':
                    afundado = False
            
            if afundado:
                quantidade += 1

    return quantidade



def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)

    for posicao in posicoes:
        
        if posicao[0] < 0 or posicao[0] > 9 or posicao[1] < 0 or posicao[1] > 9:
            return False
        
        for nome_navio in frota:
            
            for navio in frota[nome_navio]:
                
                if posicao in navio:
                    return False

    return True



navios = [
    ['porta-aviões', 4, 1],
    ['navio-tanque', 3, 2],
    ['contratorpedeiro', 2, 3],
    ['submarino', 1, 4]
]

frota = {}

for navio in navios:
    
    nome = navio[0]
    tamanho = navio[1]
    quantidade = navio[2]

    for i in range(quantidade):
        
        valida = False

        while not valida:
            
            print('Insira as informações referentes ao navio ' + nome + ' que possui tamanho ' + str(tamanho))
            linha = int(input('Linha: '))
            coluna = int(input('Coluna: '))

            if nome == 'submarino':
                orientacao = 'horizontal'
            else:
                opcao = int(input('[1] Vertical [2] Horizontal >'))
                
                if opcao == 1:
                    orientacao = 'vertical'
                else:
                    orientacao = 'horizontal'

            if posicao_valida(frota, linha, coluna, orientacao, tamanho):
                frota = preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
                valida = True
            else:
                print('Esta posição não está válida!')

print(frota)