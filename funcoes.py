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



def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto