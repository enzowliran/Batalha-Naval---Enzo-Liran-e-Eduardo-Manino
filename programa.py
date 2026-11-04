import random
from funcoes import define_posicoes, preenche_frota, posicao_valida, posiciona_frota, faz_jogada, afundados, monta_tabuleiros

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
                opcao = int(input('Orientação: [1] Vertical [2] Horizontal '))
                
                if opcao == 1:
                    orientacao = 'vertical'
                else:
                    orientacao = 'horizontal'

            if posicao_valida(frota, linha, coluna, orientacao, tamanho):
                frota = preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
                valida = True
            else:
                print('Esta posição não está válida!')

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota)

jogadas = []
jogadas_oponente = []
jogando = True

while jogando:
    
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    jogada_valida = False

    while not jogada_valida:
        
        linha = int(input('Jogador, qual linha deseja atacar? '))

        while linha < 0 or linha > 9:
            print('Linha inválida!')
            linha = int(input('Jogador, qual linha deseja atacar? '))

        coluna = int(input('Jogador, qual coluna deseja atacar? '))

        while coluna < 0 or coluna > 9:
            print('Coluna inválida!')
            coluna = int(input('Jogador, qual coluna deseja atacar? '))

        if [linha, coluna] in jogadas:
            print('A posição linha ' + str(linha) + ' e coluna ' + str(coluna) + ' já foi informada anteriormente!')
        else:
            jogadas.append([linha, coluna])
            jogada_valida = True

    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)

    if afundados(frota_oponente, tabuleiro_oponente) == 10:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False
    else:

        posicao_nova = False

        while not posicao_nova:

            linha_oponente = random.randint(0, 9)
            coluna_oponente = random.randint(0, 9)

            if [linha_oponente, coluna_oponente] not in jogadas_oponente:
                jogadas_oponente.append([linha_oponente, coluna_oponente])
                posicao_nova = True

        print('Seu oponente está atacando na linha ' + str(linha_oponente) + ' e coluna ' + str(coluna_oponente))
        tabuleiro_jogador = faz_jogada(tabuleiro_jogador, linha_oponente, coluna_oponente)

        if afundados(frota, tabuleiro_jogador) == 10:
            print('Xi! O oponente derrubou toda a sua frota =(')
            jogando = False