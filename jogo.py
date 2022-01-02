'''
Autor: Amanda Silva Santos
Componente Curricular: MI - Algoritmos I
Concluido em: 13/08/2019
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
'''

from random import *
from time import *
import os

class Carta:
    '''Representa uma carta.'''
    def __init__(self):
        self.personagem = ''
        self.valor = 0
        self.forca = 0.0
        self.energia = 0.0
        self.jokempo = ''

pilha = []
with open('Cartas.txt') as handle:
    for line in handle:
        carta = Carta()
        line = line.strip()
        line = line.split(';')
        try:
            carta.personagem = line[0]
            carta.valor = int(line[1])
            carta.forca = float(line[2])
            carta.energia = float(line[3])
            carta.jokempo = line[4]
        except:
            continue # Caso a linha do arquivo não contenha uma carta, esta não será convertida a objeto.
        pilha.append(carta)
shuffle(pilha)

class Player():
    '''Objeto que representa um jogador'''
    def __init__(self):
        self.nome = str
        self.vitorias = 0
        self.jogos = 0
        self.mao = self.mao_do_jogador(pilha)
        if self.jogos == 0:
            self.sucesso = 0
        else:
            self.sucesso = (self.vitorias / self.jogos) * 100

    def mao_do_jogador(self, pilha):
        '''Método que retorna a mão do jogador.'''
        lista = []
        for i in range(5):
            card = pilha.pop()
            lista.append(card) # A mão do jogador será uma lista de objetos do tipo carta.
        return lista

def Bubble(listadeobj, atributo):
    tam = len (listadeobj)
    if atributo == 'valor':
        for objeto in range(tam):
            for i in range (tam-1, objeto-1, -1):
                if listadeobj[i-1].valor > listadeobj[i].valor:
                    listadeobj[i], listadeobj[i-1] = listadeobj[i-1], listadeobj[i]
    elif atributo == 'forca':
        for objeto in range(tam):
            for i in range (tam-1, objeto-1, -1):
                if listadeobj[i-1].forca > listadeobj[i].forca:
                    listadeobj[i], listadeobj[i-1] = listadeobj[i-1], listadeobj[i]
    elif atributo == 'energia':
        for objeto in range(tam):
            for i in range (tam-1, objeto-1, -1):
                if listadeobj[i-1].energia > listadeobj[i].energia:
                    listadeobj[i], listadeobj[i-1] = listadeobj[i-1], listadeobj[i]
    elif atributo == 'jokempo':
        shuffle(listadeobj)
    else: # Ordem alfabética para o modo manual
        for objeto in range(tam):
            for i in range (tam-1, objeto-1, -1):
                if listadeobj[i-1].personagem < listadeobj[i].personagem:
                    listadeobj[i], listadeobj[i-1] = listadeobj[i-1], listadeobj[i]

    return listadeobj

def alguem_venceu(jogador, jogador2):
    print(('\u001b[35;1m\n\n{} VENCEU A PARTIDA!\u001b[0m' .format(jogador.nome)).center(80, '\t'))
    jogador.vitorias += 1
    jogador.jogos += 1
    jogador2.jogos += 1
    resposta = input('\nVocê quer jogar de novo? S para SIM, qualquer tecla para SAIR ')
    resposta = resposta.upper()
    return (jogador, jogador2)

def fim_do_jogo(jogador1, jogador1_mao, jogador2, jogador2_mao):
    valor, forca, energia = 0, 0, 0
    valor2, forca2, energia2 = 0, 0, 0
    for i in range(len(jogador1_mao)-1):
        valor += jogador1_mao[i].valor
        forca += jogador1_mao[i].forca
        energia += jogador1_mao[i].energia
    for j in range(len(jogador2_mao)-1):
        valor2 += jogador2_mao[j].valor
        forca += jogador2_mao[j].forca
        energia += jogador2_mao[j].energia
    if valor < valor2:
        print('\n\u001b[35;1mA soma das cartas de {} é a menor.\u001b[0m'.format(jogador1.nome))
        tupla = alguem_venceu(jogador1, jogador2)
        arquivo_final(tupla)
    elif valor > valor2:
        print('\n\u001b[35;1mA soma das cartas de {} é a menor.\u001b[0m'.format(jogador2.nome))
        tupla = alguem_venceu(jogador2, jogador1)
        arquivo_final(tupla)
    elif forca < forca2:
        print('\n\u001b[35;1mA soma das cartas de {} é a menor.\u001b[0m'.format(jogador1.nome))
        tupla = alguem_venceu(jogador1, jogador2)
        arquivo_final(tupla)
    elif forca > forca2 :
        print('\n\u001b[35;1mA soma das cartas de {} é a menor.\u001b[0m'.format(jogador2.nome))
        tupla = alguem_venceu(jogador2, jogador1)
        arquivo_final(tupla)
    elif energia < energia2:
        print('\n\u001b[35;1mA soma das cartas de {} é a menor.\u001b[0m'.format(jogador1.nome))
        tupla = alguem_venceu(jogador1, jogador2)
        arquivo_final(tupla)
    elif energia > energia2:
        print('\n\u001b[35;1mA soma das cartas de {} é a menor.\u001b[0m'.format(jogador2.nome))
        tupla = alguem_venceu(jogador2, jogador1)
        arquivo_final(tupla)
    else:
        print('\nEMPATE!\nNão houve vencedor!!')
        jogador1.jogos += 1
        jogador2.jogos += 1
        tupla = (jogador1, jogador2)
        arquivo_final(tupla)
        resposta = input('\nVocê quer jogar de novo? S para SIM, qualquer tecla para SAIR ')
        resposta = resposta.upper()
        if resposta == 'S':
            Inicio_do_Jogo()
        else:
            quit()

def exibir_mao(nome, mao_jogador):
        # Como centralizar e deixar isso bonitinho????
    print()
    print('\u001b[35;1m',(' Cartas de {} ' .format(nome)).center(80, '~'))
    print(('PERSONAGEM ~ VALOR ~ FORÇA ~ ENERGIA ~ JOKEMPÔ').center(80))
    if len(mao_jogador) != 0:
        for i in range (len(mao_jogador)):
            sleep(1.0)
            print('{}  {}  {}  {}  {}'.format(mao_jogador[i].personagem,
                   mao_jogador[i].valor,
                   mao_jogador[i].forca,
                   mao_jogador[i].energia,
                   mao_jogador[i].jokempo).center(80))
        print('\u001b[0m')
    else:
        print('\n{} já jogou todas as suas cartas...' .format(nome))
        alguem_venceu(nome)

def exibir_jogada(nome, carta): # Exibe a carta lançada pelo jogador.
    sleep(0.5)
    print()
    print('\u001b[35;1m',(' {} lançou a carta: ' .format(nome)).center(80, '~'))
    sleep(1.5)
    print(('PERSONAGEM ~ VALOR ~ FORÇA ~ ENERGIA ~ JOKEMPÔ').center(80))
    return print('{}  {}  {}  {}  {}\u001b[0m'.format(carta.personagem,
       carta.valor,
       carta.forca,
       carta.energia,
       carta.jokempo).center(80))

def disputar(p1, p2, atributo, pilha, lista):
    # Fução que joga os dados e faz a disputa automática
    p1_rodadas = 0 # Contadores locais para as rodadas...
    p2_rodadas = 0
    # Os dados são lançados para sortear a carta da disputa
    dado = randint(0, len(p1.mao)-1)
    sleep(0.75)
    print('\nO dado de {} sorteou {}!' .format(p1.nome, dado+1))
    jogada1 = p1.mao.pop(dado)
    exibir_jogada(p1.nome, jogada1)

    dado2 = randint(0, len(p2.mao)-1)
    sleep(2.0)
    print('\nO dado de {} sorteou {}!' .format(p2.nome, dado2+1))
    jogada2 = p2.mao.pop(dado2)
    exibir_jogada(p2.nome, jogada2)

    # Disputas por atributo:
    if atributo == 'valor':
        if jogada1.valor > jogada2.valor:
            sleep(1.0)
            print('\n')
            print(('{} venceu a rodada!' .format(p1.nome)).center(80, '~'))
            p1_rodadas += 1
            carta = pilha.pop()
            p2.mao.append(carta) # O Jogador que perdeu compra uma carta da pilha
        elif jogada1.valor < jogada2.valor:
            sleep(1.0)
            print('\n')
            print(('{} venceu a rodada!' .format(p2.nome)).center(80, '~'))
            p2_rodadas += 1
            carta = pilha.pop()
            p1.mao.append(carta) # Será que a lista Pilha deve ser passada como parâmetro?
                                #  Não precisou!
        else:
            sleep(1.0)
            print('\n\nÉ um empate!')
            carta = pilha.pop() #  Ambos os jogadores pegam uma nova carta
            p1.mao.append(carta)
            carta = pilha.pop()
            p1.mao.append(carta)
    elif atributo == 'forca':
        if jogada1.forca > jogada2.forca:
            sleep(1.0)
            print('\n')
            print(('{} venceu a rodada!' .format(p1.nome)).center(80, '~'))
            p1_rodadas += 1
            carta = pilha.pop()
            p2.mao.append(carta)
        elif jogada1.forca < jogada2.forca:
            sleep(1.0)
            print('\n')
            print(('{} venceu a rodada!' .format(p2.nome)).center(80, '~'))
            p2_rodadas += 1
            carta = pilha.pop()
            p1.mao.append(carta) 
        else:
            sleep(1.0)
            print('\n\nÉ um empate!')
            carta = pilha.pop()
            p1.mao.append(carta)
            carta = pilha.pop()
            p1.mao.append(carta)
    elif atributo == 'energia':
        if jogada1.energia > jogada2.energia:
            sleep(1.0)
            print('\n')
            print(('{} venceu a rodada!' .format(p1.nome)).center(80, '~'))
            p1_rodadas += 1
            carta = pilha.pop()
            p2.mao.append(carta)
        elif jogada1.energia < jogada2.energia:
            sleep(1.0)
            print('\n')
            print(('{} venceu a rodada!' .format(p2.nome)).center(80, '~'))
            p2_rodadas += 1
            carta = pilha.pop()
            p1.mao.append(carta)
        else:
            sleep(1.0)
            print('\n\nÉ um empate!')
            carta = pilha.pop()
            p1.mao.append(carta)
            carta = pilha.pop()
            p1.mao.append(carta)
    else: # Não há erro de exceção pq o input do usuario ja foi filtrado no inicio
        if jogada1.jokempo == 'Pedra' and jogada2.jokempo == 'Tesoura':
            sleep(1.0)
            print('\n')
            print(('{} venceu a rodada!' .format(p1.nome)).center(80, '~'))
            p1_rodadas += 1
            carta = pilha.pop()
            p2.mao.append(carta)
        elif jogada1.jokempo == 'Tesoura' and jogada2.jokempo == 'Papel':
            sleep(1.0)
            print('\n')
            print(('{} venceu a rodada!' .format(p1.nome)).center(80, '~'))
            
            p1_rodadas += 1
            carta = pilha.pop()
            p2.mao.append(carta)
        elif jogada1.jokempo == 'Papel' and jogada2.jokempo == 'Pedra':
            sleep(1.0)
            print('\n')
            print(('{} venceu a rodada!' .format(p1.nome)).center(80, '~'))
            p1_rodadas += 1
            carta = pilha.pop()
            p2.mao.append(carta)
        elif jogada2.jokempo == 'Pedra' and jogada1.jokempo == 'Tesoura':
            sleep(1.0)
            print('\n')
            print(('{} venceu a rodada!' .format(p2.nome)).center(80, '~'))
            p2_rodadas += 1
            carta = pilha.pop()
            p1.mao.append(carta)
        elif jogada2.jokempo == 'Tesoura' and jogada1.jokempo == 'Papel':
            sleep(1.0)
            print('\n')
            print(('{} venceu a rodada!' .format(p2.nome)).center(80, '~'))
            p2_rodadas += 1
            carta = pilha.pop()
            p1.mao.append(carta)
        elif jogada2.jokempo == 'Papel' and jogada1.jokempo == 'Pedra':
            sleep(1.0)
            print('\n')
            print(('{} venceu a rodada!' .format(p2.nome)).center(80, '~'))
            p2_rodadas += 1
            carta = pilha.pop()
            p1.mao.append(carta)
        elif jogada1.jokempo == jogada2.jokempo:
            print('É um empate!!')
            carta = pilha.pop()
            p1.mao.append(carta)
            carta = pilha.pop()
            p2.mao.append(carta)

    lista[0] += p1_rodadas
    lista[1] += p2_rodadas
    return lista

def automatico(p1, p2, jogadordavez, listascore):
    sleep(1.25)
    print('\n','\u001b[36;1mVez de {}\u001b[0m'.format(jogadordavez))
    print('\n{}! Selecione o tipo de disputa!'.format(jogadordavez))
    disputa = input('V para VALOR\nF para FORÇA\nE para ENERGIA\nJ para JOKEMPÔ\n: ')
    disputa = disputa.upper()

    if disputa == 'V':
        p1.mao = Bubble(p1.mao, 'valor')
        p2.mao = Bubble(p2.mao, 'valor')
        exibir_mao(p1.nome, p1.mao)
        exibir_mao(p2.nome, p2.mao)
        rodadas = disputar(p1, p2, 'valor', pilha, listascore)
        print(('{} já venceu {} rodadas.'.format(p1.nome, rodadas[0])).center(80))
        print(('{} já venceu {} rodadas.'.format(p2.nome, rodadas[1])).center(80))
    elif disputa == 'F':
        p1.mao = Bubble(p1.mao, 'forca')
        p2.mao = Bubble(p2.mao, 'forca')
        exibir_mao(p1.nome, p1.mao)
        exibir_mao(p2.nome, p2.mao)
        rodadas = disputar(p1, p2, 'forca', pilha, listascore)
        print(('{} já venceu {} rodadas.'.format(p1.nome, rodadas[0])).center(80))
        print(('{} já venceu {} rodadas.'.format(p2.nome, rodadas[1])).center(80))
    elif disputa == 'E':
        p1.mao = Bubble(p1.mao, 'energia')
        p2.mao = Bubble(p2.mao, 'energia')
        exibir_mao(p1.nome, p1.mao)
        exibir_mao(p2.nome, p2.mao)
        rodadas = disputar(p1, p2, 'energia', pilha, listascore)
        print(('{} já venceu {} rodadas.'.format(p1.nome, rodadas[0])).center(80))
        print(('{} já venceu {} rodadas.'.format(p2.nome, rodadas[1])).center(80))
    elif disputa == 'J':
        p1.mao = Bubble(p1.mao, 'jokempo')
        p2.mao = Bubble(p2.mao, 'jokempo')
        exibir_mao(p1.nome, p1.mao)
        exibir_mao(p2.nome, p2.mao)
        rodadas = disputar(p1, p2, 'jokempo', pilha, listascore)
        print(('{} já venceu {} rodadas.'.format(p1.nome, rodadas[0])).center(80))
        print(('{} já venceu {} rodadas.'.format(p2.nome, rodadas[1])).center(80))
        # Caso a disputa seja jokempô, não há ordenação e as cartas serão sorteadas aleatoriamente
    else:
        print('~~~~~~ Oopa!\nPor favor, selecione um modo de disputa válido...')
        print('Comece de novo! :/')
        Inicio_do_Jogo()

def manual(p1, p2, atributo, pilha, lista):
    p1_rodadas = 0
    p2_rodadas = 0
    if len(p1.mao) != 0 and len(p2.mao) != 0:
        indice = int(input('\n{}! Você ainda tem {} cartas.\nEscolha o número da carta que você quer jogar!\n:'
                           .format(p1.nome, len(p1.mao))))
        indice2 = int(input('\n{}! Você ainda tem {} cartas.\nEscolha o número da carta que você quer jogar!\n:'
                            .format(p2.nome, len(p2.mao))))
        try:
            jogada1 = p1.mao.pop(indice-1)
        except:
            print('Você tem {} cartas.\n{}! Você escolheu uma carta inválida e agora vai ter que começar de novo.'
                  '\nEscolha uma carta válida da próxima vez! >:(' .format(p1.nome, len(p1.mao)))
            Inicio_do_Jogo()
        try:
            jogada2 = p2.mao.pop(indice2-1)
        except:
            print('Você tem {} cartas.\n{}! Você escolheu uma carta inválida e agora vai ter que começar de novo.'
                  '\nEscolha uma carta válida da próxima vez! >:(' .format(p2.nome, len(p2.mao)))
            Inicio_do_Jogo()
        exibir_jogada(p1.nome, jogada1)
        exibir_jogada(p2.nome, jogada2)

        if atributo == 'valor':
            if jogada1.valor > jogada2.valor:
                sleep(1.0)
                print('\n')
                print(('{} venceu a rodada!' .format(p1.nome)).center(80, '~'))
                p1_rodadas += 1
                carta = pilha.pop()
                p2.mao.append(carta) # O Jogador que perdeu compra uma carta da pilha
            elif jogada1.valor < jogada2.valor:
                sleep(1.0)
                print('\n')
                print(('{} venceu a rodada!' .format(p2.nome)).center(80, '~'))
                p2_rodadas += 1
                carta = pilha.pop()
                p1.mao.append(carta)
            else:
                sleep(1.0)
                print('\n\nÉ um empate!')
                carta = pilha.pop() #  Ambos os jogadores pegam uma nova carta
                p1.mao.append(carta)
                carta = pilha.pop()
                p2.mao.append(carta)
        elif atributo == 'forca':
            if jogada1.forca > jogada2.forca:
                sleep(1.0)
                print('\n')
                print(('{} venceu a rodada!' .format(p1.nome)).center(80, '~'))
                p1_rodadas += 1
                carta = pilha.pop()
                p2.mao.append(carta)
            elif jogada1.forca < jogada2.forca:
                sleep(1.0)
                print('\n')
                print(('{} venceu a rodada!' .format(p2.nome)).center(80, '~'))
                p2_rodadas += 1
                carta = pilha.pop()
                p1.mao.append(carta)
            else:
                sleep(1.0)
                print('\n\nÉ um empate!')
                carta = pilha.pop()
                p1.mao.append(carta)
                carta = pilha.pop()
                p2.mao.append(carta)
        elif atributo == 'energia':
            if jogada1.energia > jogada2.energia:
                sleep(1.0)
                print('\n')
                print(('{} venceu a rodada!' .format(p1.nome)).center(80, '~'))
                p1_rodadas += 1
                carta = pilha.pop()
                p2.mao.append(carta)
            elif jogada1.energia < jogada2.energia:
                sleep(1.0)
                print('\n')
                print(('{} venceu a rodada!' .format(p2.nome)).center(80, '~'))
                p2_rodadas += 1
                carta = pilha.pop()
                p1.mao.append(carta)
            else:
                sleep(1.0)
                print('\n\nÉ um empate!')
                carta = pilha.pop()
                p1.mao.append(carta)
                carta = pilha.pop()
                p2.mao.append(carta)
        else: # Não há erro de exceção pq o input do usuario ja foi filtrado no inicio
            if jogada1.jokempo == 'Pedra' and jogada2.jokempo == 'Tesoura':
                sleep(1.0)
                print('\n')
                print(('{} venceu a rodada!' .format(p1.nome)).center(80, '~'))
                p1_rodadas += 1
                carta = pilha.pop()
                p2.mao.append(carta)
            elif jogada1.jokempo == 'Tesoura' and jogada2.jokempo == 'Papel':
                sleep(1.0)
                print('\n')
                print(('{} venceu a rodada!' .format(p1.nome)).center(80, '~'))

                p1_rodadas += 1
                carta = pilha.pop()
                p2.mao.append(carta)
            elif jogada1.jokempo == 'Papel' and jogada2.jokempo == 'Pedra':
                sleep(1.0)
                print('\n')
                print(('{} venceu a rodada!' .format(p1.nome)).center(80, '~'))

                p1_rodadas += 1
                carta = pilha.pop()
                p2.mao.append(carta)
            elif jogada2.jokempo == 'Pedra' and jogada1.jokempo == 'Tesoura':
                sleep(1.0)
                print('\n')
                print(('{} venceu a rodada!' .format(p2.nome)).center(80, '~'))

                p1_rodadas += 1
                carta = pilha.pop()
                p1.mao.append(carta)
            elif jogada2.jokempo == 'Tesoura' and jogada1.jokempo == 'Papel':
                sleep(1.0)
                print('\n')
                print(('{} venceu a rodada!' .format(p2.nome)).center(80, '~'))

                p1_rodadas += 1
                carta = pilha.pop()
                p1.mao.append(carta)
            elif jogada2.jokempo == 'Papel' and jogada1.jokempo == 'Pedra':
                sleep(1.0)
                print('\n')
                print(('{} venceu a rodada!' .format(p2.nome)).center(80, '~'))
                p1_rodadas += 1
                carta = pilha.pop()
                p1.mao.append(carta)
            elif jogada1.jokempo == jogada2.jokempo:
                sleep(1.0)
                print('\nÉ UM EMPATE!')
                carta = pilha.pop()
                p1.mao.append(carta)
                carta = pilha.pop()
                p2.mao.append(carta)
            else:
                pass

    elif len(p1.mao) == 0:
        alguem_venceu(p1.nome)
    else:
        alguem_venceu(p2.nome)

    lista[0] += p1_rodadas
    lista[1] += p2_rodadas
    print()
    print(('{} já venceu {} rodadas.'.format(p1.nome, lista[0])).center(80))
    print(('{} já venceu {} rodadas.'.format(p2.nome, lista[1])).center(80))

def tipo_disputa_manual(jogador):
    print('\n{}! Selecione o tipo de disputa!'.format(jogador.nome))
    disputa = input('V para VALOR\nF para FORÇA\nE para ENERGIA\nJ para JOKEMPÔ\n: ')
    disputa = disputa.upper()
    if disputa == 'V':
        disputa = 'valor'
    elif disputa == 'F':
        disputa = 'forca'
    elif disputa == 'E':
        disputa = 'energia'
    elif disputa == 'J':
        disputa = 'jokempo'
    else:
        print('~~~~~~ Oopa!\nPor favor, selecione um modo de disputa válido...')
        print('Comece de novo! :/')
        Inicio_do_Jogo()
    return disputa

def arquivo_jogadores(p1, p2):
    try:
        arq = open('Jogadores.txt', 'r+')
    except FileNotFoundError:
        arq = open('Jogadores.txt', 'w+')
    for line in arq:
        line = line.split(';')
        if p1.nome == line[0]:
            print('Nome: {}\nVitorias: {}\nSucesso: {}'.format(line[0], line[1], line[2]))
            break
    else:
        arq.write('{};{};{};{}%\n'.format(p1.nome, p1.vitorias, p1.jogos, p1.sucesso))
        print('{} foi cadastrado'.format(p1.nome))
    for line in arq:
        line = line.split(';')
        if p2.nome == line[0]:
            print('Nome: {}\nVitorias: {}\nSucesso: {}'.format(line[0], line[1], line[2]))
            break
    else:
        arq.write('{};{};{};{}%\n'.format(p2.nome, p2.vitorias, p2.jogos, p2.sucesso))
        print('{} foi cadastrado.'.format(p2.nome))
    arq.close()

def arquivo_final(tupla):
    p1, p2 = tupla
    arq = open('Jogadores.txt', 'r+')
    for linha in arq:
        linha.split(';')
        if p1.nome == linha[0]:
            linha[1] += p1.vitorias
            linha[2] += p1.jogos
            linha[3] += p1.sucesso
        if p2.nome == linha[0]:
            linha[1] += p2.vitorias
            linha[2] += p2.jogos
            linha[3] += p2.sucesso
    arq.close()

def Inicio_do_Jogo():
    rodadas_score = [0, 0]
    p1 = Player()
    p1.nome = input('Jogador 1! Qual é o seu nickname? ')
    p1.nome = p1.nome.upper()
    exibir_mao(p1.nome, p1.mao)
    sleep(0.5)
    modo_jogo = input('{}! Escolha o modo de jogo: A para AUTOMÁTICO, M para MANUAL\n: ' .format(p1.nome))
    modo_jogo = modo_jogo.upper()

    p2 = Player()
    p2.nome = input('Jogador 2! Qual é o seu nickname? ')
    p2.nome = p2.nome.upper()
    exibir_mao(p2.nome, p2.mao)

    arquivo_jogadores(p1, p2)

    if modo_jogo == 'A':
        for i in range (0, 10):
            print(('RODADA ATUAL: {}' .format(i+1)).center(80))
            if i < 5:
                if i % 2 == 0:
                    automatico(p1, p2, p1.nome, rodadas_score)
                else:
                    automatico(p1, p2, p2.nome, rodadas_score)
            else:
                break
        fim_do_jogo(p1, p1.mao, p2, p2.mao)

    elif modo_jogo == 'M':
        for i in range (10):
            print(('RODADA ATUAL: {}' .format(i+1)).center(80))
            if i < 10:
                if i % 2 == 0:
                    disputa = tipo_disputa_manual(p1)
                    manual(p1, p2, disputa, pilha, rodadas_score)
                else:
                    disputa = tipo_disputa_manual(p2)
                    manual(p1, p2, disputa, pilha, rodadas_score)
            else:
                break
        fim_do_jogo(p1, p1.mao, p2, p2.mao)

Inicio_do_Jogo()
